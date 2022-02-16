from bs4 import BeautifulSoup

test_html = open('naver_test.html', 'r', encoding='utf-8')

soup = BeautifulSoup(test_html, 'html.parser')
#print(soup.prettify())

tag_h1 = soup.h1
tag_div = soup.div

tag_ul = soup.ul
#print(soup.ul) 여러개의 ul태그 중 첫번째 ul태그만 출력됨

tag_li = soup.li
#print(tag_li) 여러개의 li태그 중 첫번째 li태그만 출력됨

tag_a = soup.a
#print(tag_a)

tag_ul_all = soup.find_all("ul") # 모든 ul태그를 리스트형태로 반환
#print(tag_ul_all[1])

tag_li_all = soup.find_all('li')
#print(tag_li_all[2])

#print(tag_a.attrs) # 해당 태그의 속석이름과 속성값으로 dic형태로 반환
#print(tag_a['href']) # 해당 태그의 속성값만 출력
#print(tag_a['class'])

#print(soup.find('ul',attrs={'class':'section'})) # ul태그 중에서 class가 section인 ul만 출력(파싱)
h1_title=(soup.find(id='title'))
#print(h1_title.string) # 태그빼고 텍스트만 추출

li_list = soup.select('div>ul.section>li')
print(li_list)

print(li_list[0].string)
print(li_list[1].string)

for li in li_list:
    print(li.string)