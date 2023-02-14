# import requests
# from bs4 import BeautifulSoup

# url = 'https://sports.yahoo.com/nhl/standings/'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# for td in soup.find_all('td', class_='Bdb(primary-border) Ta(end) Px(cell-padding-x)'):
#     span = td.find_previous('span', class_='Va(m) H(40px) Px(cell-padding-x)')
#     print(span.text, td.text)


# import requests
# from bs4 import BeautifulSoup

# url = 'https://sports.yahoo.com/nhl/standings/'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# current_span_text = ""
# line = ""

# for td in soup.find_all('td', class_='Bdb(primary-border) Ta(end) Px(cell-padding-x)'):
#     span = td.find_previous('span', class_='Va(m) H(40px) Px(cell-padding-x)')
#     if current_span_text != span.text:
#         if current_span_text:
#             print(line)
#         line = span.text + " " + td.text
#         current_span_text = span.text
#     else:
#         line += " " + td.text
# if line:
#     print(line)

# import requests
# from bs4 import BeautifulSoup

# url = 'https://sports.yahoo.com/nhl/standings/'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# current_span_text = ""
# line = ""

# for td in soup.find_all('td', class_='Bdb(primary-border) Ta(end) Px(cell-padding-x)'):
#     span = td.find_previous('span', class_='Va(m) H(40px) Px(cell-padding-x)')
#     th = td.find_previous('th', class_='Py(6px) Px(4px) Ta(end)')
#     if current_span_text != span.text:
#         if current_span_text:
#             print(line)
#         line = span.text + " " + th["title"]+ " " + td.text
#         current_span_text = span.text
#     else:
#         line += " " + th["title"]+ " " + td.text
# if line:
#     print(line)

# import requests
# from bs4 import BeautifulSoup

# url = 'https://sports.yahoo.com/nhl/standings/'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# th_title_list = []

# for th in soup.find_all('th', class_='Py(6px) Px(4px) Ta(end)'):
#     th_title_list.append(th["title"])

# print(th_title_list)

# import requests
# from bs4 import BeautifulSoup

# url = 'https://sports.yahoo.com/nhl/standings/'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# current_span_text = ""
# line = ""
# th_title_list = []

# for th in soup.find_all('th', class_='Py(6px) Px(4px) Ta(end)'):
#     # print((th["title"]))
#     th_title_list.append(th["title"])
# print(th_title_list)

# for td in soup.find_all('td', class_='Bdb(primary-border) Ta(end) Px(cell-padding-x)'):
#     span = td.find_previous('span', class_='Va(m) H(40px) Px(cell-padding-x)')
#     # th = td.find_previous('th', class_='Py(6px) Px(4px) Ta(end)')
#     # th_title_list.append(th["title"])
#     if current_span_text != span.text:
#         if current_span_text:
#             print(line)
#         line = span.text + " " + td.text
#         current_span_text = span.text
#     else:
#         line += " " + td.text
# if line:
#     print(line)


# import requests
# from bs4 import BeautifulSoup

# url = 'https://sports.yahoo.com/nhl/standings/'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# current_span_text = ""
# line = ""
# th_title_list = []
# i = 0

# for th in soup.find_all('th', class_='Py(6px) Px(4px) Ta(end)', class_='Py(6px) Px(4px) Ta(end) Ta(c)!' ):
#     th_title_list.append(th["title"])
#     print(th_title_list)

# for td in soup.find_all('td'):
#     span = td.find_previous('span', class_='Va(m) H(40px) Px(cell-padding-x)')
#     if current_span_text != span.text:
#         if current_span_text:
#             print(line)
#         line = span.text + " " + th_title_list[i] + " " + td.text
#         current_span_text = span.text
#         i = 0
#     else:
#         line += " " + th_title_list[i] + " " + td.text
#     i += 1
# if line:
#     print(line)


# import requests
# from bs4 import BeautifulSoup

# url = 'https://sports.yahoo.com/nhl/standings/'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# current_span_text = ""
# line = ""
# th_title_list = []
# i = 0

