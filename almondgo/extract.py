# response , request 로 추가해보기 

def findSentence(fileName, findText):
    file = open("winter.html", mode="r", encoding="utf8")

    result = []
    data = file.read()
    data = data.splitlines()

    for line in data:
        sentences = line.split(". ")
        for sentence in sentences:
            sentence = sentence.strip(".")
            if findText in sentence:
                result.append(sentence + ".")

    file.close()
    return result

result = findSentence("winter.html", "봄")


for sentence in result:
    print(sentence)
