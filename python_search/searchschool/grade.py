import requests
from bs4 import BeautifulSoup

login_url = 'https://aca.nuk.edu.tw/Student2/login.asp'
grades_url = 'https://aca.nuk.edu.tw/Student2/SO/ScoreQuery.asp'

login_payload = {
    'username': 'a1115513',
    'password': 'pei2004930725'
}

# 使用 session 來保持連線狀態
with requests.Session() as session:

    login_response = session.post(login_url, data=login_payload)

    if login_response.status_code == 200:
        # 登入成功，發送請求以獲取成績
        grades_response = session.get(grades_url)

        # 處理成績頁面的回應
        if grades_response.status_code == 200:

            # 使用 BeautifulSoup 解析 HTML
            soup = BeautifulSoup(grades_response.text, 'html.parser')

            # 找到所有 <td> 標籤
            td_elements = soup.find_all('td')

            # 提取每個 <td> 標籤的文字內容
            for td in td_elements:
                print(td.text)

        else:
            print('無法獲取成績')
    else:
        print('登入失敗')
