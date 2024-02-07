import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope) #adicionar credencial.json detalhado no README
client = gspread.authorize(creds)

def process_student_data(sheet):
    data_range = sheet.get_all_values()
    for i, row in enumerate(data_range[3:28], start=4):  
        student_name = (row[1])
        
        total_grade = sum(float(cell) for cell in row[3:6])
        
        # Calculando a média
        average = round(total_grade / 3)
        miss_class = int(row[2])

        if miss_class > 60 * 0.25:
            situation = "Reprovado por Falta"
        else:
            if any(not cell.strip() or not cell.strip().replace('.', '').isdigit() for cell in row[3:6]):
                situation = "Dados de notas inválidos"
            elif average < 50:
                situation = "Reprovado por Nota"
            elif 50 <= average < 70:
                situation = "Exame Final"
            else:
                situation = "Aprovado"
        
        # Escrevendo a média nas colunas G e H
        sheet.update_cell(i, 7, situation)

        if situation == "Exame Final":
            naf = 100 - average
            sheet.update_cell(i, 8, naf) 
        else:
            sheet.update_cell(i, 8, 0) 

        print(f"Processed data for {student_name}:")
        print(f"- Total Grade: {total_grade}")
        print(f"- Average: {average}")
        print(f"- Miss Classes: {miss_class}")
        print(f"- Situation: {situation}")
        print("----------------------")
        

def main():
    spreadsheet_id = '1yVNNbwZ4iNRDJ42_oN6452Xo7LItYIYXsj7nYheQhtg' #ID da planilha
    sheet = client.open_by_key(spreadsheet_id).sheet1
    
    process_student_data(sheet)
    
    print("All data processed and updated successfully!")

if __name__ == "__main__":
    main()
