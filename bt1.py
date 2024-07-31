import requests
from bs4 import BeautifulSoup
import csv
import json

base_url = 'https://datatables.net/'


def rawl_data():
    try:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        all_data = []

        table = soup.find('table', {'id': 'example'})
        rows = table.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            col=[]
            for ele in cols:
                col.append(ele.text)
            all_data.append(col)

        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(all_data)

        with open('data.json', 'w') as file:
            json.dump(all_data, file, indent=1)


        print('Data saved to file data.csv')

    except Exception as e:
        raise Exception(f"ERROR: {e}")


rawl_data()
