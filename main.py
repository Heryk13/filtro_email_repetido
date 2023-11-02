import csv
import os

desktop_path = os.path.expanduser("~/Desktop")

while True:
    input_filename = input("cole aqui o local do arquivo csv (ou digite 'exit' para fechar): ")

    if input_filename.lower() == "exit":
        print("Fechando o programa.")
        break

    output_filename = os.path.join(desktop_path, "emails_filtrado.csv")

    unique_emails = set()

    with open(input_filename, "r") as input_file:
        csv_reader = csv.reader(input_file)
        for row in csv_reader:
            email = row[0].strip()  # Assuming email is in the first column
            if email:
                unique_emails.add(email)

    with open(output_filename, "w", newline="") as output_file:
        csv_writer = csv.writer(output_file)
        for email in unique_emails:
            csv_writer.writerow([email])

    print("emails filtrado com sucesso\nverifique sua area de trabalho pelo arquivo email_filtrado.csv")