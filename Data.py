import requests
import json
import openai
import sys

class Main:    
    def __init__(self) -> None:
        self.data = [
        {
        'name':'Shahzeb',
        'link':'https://portal.fbise.edu.pk/fbise-conduct/result/Result-link-ssc1.php?rollNo=9035206',
        'marks': "475",
        'class': 'Metric',
        'pic': 'https://portal.fbise.edu.pk/fbise-conduct/std-img/img-ssc1/281200131.jpg'},
        
        {
        'name': 'Hira',
        'link':'https://portal.fbise.edu.pk/fbise-conduct/result/Result-link-hssc1.php?rollNo=489297',
        'marks': "355",
        'class': '2nd Year',
        'pic': 'https://portal.fbise.edu.pk/fbise-conduct/std-img/img-HSSC1_2nd/281200001.jpg'
        }]


    def Result_data(self) -> list:
        return self.data
    
    
    def get_meme():
        url = "https://meme-api.com/gimme"
        response = json.loads(requests.request("GET", url).text)
        return response['url']
    
class ChatGPT: 
    def __init__(self, role) -> None:
        self.Messages =  [
                {"role": "system", "content": role}       
            ]
    
    
    def ask(self, Q: str) -> str:
        self.Messages.append({"role": "user", "content": Q})
        
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=self.Messages
        ) 
        self.Messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
        return response["choices"][0]["message"]["content"]
    
    
    def Saving_Messages(self) -> None:
        title = "Please Provide a 3 Worded Title for this conversation. NOTE: Only 3 Words and should described what we talked about."
        Logs = self.ask(title)
        sys.path.append("/logs")
        with open(f"{Logs}.log", "a") as log:
            for Message in self.Messages:
                log.write(str(f"{Message}\n"))
            log.write("\n\n\n")
            log.close()
    






# Data i.e Lists, Sets, Other Stuff