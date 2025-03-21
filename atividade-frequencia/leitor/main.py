import csv

class leitor:
    def ler_csv():

        csv_file = '/home/caiquefrd/fatec/estatistica-aplicada/dados_A618_D_2022-10-01_2023-12-31.csv'

        temp_media = []

        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            
            headers = next(reader)
            
            for row in reader:
                if len(row) >= 2:
                    combined_field = row[1]
                    
                    values = combined_field.split(',')
                    
                    if len(values) >= 1:
                        temperatura = values[0]
                        temp_media.append(temperatura)

        return temp_media
