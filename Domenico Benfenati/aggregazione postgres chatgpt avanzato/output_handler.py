import csv

def write_to_csv(data, output_file):
    try:
        with open(output_file, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['tipoprodotto', 'annoproduzione', 'dimensionetotalemanuali'])
            csv_writer.writerows(data)
    except Exception as e:
        raise Exception(f"Error writing to CSV file: {e}")
