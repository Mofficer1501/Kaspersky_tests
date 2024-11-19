import requests
import pytest

def test_send_GET_posts():
    # NAME: Проверка получения всех постов
    # ACTION: Сгенерировать запрос.
    url = 'https://jsonplaceholder.typicode.com/posts'
    # ACTION: Отправить запрос.
    response = requests.get(url)
    # ACTION: Получить ответ.
    data = response.json()
    # ACTION: Проанализировать полученный ответ.
    assert response.status_code == 200
    assert isinstance(data, list)  # Проверяем, что данные - это список
    assert len(data) > 0  # Убедимся, что есть хотя бы один пост
    # RESULT: Проверка кода статуса и структуры данных.
    assert data[0]['id'] == 1  # Проверка, что первый пост имеет id 1


def test_send_POST_posts():
    # NAME: Проверка создания нового поста
    # ACTION: Сгенерировать запрос.
    url = 'https://jsonplaceholder.typicode.com/posts'
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    # ACTION: Отправить запрос.
    response = requests.post(url, json=new_post)
    # ACTION: Получить ответ.
    data = response.json()
    # ACTION: Проанализировать полученный ответ.
    assert response.status_code == 201
    assert data['title'] == new_post['title']
    assert data['body'] == new_post['body']
    assert data['userId'] == new_post['userId']
    # RESULT: Проверка кода статуса и содержимого.
    assert 'id' in data  # Убедимся, что в ответе есть id


def test_send_PUT_post():
    # NAME: Проверка замены существующего поста
    # ACTION: Сгенерировать запрос.
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    updated_post = {
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    # ACTION: Отправить запрос.
    response = requests.put(url, json=updated_post)
    # ACTION: Получить ответ.
    data = response.json()
    # ACTION: Проанализировать полученный ответ.
    assert response.status_code == 200
    assert data['title'] == updated_post['title']
    assert data['body'] == updated_post['body']
    # RESULT: Проверка кода статуса и содержимого.
    assert data['id'] == 1  # Убедимся, что пост с id 1 был обновлён


def test_send_PATCH_post():
    # NAME: Проверка частичного обновления поста
    # ACTION: Сгенерировать запрос.
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    update_data = {
        "title": "partially updated title"
    }
    # ACTION: Отправить запрос.
    response = requests.patch(url, json=update_data)
    # ACTION: Получить ответ.
    data = response.json()
    # ACTION: Проанализировать полученный ответ.
    assert response.status_code == 200
    assert data['title'] == update_data['title']
    # RESULT: Проверка кода статуса и содержимого.
    assert data['id'] == 1  # Убедимся, что пост с id 1 был обновлён


def test_send_DELETE_post():
    # NAME: Проверка удаления поста
    # ACTION: Сгенерировать запрос.
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    # ACTION: Отправить запрос.
    response = requests.delete(url)
    # ACTION: Получить ответ.
    assert response.status_code == 200  # Ожидаем код 200 для успешного удаления
    # ACTION: Проверка: попытка получить удалённый пост должна вернуть ошибку
    response_get = requests.get(url)
    assert response_get.status_code == 404  # После удаления, пост больше не существует
    # RESULT: Проверка кода статуса удаления и получения

# Запуск тестов с использованием pytest
if __name__ == "__main__":
    pytest.main()  # Запускаем pytest для выполнения всех тестов