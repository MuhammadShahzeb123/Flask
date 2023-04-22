import requests
import json


class Main:
    def __init__(self) -> str:
        self.Titles = ['Home', 'About', 'Code']

    def return_titles(self, num) -> str:
        return self.Titles[num]
    
    def get_meme():
        url = "https://meme-api.com/gimme"
        response = json.loads(requests.request("GET", url).text)
        return response['url']
    
    
class ChatGPT:
    def __init__(self) -> None:
        pass
    






# Data i.e Lists, Sets, Other Stuff