import csv

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.15min.lt/').text
soup = BeautifulSoup(source, 'html.parser')

blokai = soup.find_all('div', class_='<class="col-18">

<
with open("Telia Samsung telefonai.csv", "w", encoding="UTF-8", newline='') as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(['Modelis', 'Mėnesio kaina', 'Kaina'])

    for blokas in blokai:
        try:
            pavadinimas = blokas.find('a', class_ = 'card__title js-product-name-truncate').text.strip()
            men_kaina = blokas.find('div', class_ = 'pull-left').span.text.strip()
            kaina = blokas.find('span', class_ = 'price--marker').next_element.next_element.next_element.next_element.span.text.strip()
            csv_writer.writerow([pavadinimas, men_kaina, kaina])
        except:
            pass