import telebot
from telebot import types
import bd
import requests
token="5092804069:AAFIxhbHKIxNSKnsGenCu-Clvrfxzv0KKvw"
bot=telebot.TeleBot(token)
import re
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,bd.BasaData.login(message.chat.id))


@bot.message_handler(commands=["my"])
def my(message):
    k=bd.BasaData.my(message.chat.id)
    for i in k:
            m=i[1].split(".")
            print(m[1])
            if m[1] in ["png","jpg"]:
                chat_id=message.chat.id
                bot.send_message(message.chat.id,f"Пользователь:{i[0]}")
                photo = open(f'{i[1]}', 'rb')
                bot.send_photo(chat_id, photo)
                bot.send_message(message.chat.id,f"Дата публикации:{i[2]}") 
            elif m[1] in ["mp4"]:
                  bot.send_message(message.chat.id,f"Пользователь:{i[0]}")
                  video = open(f'{i[1]}', 'rb')
                  bot.send_video(message.chat.id, video)
                  bot.send_message(message.chat.id,f"Дата публикации:{i[2]}") 
    
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id,"Это бот-машина времени).Вы может оставлять послания,просто отправляя фото и видео)")
 

   
@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):

    try:


        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src=file_info.file_path;
        bd.BasaData.file(message.chat.id,src)
        with open(src, 'wb') as new_file:
           new_file.write(downloaded_file)
        bot.reply_to(message,"Фото добавлено") 

    except Exception as e:
        bot.reply_to(message,e )
    
@bot.message_handler(content_types=['video'])
def send_text(message):
    bot.send_message(message.chat.id, 'Ты отправил мне видео')
    file_info = bot.get_file(message.video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src =  file_info.file_path
    bd.BasaData.file(message.chat.id,src)
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Видео сохранено")
    

@bot.message_handler(content_types=['voice'])
def repeat_all_message(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src =  file_info.file_path
    bd.BasaData.file(message.chat.id,src)
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, "Аудио сохранено")            
      
@bot.message_handler(content_types=["text"])
def main(message):
    if "/alt" in message.text:
        
       
            
            i=bd.BasaData.random_img()
            
            m=i[1].split(".")
          
            if m[1] in ["png","jpg"]:
                chat_id=message.chat.id
                bot.send_message(message.chat.id,f"Пользователь:{i[0]}")
                photo = open(f'{i[1]}', 'rb')
                bot.send_photo(chat_id, photo)
                bot.send_message(message.chat.id,f"Дата публикации:{i[2]}") 
            elif m[1] in ["mp4"]:
                  bot.send_message(message.chat.id,f"Пользователь:{i[0]}")
                  video = open(f'{i[1]}', 'rb')
                  bot.send_video(message.chat.id, video)
                  bot.send_message(message.chat.id,f"Дата публикации:{i[2]}") 
                  
                  
                  
            
            
            
        
    if "/mg:" in message.text:
        s=message.text.split(":")
        if len(s)==2:
            bd.BasaData.letter(message.chat.id,s[1])
            bot.send_message(message.chat.id,"Ваше письмо-послание успешно отправлено")
         
       
            
        

bot.polling(none_stop=True)