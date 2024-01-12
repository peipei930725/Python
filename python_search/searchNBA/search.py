import requests
from bs4 import BeautifulSoup
import csv
from opencc import OpenCC

def convert_to_traditional_chinese(text):
    cc = OpenCC('s2twp')  # s: simplified, t: traditional, wp: Taiwan standard
    return cc.convert(text)

def get_nba_data():
    url = 'https://www.qiumiwu.com/player?active=0&team=duxingxia'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        NBA_member = soup.find_all('a', class_="list")

        with open('達拉斯獨行俠.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['球員中文名', '英文名', 'Number', 'Position', 'Height', 'Weight', '選秀', 'Salary']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for member in NBA_member:
                player_name = member.find('span', class_='player-name single-line') 
                team_name = member.find('span', class_='alias') 
                player_number = member.find('span', class_='number') 
                position = member.find('span', class_='position')
                height = member.find('span', class_='height')
                weight = member.find('span', class_='weight') 
                year = member.find('span', class_='join_at') 
                salary = member.find('span', class_='salary') 

                row_data = {
                    '球員中文名': convert_to_traditional_chinese(player_name.text.strip()) if player_name else '',
                    '英文名': convert_to_traditional_chinese(team_name.text.strip()) if team_name else '',
                    'Number': player_number.text.strip() if player_number else '',
                    'Position': convert_to_traditional_chinese(position.text.strip()) if position else '',
                    'Height': height.text.strip() if height else '',
                    'Weight': weight.text.strip() if weight else '',
                    '選秀': year.text.strip() if year else '',
                    'Salary': convert_to_traditional_chinese(salary.text.strip()) if salary else ''
                }

                # 寫入一行資料
                writer.writerow(row_data)

if __name__ == '__main__':
    get_nba_data()
