import requests


def getimg(a):
    query = a
    url = f"https://pixabay.com/api/?key=49887788-81f6b38092977e4c892d71f51&q={query}&image_type=photo"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        image_url = data["hits"][0]["webformatURL"]
        w = data["hits"][0]["webformatWidth"]
        h = data["hits"][0]["webformatHeight"]
        img = requests.get(image_url)
        with open("C:\\Users\\Владелец\\PycharmProjects\\api\\img.jpeg", 'wb') as file:
            file.write(img.content)
        print(f"Вот тебе фото: {image_url}")
        return w,h
    else:
        print(f"Ошибка при запросе: {response.status_code}")