# for th in soup.find_all('th', class_='Py(6px) Px(4px) Ta(end)'):
#     th_title_list.append(th["title"])

# for td in soup.find_all('td', class_='Bdb(primary-border) Ta(end) Px(cell-padding-x)'):
#     span = td.find_previous('span', class_='Va(m) H(40px) Px(cell-padding-x)')
#     if current_span_text != span.text:
#         if current_span_text:
#             print(line)
#         line = span.text + " " + th_title_list[i] + " " + td.text 
#         current_span_text = span.text
#         i = 0
#     else:
#         line +="(" +  " " + th_title_list[i] + " " + td.text + ")"
#     i += 1
# if line:
#     print(line)

# import requests
# from bs4 import BeautifulSoup

# url = 'https://sports.yahoo.com/nhl/standings/'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# current_span_text = ""
# line = ""
# th_title_list = []
# i = 0

# for th in soup.find_all('th', {'class': ['Py(6px) Px(4px) Ta(end)', 'Py(6px) Px(4px) Ta(end) Ta(c)!']}):
#     th_title_list.append(th["title"])
# print(th_title_list)

# for td in soup.find_all('td', class_='Bdb(primary-border) Ta(end) Px(cell-padding-x)'):
#     span = td.find_previous('span', class_='Va(m) H(40px) Px(cell-padding-x)')
#     if current_span_text != span.text:
#         if current_span_text:
#             print(line)
#         line = span.text + " " + ": " + "(" + th_title_list[i] + " " + td.text + ")" 
#         current_span_text = span.text
#         i = 1
#     else:
#         line += "(" +  " " + th_title_list[i] + " " + td.text + ")" 
#     i += 1
# if line:
#     print(line)

# import requests
# from bs4 import BeautifulSoup

# url = 'https://sports.yahoo.com/nhl/standings/'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# current_span_text = ""
# line = ""
# th_title_list = []
# i = 0

# for th in soup.find_all('th', {'class': ['Py(6px) Px(4px) Ta(end)', 'Py(6px) Px(4px) Ta(end) Ta(c)!']}):
#     th_title_list.append(th["title"])
# print(th_title_list)

# for td in soup.find_all('td', class_='Bdb(primary-border) Ta(end) Px(cell-padding-x)'):
#     span = td.find_previous('span', class_='Va(m) H(40px) Px(cell-padding-x)')
#     if current_span_text != span.text:
#         if current_span_text:
#             print(line)
#         line = span.text + " " + ": " + "(" + th_title_list[i] + " " + td.text + ")" 
#         current_span_text = span.text
#         i = 1
#         with open("output.txt", "a") as file:
#                 file.write(line+"\n")
#         line = span.text + " " + ": " + "(" + th_title_list[i] + " " + td.text
#     else:
#         line += "(" + " " + th_title_list[i] + " " + td.text + ")"
#     i += 1
# if line:
#     with open("output.txt", "w") as file:
#         file.write(line)
#     print("Data written to output.txt")


import requests
from bs4 import BeautifulSoup

url = 'https://sports.yahoo.com/nhl/standings/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

current_span_text = ""
line = ""
th_title_list = []
i = 0

for th in soup.find_all('th', {'class': ['Py(6px) Px(4px) Ta(end)', 'Py(6px) Px(4px) Ta(end) Ta(c)!']}):
    th_title_list.append(th["title"])
print(th_title_list[0])


for td in soup.find_all('td', class_='Bdb(primary-border) Ta(end) Px(cell-padding-x)'):
    span = td.find_previous('span', class_='Va(m)  Px(cell-padding-x)')
    if current_span_text != span.text:
        if current_span_text:
            print(line)
            with open("output.txt", "a") as file:
                file.write(line+"\n")
        line = span.text + " " + ": " + "(" + th_title_list[i] + " " + td.text + "),"
        current_span_text = span.text
        i = 0
    else:
        line += "(" + " " + th_title_list[i] + " " + td.text + "),"
        i += 1

if line:
    with open("output.txt", "a") as file:
        file.write(line+"\n")
    print("Data written to output.txt")



