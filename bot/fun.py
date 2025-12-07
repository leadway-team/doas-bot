import random
import requests
import json

doas = None

async def json_animal_api(animal):
    resp = requests.get(url=f"https://some-random-api.com/animal/{animal}")
    return resp.json()

def register():
    @doas.message_handler(commands=["hack", "heck"])
    async def ver(message):
        hacked_entity = str()
        
        args = message.text.split()
        if len(args) < 2:
            hacked_entity = f"@{message.from_user.username}"
        else:
            hacked_entity = args[1]
        
        hack_status = [
                "was successfully hacked!",
                "wasn't hacked. And don't even try to do it again!",
                "wasn't hacked, there is no intenet.",
                "was hacked, now (s)he's an Illuminati"
        ]
        
        await doas.reply_to(message, f"{hacked_entity} {random.choice(hack_status)}")
    
    @doas.message_handler(commands=["ball"])
    async def ball(message):
        args = message.text.split()
        if len(args) < 2:
            await doas.reply_to(message, "Dude, ask a question.")
            return
        
        
        ball_status = [
                "Yes, sure",
                "Maybe",
                "idk bro",
                "No, I don't think that"
        ]
        
        await doas.reply_to(message, random.choice(ball_status))
    
    @doas.message_handler(commands=["cat", "dog", "fox"])
    async def animal(message):
        args = message.text.split()
        
        a = await json_animal_api(args[0].replace("/", ""))
        
        await doas.send_photo(message.chat.id, a["image"])
