import openai
import os
import GPT_Key

openai.api_key = GPT_Key.key

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
        with open(f"{Logs}.log", "a") as log:
            for Message in self.Messages:
                log.write(str(f"{Message}\n"))
            log.write("\n\n\n")
            log.close()
        os.system("move *.log /logs")

# Data i.e Lists, Sets, Other Stuff

dummy = [
    {
        "name": "Shahzeb",
        "class": "Metric",
        "pic": "https://portal.fbise.edu.pk/fbise-conduct/std-img/img-ssc1/281200131.jpg",
        "result": "https://portal.fbise.edu.pk/fbise-conduct/result/Result-link-ssc1.php?rollNo=9035206",
        "marks": "475"
    },
    {
        "name": "Zaryab",
        "class": "Metric",
        "pic": "https://portal.fbise.edu.pk/fbise-conduct/std-img/img-ssc1/281200119.jpg",
        "result": "https://portal.fbise.edu.pk/fbise-conduct/result/Result-link-ssc1.php?rollNo=9035194",
        "marks": "475"
    }
]