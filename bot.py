import discord
import openai

discord_token = 'DONT WANT TO REVEAL THE TOKEN(Enter YOur dc bot token)'
openai_api_key = 'DONT WANT TO REVEAL THE KEY(Enter Your openais api key)'

openai.api_key = openai_api_key


with open("chat.txt", "r") as f:
   chat = f.read()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        chat += f"{message.author}: {message.content}\n"
        print(f'Message from {message.author}: {message.content}')
        if self.user != message.author:
            if self.user in message.mentions:
               response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt= f"{chat}\nNyctoGPT :",
                    temperature=1,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                    )
               channel = message.channel
               messageToSend = response.choices[0].text
               await message.channel.send(messageToSend)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(discord_token)
