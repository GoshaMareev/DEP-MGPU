import csv
from datetime import datetime

# Список заголовков
column_names = [
    "ID", "CallDate",
    "Q3_Overall_Satisfaction",
    "Q4_911_Operator_Satisfaction",
    "Q5.1_Officer_Provided_Information",
    "Q5.2_Officer_Explained_Procedures",
    "Q5.3_Officer_Professionalism",
    "Q5.4_Officer_Explained_Next_Steps",
    "Q5.5_Officer_Gave_Tips",
    "Q5.6_Officer_Provided_Crime_Information",
    "Q5.7_Officer_Referred_To_Website",
    "Q5.8_Officer_Provided_Assistance",
    "Q5.9_Officer_Listened_To_Concerns",
    "Q5.10_Officer_Answered_Questions",
    "Q6.1_Department_Availability",
    "Q6.2_Department_Crime_Prevention_Resource",
    "Q6.3_Department_Explains_Procedures",
    "Q6.4_Department_Personnel_Professionalism",
    "Q6.5_Department_Focuses_On_Public_Safety",
    "Q6.6_Department_Understands_Neighborhood_Issues",
    "Q6.7_Department_Listens_To_Input",
    "Q7.1_Overall_Neighborhood_Police_Job",
    "Q7.2_Neighborhood_Police_Professionalism",
    "Q7.3_Neighborhood_Police_Resource_For_Problems",
    "Q7.4_Neighborhood_Police_Traffic_Safety",
    "Q7.5_Neighborhood_Police_Park_Safety",
    "Q7.6_Neighborhood_Police_Focus_On_Public_Safety",
    "Q8_Speed_Of_911_Response",
    "Q9_Call_Success_First_Attempt",
    "Q10_Problem_Reaching_Operator",
    "Q11_Number_Of_Dials_To_Reach_Operator",
    "Q12_Overall_Safety_In_Seattle",
    "Q13_Safety_After_Incident",
    "Q14_Safety_After_Service_From_SPD",
    "Q15_Favorability_Towards_SPD",
    "Q16_Safety_Walking_Day",
    "Q17_Safety_Walking_Night",
    "Q19_Contact_Desired",
    "Q21_Unreported_Crime",
    "Q22_When_Unreported_Crime_Occurred",
    "Wave",
    "Q11.1.17_Firsthand_Experience",
    "Q11.2.17_Family_Friends_Coworkers_Experience",
    "Q11.3.17_Television",
    "Q11.4.17_Radio",
    "Q11.5.17_Daily_Newspapers",
    "Q11.6.17_Neighborhood_Newspapers",
    "Q11.7.17_SPD_Blotter_Webpage",
    "Q11.8.17_Local_Blogs",
    "Q11.9.17_News_Outlets_Online",
    "Q11.10.17_Email_Text_Messages",
    "Q11.11.17_SPD_Facebook_Twitter",
    "Q11.12.17_Other_Social_Media",
    "Q5.8.2015_Officer_Provided_Contact_Info",
    "Q7.4.2015_Neighborhood_Police_Traffic_Safety",
    "Q6.5.13_Department_Neighborhood_Resource",
    "Q8.11.13_Social_Media",
    "Q8.8.1_Internet",
    "Q8.9.1_Email",
    "Q8.10.1_Text_Messages",
    "Q8.1orig_Email",
    "Q8.2orig_Text_Messaging",
    "Q8.3orig_SPD_Website",
    "Q8.4orig_US_Mail",
    "Q8.5orig_Neighborhood_Meetings",
    "Q8.6orig_Block_Watch_Meetings",
    "Q8.7orig_Newspaper_Articles",
    "Q8.8orig_Radio_TV_News_Stories",
    "Q6.06_Detective_Follow_Up",
    "Q7.06.1_Detective_Provided_Information",
    "Q7.06.2_Detective_Explained_Procedures",
    "Q7.06.3_Detective_Professionalism",
    "Q7.06.4_Detective_Explained_Next_Steps",
    "Q7.06.5_Detective_Gave_Tips",
    "Q7.06.6_Detective_Provided_Crime_Information",
    "Q8.06_Number_Of_Contacts_With_Police",
    "source01",
    "filter_$"
]

def clean_value(value):
    """Очищает значение, удаляя лишние пробелы и пустые строки"""
    return value.strip() if value else None

def process_row(row):
    """Обрабатывает строку, разделяя её на правильное количество полей"""
    # Первый элемент - ID
    id_ = row[0]

    # Второй элемент - дата (CallDate)
    call_date = row[1]

    # Остальные значения
    values = row[2:]

    # Добавляем недостающие значения в конце строки
    while len(values) < len(column_names) - 2:
        values.append(None)

    # Обрезаем лишние значения в конце строки
    values = values[:len(column_names) - 2]

    # Объединяем всё обратно
    return [id_, call_date] + [clean_value(v) for v in values]

def main(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile, delimiter=';')

        # Записываем заголовок
        writer.writerow(column_names)

        for row in reader:
            # Если строка начинается с числа (ID), обрабатываем её
            if row and row[0].isdigit():
                processed_row = process_row(row)
                writer.writerow(processed_row)

if __name__ == "__main__":
    input_file = 'SPD_9-11_Customer_Satisfaction_Survey_Data.csv'
    output_file = 'cleaned_survey_data.csv'
    main(input_file, output_file)
    print(f"Преобразование завершено. Очищенные данные сохранены в {output_file}")