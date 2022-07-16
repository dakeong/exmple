import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.instagram.com/dakeong_810/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["blue", "black"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "이다경")
write("description", ".")
write("button", "instgram")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "소속": "경서중학교",
  "생년월일": "2007.08.10",
  "해본거": "스크래치. 엔트리. c언어. 파이썬 등",
  "좋아하는 색": "파랑색. 검은색"
}
information(informations)
