import requests


def getimg():
    url = "https://dog.ceo/api/breeds/image/random"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        dog_image_url = data['message']
        img = requests.get(dog_image_url)
        with open("C:\\Users\\Владелец\\PycharmProjects\\api\\img.jpeg", 'wb') as file:
            file.write(img.content)
        print(f"Вот тебе бобик: {dog_image_url}")
    else:
        print(f"Ошибка при запросе: {response.status_code}")