import vk
import requests
import json


# URL для получения access token
url_token = 'https://oauth.vk.com/authorize?client_id=5792949&display=page&redirect_url=http://localhost&' \
            'scope=wall,offline&response_type=token&v=5.50'

# Публикация сообщения с изображением на стену
getWallUploadServer = 'https://api.vk.com/method/photos.getWallUploadServer?'
saveWallPhoto = 'https://api.vk.com/method/photos.saveWallPhoto?'
wall_post_url = 'https://api.vk.com/method/wall.post?'

# Публикация изображения в профиль
getOwnerPhotoUploadServer = 'https://api.vk.com/method/photos.getOwnerPhotoUploadServer?'
saveOwnerPhoto = 'https://api.vk.com/method/photos.saveOwnerPhoto?'

# Изображение
photo = {'photo': ('birds800.jpg', open(r'birds800.jpg', 'rb'))}

VK_APP_ID = '5792949'
VK_KEY = 'OIXhmsrkBQwe4WG45qjr'
VK_LOGIN = 'wikisocial2016@gmail.com'
VK_PASS = 'WikiSocial2016'
MY_USER_ID = '403023095'


def upload_msg_to_wall(access_token, img, msg):

    # Получаем ссылку для загрузки изображений
    data = dict(access_token=access_token)
    response = requests.post(getWallUploadServer, data)
    result = json.loads(response.text)

    upload_url = result['response']['upload_url']

    # Загружаем изображение на url
    response = requests.post(upload_url, files=img)
    result = json.loads(response.text)

    # Сохраняем фото на сервере и получаем id
    data = dict(access_token=access_token, photo=result['photo'], hash=result['hash'], server=result['server'])
    response = requests.post(saveWallPhoto, data)
    result = json.loads(response.text)['response'][0]['id']

    # Теперь этот id остается лишь прикрепить в attachments метода wall.post
    data = dict(access_token=access_token, attachments=result, message=msg)
    response = requests.post(wall_post_url, data)
    result = json.loads(response.text)
    # На выходе мы получим в ответе post_id если не было ошибки

    return result


def upload_img_to_profile(access_token, img, crop_x, crop_y, crop_width):
    # Получаем ссылку для загрузки изображений
    data = dict(access_token=access_token)
    response = requests.post(getOwnerPhotoUploadServer, data)
    result = json.loads(response.text)

    upload_url = result['response']['upload_url']

    crop_params = dict(_square_crop='{0},{1},{2}'.format(crop_x, crop_y, crop_width))

    # Загружаем изображение на url
    response = requests.post(upload_url, data=crop_params, files=img)
    result = json.loads(response.text)

    # Сохраняем фото на сервере и получаем id
    data = dict(access_token=access_token, photo=result['photo'], hash=result['hash'], server=result['server'])
    response = requests.post(saveOwnerPhoto, data)
    result = json.loads(response.text)['response']['post_id']

    print(result)
    # # Теперь этот id остается лишь прикрепить в attachments метода wall.post
    # data = dict(access_token=session.access_token, attachments=result, message='123')
    # response = requests.post(wall_post_url, data)
    # result = json.loads(response.text)
    # # На выходе мы получим в ответе post_id если не было ошибки

    return result

if __name__ == "__main__":

    # Авторизация
    session = vk.AuthSession(VK_APP_ID, VK_LOGIN, VK_PASS, scope='offline, wall, photos')

    # res = upload_img_to_profile(access_token=session.access_token, img=photo, crop_x=20, crop_y=20, crop_width=50)
    # res = upload_msg_to_wall(access_token=session.access_token, img=photo, msg='Test')



