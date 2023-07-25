import requests

def shorten_link(full_link, link_name):
    api_key = "e615943c8b5ad81231687f43e3c4b7d920f67"
    base_url = 'https://cutt.ly/api/api.php'

    payload = {'key': api_key, 'short': full_link, 'name' : link_name}
    request = requests.get(base_url, params=payload)
    data = request.json()

    print('')

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']

        print('Title', title)
        print('Link',short_link)
    except:
        status = data['url']['status']
        print('Error Status:', status)

link = input('Enter link:')
name = input('Give name to your link: ')

shorten_link(link, name)

