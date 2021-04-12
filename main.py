import json
import requests

def main():
    api_token = '2619421814940190'
    api_address = 'https://www.superheroapi.com/api.php'
    characters = ['Hulk', 'Captain America', 'Thanos']
    all_characters_dict = {}
    responce_ok = False
    for character in characters:
        url = f'{api_address}/{api_token}/search/{character}'
        response = requests.get(url)
        if response.status_code == 200:
            character_dict = json.loads(response.text)
            if character_dict['response'] == 'success':
                all_characters_dict[character] = int(character_dict['results'][0]['powerstats']['intelligence'])
                responce_ok = True
            else:
                print(f'Ошибка в ответе от API - {character_dict["error"]}')
        else:
            print(f'Ошибка доступа к API - {response.status_code}')

    if responce_ok:
        most_intelligent_character = max(all_characters_dict, key=all_characters_dict.get)
        print(f'Самый умный персонаж - {most_intelligent_character}')

if __name__ == '__main__':
    main()

