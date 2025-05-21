import csv
from datetime import datetime

def log_to_csv(keyword, url, filename="logs.csv"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, keyword, url])

