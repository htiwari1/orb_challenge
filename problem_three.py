from bs4 import BeautifulSoup
import urllib.robotparser
import requests
import time

def office_scrape():
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url("http://www.dot.ca.gov/robots.txt")
    rp.read()

    # See if we are allowed to scrape by the site owner
    if not rp.can_fetch("*", "http://www.dot.ca.gov/mail.htm"):
        return "Cannot Scrape due to robots.txt conditions"

    page = requests.get("http://www.dot.ca.gov/mail.htm")

    soup = BeautifulSoup(page.content, 'html.parser')
    root_link = 'http://www.dot.ca.gov'

    offices_link = (soup.find('div', class_='settings-links').findAll('a')[1]['href'])

    # See if we are allowed to scrape by the site owner
    if not rp.can_fetch("*", root_link + offices_link):
        return "Cannot Scrape due to robots.txt conditions"

    # Add a time delay if specified by robots.txt
    rrate = rp.request_rate("*")
    if rrate is not None:
        time.sleep(rrate)

    offices_page = requests.get(root_link + offices_link)
    soup_offices = BeautifulSoup(offices_page.content, 'html.parser')

    office_table_row_list = (soup_offices.find('table', class_='table table-striped').find('tbody').find_all('tr'))
    result_array = []

    for office_row in office_table_row_list:
        office_name = office_row.find_all('td')[0].getText().split('-')[0].replace(':', '').strip()
        office_link = 'http://www.dot.ca.gov'
        office_address = office_row.find_all('td')[1].getText().strip().split('\n')[0]
        office_state = office_row.find_all('td')[1].getText().strip().split('\n')[-1].split(' ')[-2]
        office_zip = office_row.find_all('td')[1].getText().strip().split('\n')[-1].split(' ')[-1].replace('.', '')
        office_phone = office_row.find_all('td')[3].getText().strip().split('Public Affairs/Media Line:')[0].replace(
            'General Information:', '').strip()
        office_city = office_row.find_all('td')[1].getText().strip().split('\n')[-1].replace(office_state, '').replace(
            office_zip, '').replace(',', '').replace('.', '').strip()

        mail_address = office_row.find_all('td')[2].getText().strip().split('\n')[0]
        mail_pobox = None
        if 'P.O. Box' in mail_address:
            mail_pobox = mail_address
            mail_address = None

        mail_state = office_row.find_all('td')[2].getText().strip().split('\n')[-1].split(' ')[-2]
        mail_zip = office_row.find_all('td')[2].getText().strip().split('\n')[-1].split(' ')[-1].replace('.', '')
        mail_city = office_row.find_all('td')[2].getText().strip().split('\n')[-1].replace(mail_state, '').replace(mail_zip,
                                                                                                                   '').replace(
            ',', '').replace('.', '').strip()
        mail_phone = None

        result_json = {}

        result_json['office_name'] = office_name
        result_json['office_link'] = office_link
        result_json['office_address'] = office_address
        result_json['office_city'] = office_city
        result_json['office_state'] = office_state
        result_json['office_zip'] = office_zip
        result_json['office_phone'] = office_phone
        result_json['mail_address'] = mail_address
        result_json['mail_pobox'] = mail_pobox
        result_json['mail_city'] = mail_city
        result_json['mail_state'] = mail_state
        result_json['mail_zip'] = mail_zip
        result_json['mail_phone'] = mail_phone

        try:
            result_json['office_link'] = office_link + (office_row.find_all('td')[0].find('a')['href'])
        except TypeError:
            pass
        result_array.append(result_json)

    return result_array

if __name__ == "__main__":
    print(office_scrape())