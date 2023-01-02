import sqlite3
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message,CallbackQuery
from buttons import *
from config import *




logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

Admin = 708006401

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS user1(
        id integer,
        username varchar(60),
        first_name varchar(60),
        kurs_nomi varchar(50) NULL,
        tel_nomer integer NULL,
        ariza_shikoyatlar varchar(250) NULL
       
        )""")
    conn.commit()


    user_id = message.chat.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    c.execute(f"SELECT id FROM user1 WHERE id = {user_id}")
    data = c.fetchone()

    if data is None:
        c.execute("INSERT INTO user1 VALUES ({},'{}','{}',NULL,NULL,NULL)".format(user_id,username,first_name))
        conn.commit()
        javob1=f"*Assalomu aleykum😊 * \n*ZUCCO academiyasiga Xush kelibsz!💻*"
        await message.reply_photo(
            photo = open("images/zucco.jpg","rb"),
            caption=""" Bizning saytimiz ➡️ zucco.academy""",reply_markup= bosh_menu) 
        await message.reply(javob1,parse_mode="markdown",reply_markup=pas_menu)
        
    else:
        javob1 =f"*Siz ro\'yxatdan o\'tkansiz✅*"
        await message.reply_photo(
            photo = open("images/zucco.jpg","rb"),
            caption=""" Bizning saytimiz ➡️ zucco.academy""",reply_markup= bosh_menu) 
        await message.reply(javob1,parse_mode="markdown",reply_markup=pas_menu)


@dp.message_handler(content_types=['contact'])
async def contact(message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    usertext = message.text
    tel = int(message.contact['phone_number'])
    c.execute(f"UPDATE user1 SET tel_nomer = {tel} WHERE id = {user_id} ")    
    conn.commit()
    conn = sqlite3.connect('zucco.db')
    c.execute(f"SELECT * FROM user1 WHERE id = {user_id}")
    data = c.fetchone()
    print(data)
    c = conn.cursor()
    jb = f"*Ro'yxatdan o'tdingiz✅\nTez orada siz bilan bog'lanishadi📞*"
    await message.answer(jb,parse_mode ="markdown",reply_markup=bosh_menu)
    await message.answer("menu",reply_markup=pas_menu)
    await bot.send_message(Admin,f"ID: #{data[0]}\nUsername: @{data[1]}\nF.I.O: {data[2]}\nTelefon raqami: +{data[4]}\nKurs yo'nalishi: {data[3]}")



@dp.message_handler(commands=['2021202232'])
async def oshish(message: types.Message):
    conn = sqlite3.connect("zucco.db")
    c = conn.cursor()
    c.execute("SELECT * FROM user1")
    data = c.fetchall()
    for dat in data:
      user_id = dat[0]
      await bot.send_message(chat_id = user_id,text = f"☺️Assalomu aleykum 'ZUCCO ACADEMIYA' o'quvchilari\n\nYalshanba kuni 01.03.2022 kuni soat 14:00 da\n🌐Backend bo'yicha ochiq dars bo'ladi sizni Academiyamizda kutb qolamz")



@dp.callback_query_handler(text="biz")
async def til_tanlash(call:CallbackQuery):
    javob3=f"*Qaysi kursimizga yozilmoqchisz ☺️*"
    await call.message.answer(javob3,parse_mode="markdown",reply_markup=lan_nopka)
    await call.message.delete()

@dp.callback_query_handler(text="haq")
async def til_tanlash(call:CallbackQuery):
    javob2=f"*Qaysi kursimiz xaqida malumot olmoqchisz ☺️*"
    await call.message.answer(javob2,parse_mode="markdown",reply_markup=lan1_nopka)
    await call.message.delete()


####################################################################rus
@dp.callback_query_handler(text="zap")
async def til_tanlash(call:CallbackQuery):
    javob312=f"*На какой курс вы хотите записаться? ☺️*"
    await call.message.answer(javob312,parse_mode="markdown",reply_markup=lan00_nopka)
    await call.message.delete()

@dp.callback_query_handler(text="okur")
async def til_tanlash(call:CallbackQuery):
    javob222=f"*О каком курсе вы хотите узнать? ☺️*"
    await call.message.answer(javob222,parse_mode="markdown",reply_markup=lan100_nopka)
    await call.message.delete()



#####################################################################################################
@dp.callback_query_handler(text="back1")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/zucco.jpg","rb"),
        caption=""" Bizning saytimiz ➡️ zucco.academy""",reply_markup= bosh_menu) 
    await call.message.answer("menu",reply_markup=pas_menu) 
    await call.message.delete()


@dp.callback_query_handler(text="backkk")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/zucco.jpg","rb"),
        caption=""" Наш сайт ➡️ zucco.academy""",reply_markup= glav_menu) 
    await call.message.answer("меню",reply_markup=vniz_menu) 
    await call.message.delete()



@dp.callback_query_handler(text="back2")
async def til_tanlash(call:CallbackQuery):
    javob9=f"*Qaysi kursimiz xaqida malumot olmoqchisz ☺️*"
    await call.message.answer(javob9,parse_mode="markdown",reply_markup=lan1_nopka)
    await call.message.delete()

@dp.callback_query_handler(text="back200")
async def til_tanlash(call:CallbackQuery):
    javob900=f"*О каком курсе вы хотите узнать? ☺️*"
    await call.message.answer(javob900,parse_mode="markdown",reply_markup=lan100_nopka)
    await call.message.answer('меню',reply_markup=vniz_menu)
    await call.message.delete()





@dp.callback_query_handler(text="back9")
async def til_tanlash(call:CallbackQuery):
  await call.message.answer_photo(
    photo = open("images/zucco.jpg","rb"),
    caption=""" Bizning saytimiz ➡️ zucco.academy""",reply_markup= bosh_menu) 
  await call.message.answer('menu',reply_markup=pas_menu)


@dp.callback_query_handler(text="back900")
async def til_tanlash(call:CallbackQuery):
  await call.message.answer_photo(
    photo = open("images/zucco.jpg","rb"),
    caption=""" Наш сайт ➡️ zucco.academy""",reply_markup= glav_menu) 
  await call.message.answer('меню',reply_markup=vniz_menu)


@dp.message_handler(text="🔙orqaga")
async def til_tanlash(message:types.Message):
  await message.answer_photo(
    photo = open("images/zucco.jpg","rb"),
    caption=""" Bizning saytimiz ➡️ zucco.academy""",reply_markup= bosh_menu) 
  await message.answer("menu",reply_markup=pas_menu) 


@dp.message_handler(text="🔙назад")
async def til_tanlash(message:types.Message):
  await message.answer_photo(
    photo = open("images/zucco.jpg","rb"),
    caption=""" Наш сайт ➡️ zucco.academy""",reply_markup= glav_menu) 
  await message.answer("меню",reply_markup=vniz_menu) 



###########################################################################
@dp.message_handler(text='💻 IT Project Menejment')
async def oqish(message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '💻 IT Project Menejment' WHERE id = {user_id} ")
    conn.commit()
    javob4=f"*Raqamingizni yuboring😊👇🏻*"
    await message.answer(javob4,parse_mode="markdown",reply_markup=con_nopka)


@dp.message_handler(text='💻 IT Project Menejment')
async def oqish(message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '💻 IT Project Menejment' WHERE id = {user_id} ")
    conn.commit()
    javob400=f"*Отправьте свой номер😊👇🏻*"
    await message.answer(javob400,parse_mode="markdown",reply_markup=con0_nopka)
#####################################################################################
@dp.message_handler(text='✅ IT start')
async def oqish(message: types.Message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '✅ IT start' WHERE id = {user_id} ")
    conn.commit()
    javob4=f"*Raqamingizni yuboring😊👇🏻*"
    await message.answer(javob4,parse_mode="markdown",reply_markup=con_nopka)


@dp.message_handler(text='✅ IT start')
async def oqish(message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '✅ IT start' WHERE id = {user_id} ")
    conn.commit()
    javob400=f"*Отправьте свой номер😊👇🏻*"
    await message.answer(javob400,parse_mode="markdown",reply_markup=con0_nopka)
########################################################################################################
@dp.message_handler(text='📃 Savodxonlik')
async def contact(message: types.Message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '📃 Savodxonlik' WHERE id = {user_id} ")
    conn.commit()
    javob4=f"*Raqamingizni yuboring😊👇🏻*"
    await message.answer(javob4,parse_mode="markdown",reply_markup=con_nopka)


@dp.message_handler(text='📃 Грамотность')
async def oqish(message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '📃 Грамотность' WHERE id = {user_id} ")
    conn.commit()
    javob400=f"*Отправьте свой номер😊👇🏻*"
    await message.answer(javob400,parse_mode="markdown",reply_markup=con0_nopka)
    
####################################################################################
@dp.message_handler(text='🚀 Flatter')
async def echo(message: types.Message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '🚀 Flatter' WHERE id = {user_id} ")
    conn.commit()
    javob4=f"*Raqamingizni yuboring😊👇🏻*"
    await message.answer(javob4,parse_mode="markdown",reply_markup=con_nopka)



@dp.message_handler(text='🚀 Flatter')
async def oqish(message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '🚀 Flatter' WHERE id = {user_id} ")
    conn.commit()
    javob400=f"*Отправьте свой номер😊👇🏻*"
    await message.answer(javob400,parse_mode="markdown",reply_markup=con0_nopka)

@dp.message_handler(text='🌐 Frontend Developer')
async def echo(message: types.Message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '🌐 Frontend Developer' WHERE id = {user_id} ")
    conn.commit()
    javob4=f"*Raqamingizni yuboring😊👇🏻*"
    await message.answer(javob4,parse_mode="markdown",reply_markup=con_nopka)


@dp.message_handler(text='🌐 Frontend Developer')
async def oqish(message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '🌐 Frontend Developer' WHERE id = {user_id} ")
    conn.commit()
    javob400=f"*Отправьте свой номер😊👇🏻*"
    await message.answer(javob400,parse_mode="markdown",reply_markup=con0_nopka)

@dp.message_handler(text='💠 Vuejes')
async def echo(message: types.Message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '💠 Vuejes' WHERE id = {user_id} ")
    conn.commit()
    javob4=f"*Raqamingizni yuboring😊👇🏻*"
    await message.answer(javob4,parse_mode="markdown",reply_markup=con_nopka)


@dp.message_handler(text='💠 Vuejes')
async def oqish(message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '💠 Vuejes' WHERE id = {user_id} ")
    conn.commit()
    javob400=f"*Отправьте свой номер😊👇🏻*"
    await message.answer(javob400,parse_mode="markdown",reply_markup=con0_nopka)


@dp.message_handler(text='📂 PHP')
async def echo(message: types.Message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '📂 PHP' WHERE id = {user_id} ")
    conn.commit()
    javob4=f"*Raqamingizni yuboring😊👇🏻*"
    await message.answer(javob4,parse_mode="markdown",reply_markup=con_nopka)


@dp.message_handler(text='📂 PHP')
async def oqish(message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '📂 PHP' WHERE id = {user_id} ")
    conn.commit()
    javob400=f"*Отправьте свой номер😊👇🏻*"
    await message.answer(javob400,parse_mode="markdown",reply_markup=con0_nopka)


@dp.message_handler(text='🖥 JAVA')
async def echo(message: types.Message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '🖥 JAVA' WHERE id = {user_id} ")
    conn.commit()
    javob4=f"*Raqamingizni yuboring😊👇🏻*"
    await message.answer(javob4,parse_mode="markdown",reply_markup=con_nopka)


@dp.message_handler(text='🖥 JAVA')
async def oqish(message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '🖥 JAVA' WHERE id = {user_id} ")
    conn.commit()
    javob400=f"*Отправьте свой номер😊👇🏻*"
    await message.answer(javob400,parse_mode="markdown",reply_markup=con0_nopka)


@dp.message_handler(text='🎬 Cinema 4')
async def echo(message: types.Message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '🎬 Cinema 4' WHERE id = {user_id} ")
    conn.commit()
    javob4=f"*Raqamingizni yuboring😊👇🏻*"
    await message.answer(javob4,parse_mode="markdown",reply_markup=con_nopka)


@dp.message_handler(text='🎬 Cinema 4')
async def oqish(message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '🎬 Cinema 4' WHERE id = {user_id} ")
    conn.commit()
    javob400=f"*Отправьте свой номер😊👇🏻*"
    await message.answer(javob400,parse_mode="markdown",reply_markup=con0_nopka)

@dp.message_handler(text='🧩 Unity')
async def echo(message: types.Message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '🧩 Unity' WHERE id = {user_id} ")
    conn.commit()
    javob4=f"*Raqamingizni yuboring😊👇🏻*"
    await message.answer(javob4,parse_mode="markdown",reply_markup=con_nopka)


@dp.message_handler(text='🧩 Unity')
async def oqish(message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '🧩 Unity' WHERE id = {user_id} ")
    conn.commit()
    javob400=f"*Отправьте свой номер😊👇🏻*"
    await message.answer(javob400,parse_mode="markdown",reply_markup=con0_nopka)


@dp.message_handler(text='📈 Unreal engine')
async def echo(message: types.Message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '📈 Unreal engine' WHERE id = {user_id} ")
    conn.commit()
    javob4=f"*Raqamingizni yuboring😊👇🏻*"
    await message.answer(javob4,parse_mode="markdown",reply_markup=con_nopka)

@dp.message_handler(text='📈 Unreal engine')
async def oqish(message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    user_id = message.chat.id
    c.execute(f"UPDATE user1 SET kurs_nomi = '📈 Unreal engine' WHERE id = {user_id} ")
    conn.commit()
    javob400=f"*Отправьте свой номер😊👇🏻*"
    await message.answer(javob400,parse_mode="markdown",reply_markup=con0_nopka)


###################################################################################
#1
@dp.callback_query_handler(text="project")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/hgh.jpg","rb"),
        caption="""🌐Web dasturlash\n\n -Frontend - 'Tashqi interfeys' degan ma’noni bildirib, web dasturlashning bir qismi hisoblanadi.\n-Bu texnologiya yordamida web sahifalarning insonga ko‘rinib turuvchi, ma’lumot beruvchi vizual qismi yaratiladi.\n-Frontend: HTML,CSS,SCSS,BOOTSTRAP,JS, daovmiyligi 6 oy jamoviy tarzda otiladi.\n\n📲 Kursni yakunlab nimalar qilish mumkin: web saytlar, avtomatlashtirilgan loyiha tizimlari, web servis va boshqa ko'p funksiyali web saytlar yarata olasiz.\n\n👨‍💻 Ushbu kurs ko'p yillik tajriba ega web dasturchi tomonidan o'tiladi! \n\nzucco.academy""",reply_markup= menu1) 
    await call.message.delete()

#1rus
@dp.callback_query_handler(text="pro")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/hgh.jpg","rb"),
        caption="""🌐Веб-программирование \n \n -Frontend - означает «внешний интерфейс» и является частью веб-программирования. \n-Эта технология создает видимую и информативную визуальную часть веб-страниц. \n -Frontend: HTML, CSS, SCSS , BOOTSTRAP, JS, продолжительность 6 месяцев. \n \n📲 Что вы сможете делать после прохождения курса: вы сможете создавать сайты, автоматизированные системы проектов, веб-сервисы и другие многофункциональные сайты . \n \n👨‍💻 Данный курс преподается веб-программистом с многолетним стажем! \n \nzucco.academy""",reply_markup= menu100) 
    await call.message.answer("меню",reply_markup=vniz_menu) 
    await call.message.delete()

#2
@dp.callback_query_handler(text="start")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/start.jpg","rb"),
        caption=""" ✅IT start\n\n\nIT START kursi dasturlashga kirib kelayotgan har bir talaba uchun juda muhim hisoblanadi.\nUnda siz dasturchilar bilishi kerak bo'lgan eng kerakli bilimlarni o'rganasiz.\nBundan tashqari IT sohasidagi keng tarqalgan kasblar, Backend Development va Frontend yo'nalishlari bilan o'z sohasining tajribali mutahassislari tushuntirib berishadi. Kurs yakunida o'z yo'nalishingizni tanlab, shu sohada o'qishni davom ettirasiz.\n\n📲 Kurs davomida sizga sizga Frontend va Backend soxasi tushuntirildi:IOS va ANDROID mobil ilova yaratishingiz mumkun\n\n👨‍💻 Ushbu kurs ko'p yillik tajriba ega web dasturchi tomonidan o'tiladi! IT start: Google Docs, GitHub, HTML, CSS\n\n zucco.academy""",reply_markup= menu1) 

    await call.message.delete()

#2rus

@dp.callback_query_handler(text="it")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/start.jpg","rb"),
        caption="""✅IT start\n\n\nIT START курс очень важен для каждого студента, поступающего на программирование.\nЗатем вы получите самые необходимые знания, которые необходимо знать программистам.Направления фронтенда объясняют опытные профессионалы своего дела. По окончанию курса вы сможете выбрать свое направление и продолжить обучение в этой сфере.'p проходит веб-программист с многолетним стажем! ИТ-старт: Google Docs, GitHub, HTML, CSS\n\n zucco.academy""",reply_markup= menu100) 
    await call.message.answer("меню",reply_markup=vniz_menu) 
    await call.message.delete()

#3
@dp.callback_query_handler(text="savod")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/word.jpg","rb"),
        caption="""zucco.academy""",reply_markup= menu1) 

    await call.message.delete()
#3rus
@dp.callback_query_handler(text="gram")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/word.jpg","rb"),
        caption="""zucco.academy""",reply_markup= menu100) 
  
    await call.message.delete()

#4
@dp.callback_query_handler(text="front")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/front.jpg","rb"),
        caption="""🌐Web dasturlash\n\n -Frontend - 'Tashqi interfeys' degan ma’noni bildirib, web dasturlashning bir qismi hisoblanadi.\n-Bu texnologiya yordamida web sahifalarning insonga ko‘rinib turuvchi, ma’lumot beruvchi vizual qismi yaratiladi.\n-Frontend: HTML,CSS,SCSS,BOOTSTRAP,JS, daovmiyligi 6 oy jamoviy tarzda otiladi.\n\n📲 Kursni yakunlab nimalar qilish mumkin: web saytlar, avtomatlashtirilgan loyiha tizimlari, web servis va boshqa ko'p funksiyali web saytlar yarata olasiz.\n\n👨‍💻 Ushbu kurs ko'p yillik tajriba ega web dasturchi tomonidan o'tiladi! \n\nzucco.academy""",reply_markup= menu1) 

    await call.message.delete()


#4 rus
@dp.callback_query_handler(text="dev")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/front.jpg","rb"),
        caption="""🌐Веб-программирование \n \n -Frontend - означает «внешний интерфейс» и является частью веб-программирования. \n-Эта технология создает видимую и информативную визуальную часть веб-страниц. \n -Frontend: HTML, CSS, SCSS , BOOTSTRAP, JS, продолжительность 6 месяцев. \n\n📲 Что вы сможете делать после прохождения курса: вы сможете создавать сайты, автоматизированные системы проектов, веб-сервисы и другие многофункциональные сайты . \n \n👨‍💻 Данный курс преподается веб-программистом с многолетним стажем! \n \nzucco.academy""",reply_markup= menu100) 
    await call.message.answer("меню",reply_markup=vniz_menu) 
    await call.message.delete()



#5
@dp.callback_query_handler(text="vu")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/vue.jpg","rb"),
        caption="""💠Vuejs\n\n Vuejskutubxonasi frontend web dasturini tuzish uchun.Kurs 2 oydan iborat.\n\n📲 Kursni yakunlab nimalar qilish mumkin:\n\n👨‍💻 Ushbu kurs ko'p yillik tajriba ega web dasturchi tomonidan o'tiladi!\n\n\nzucco.academy
""",reply_markup= menu1) 

    await call.message.delete()

#5rus
@dp.callback_query_handler(text="vuej")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/vue.jpg","rb"),
        caption="""💠Vuejs\n\nVuejslibrary для создания фронтенд веб-приложения.Длится курс 2 месяца.\n\n📲 Что можно будет делать после прохождения курса:\n\n👨‍💻 Этот курс преподает веб-программист со многими многолетний опыт! \n  \n \nzucco.academy""",reply_markup= menu100) 
    await call.message.answer("меню",reply_markup=vniz_menu) 
    await call.message.delete()


#6
@dp.callback_query_handler(text="php")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/phhp.jpg","rb"),
        caption="""🌐Backend PHP \n\nBackend - Frontendning aksi hisoblanib, loyihaning ichki, yoki orqa tomoni degan ma’noni anglatadi.\n Ular asosan ma'lumotlar ombori bilan ishlaydi.\nBu qismni ko'rish oddiy foydalanuvchilar uchun mavjud emas.\nFaqatgina admin yoki dasturchilar unga kirish imkoni bo'ladi.\nUmumiy holda qaysidir platformaning hammaga ko’rinmaydigan, yashirin, ichki yoki orqa tomoni uning backend qismi hisoblanadi.\nWeb-Dasturlashning backend qismini PHP da qurish va ishga tushirish bilimlarini o'z ichiga oladi, davomiyligi 6 oydan iborat.\n\n📲 Kursni yakunlab nimalar qilish mumkin:\n\nBackend: javacore, Java, PHP\n\n👨‍💻 Ushbu kurs ko'p yillik tajriba ega web dasturchi tomonidan o'tiladi!\n\n\nzucco.academy""",reply_markup= menu1) 
 
    await call.message.delete()

#6rus
@dp.callback_query_handler(text="phpee")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/phhp.jpg","rb"),
        caption="""🌐Backend PHP \n \nBackend - это противоположность Frontend, то есть внутренняя или задняя часть проекта. \n Они в основном работают с базой данных. \n Этот раздел недоступен для обычных пользователей. \nНЕТолько админ или программисты смогут получить к нему доступ.\nВ целом невидимая, скрытая, внутренняя или тыльная сторона платформы является частью ее бэкенда.6 месяцев.\n\n📲 Что делать после прохождения курса: \n\nБэкенд: javacore, Java, PHP \n \n👨‍💻 Этот курс ведет веб-программист с многолетним стажем! \n \n \nzucco.academy""",reply_markup= menu100) 
    await call.message.answer("меню",reply_markup=vniz_menu) 
    await call.message.delete()

#7
@dp.callback_query_handler(text="java")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/javaaa.jpg","rb"),
        caption="""🌐Backend JAVA \n\nBackend - Frontendning aksi hisoblanib, loyihaning ichki, yoki orqa tomoni degan ma’noni anglatadi.\n Ular asosan ma'lumotlar ombori bilan ishlaydi.\nBu qismni ko'rish oddiy foydalanuvchilar uchun mavjud emas.\nFaqatgina admin yoki dasturchilar unga kirish imkoni bo'ladi.\nUmumiy holda qaysidir platformaning hammaga ko’rinmaydigan, yashirin, ichki yoki orqa tomoni uning backend qismi hisoblanadi.\nJava dasturlash tili bilan tanishish va uni ustida ishlab ishga tushurish , davomiyligi 6 oy iborat\n\n📲 Kursni yakunlab nimalar qilish mumkin:\n\nBackend: javacore, Java, PHP\n\n👨‍💻 Ushbu kurs ko'p yillik tajriba ega web dasturchi tomonidan o'tiladi!\n\n\nzucco.academy""",reply_markup= menu1) 

    await call.message.delete()
#7rus
@dp.callback_query_handler(text="javaaa")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/javaaa.jpg","rb"),
        caption="""🌐Backend JAVA \n \nBackend - это противоположность frontend, то есть внутренняя или задняя часть проекта. \n Они в основном работают с базой данных. \n Этот раздел недоступен для обычных пользователей. \nСмогут только администратор или разработчики для доступа к нему. \nВ целом невидимая, скрытая, внутренняя или тыльная сторона платформы является частью ее бэкенда. \nВведение в язык программирования Java и начало работы над ним, длится 6 месяцев \n \n📲 Что делать после прохождение курса: \n \nBackend: javacore, Java, PHP  \n \n👨‍💻 Этот курс ведет веб-программист с многолетним стажем! \n \n \nzucco.academy""",reply_markup= menu100) 

    await call.message.delete()

#8
@dp.callback_query_handler(text="cinema")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/cinema.jpg","rb"),
        caption="""zucco.academy""",reply_markup= menu1) 

    await call.message.delete()

#8rus
@dp.callback_query_handler(text="cinemaaa")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/cinema.jpg","rb"),
        caption="""zucco.academy""",reply_markup= menu100) 
    await call.message.answer("меню",reply_markup=vniz_menu) 
    await call.message.delete()
#9
@dp.callback_query_handler(text="unity")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/unity.jpg","rb"),
        caption="""🧩UNITY\n\n Unity bu kompyuter va telefon o'yinlari uchun cross-platforma muhiti xisoblanadi.\nUnity 2D va 3D o'yinlar yaratish imkonini beradi\n\n📲 Kursni yakunlab nimalar qilish mumkin:\n\n👨‍💻 Ushbu kurs ko'p yillik tajriba ega web dasturchi tomonidan o'tiladi!\n\n\nzucco.academy""",reply_markup= menu1) 

    await call.message.delete()

#9rus
@dp.callback_query_handler(text="unityaa")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/unity.jpg","rb"),
        caption="""  🧩UNITY  \n \n Unity - это кроссплатформенная среда для компьютерных и телефонных игр. \nUnity позволяет создавать 2D и 3D игры \n \n📲 Что делать после прохождения курса: \n \n👨‍💻 Это Курс ведет веб-разработчик с многолетним опытом! \n \n \nzucco.academy""",reply_markup= menu100) 
    await call.message.answer("меню",reply_markup=vniz_menu) 
    await call.message.delete()

#10
@dp.callback_query_handler(text="unreal")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/engine.jpg","rb"),
        caption="""📈UNREAL\n\nUnreal Engine 4 asoslari, 3D modellar yasash, VR sahnalar qurish, tekstura berish, animatsiya.
Kurs 6 oydan iborat\n\n📲 Kursni yakunlab nimalar qilish mumkin:\n\n👨‍💻 Ushbu kurs ko'p yillik tajriba ega web dasturchi tomonidan o'tiladi!\n\n\nzucco.academy""",reply_markup= menu1) 

    await call.message.delete()
#10rus
@dp.callback_query_handler(text="unrealaa")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/engine.jpg","rb"),
        caption="""📈UNREAL\n\nОсновы Unreal Engine 4, 3D моделирование, построение VR сцены, текстуры, анимация.
Курс длится 6 месяцев \n \n📲 Что можно делать после прохождения курса: \n \n👨‍💻 Этот курс ведет веб-программист с многолетним стажем! \n \n \nzucco.academy""",reply_markup= menu100) 
    await call.message.answer("меню",reply_markup=vniz_menu) 
    await call.message.delete()

#11
@dp.callback_query_handler(text="flatter")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/flutter.jpg","rb"),
        caption="""🚀 Flutter\n\nMobil development - loyihaning aynan mobil operatsion sistemasi uchun quriladigan platforma.\nUlarga misol qilib Android va iOS platformalarini olishimiz mumkin.\nBundan tashqari ularning ikkisini ham o'zida jamlashtirgan\n\n - Flutter.flutter  : dart\n\n👨‍💻 Ushbu kurs ko'p yillik tajriba ega web dasturchi tomonidan o'tiladi!\n\n\nzucco.academy""",reply_markup= menu1) 

    await call.message.delete()
#11rus
@dp.callback_query_handler(text="flotter")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/flutter.jpg","rb"),
        caption="""🚀 Flutter \n \nМобильная разработка — это платформа, построенная для мобильной операционной системы проекта. \nExamples — это платформы Android и iOS. \n👨‍💻 Этот курс преподает веб-разработчик с многолетним опытом! \n \n \nzucco.academy""",reply_markup= menu100) 
    await call.message.answer("меню",reply_markup=vniz_menu) 
    await call.message.delete()



@dp.callback_query_handler(text="yoz")
async def til_tanlash(call:CallbackQuery):
    javob11=f"*Qaysi kursimizga yozilmoqchisz ☺️*"
    await call.message.answer(javob11,parse_mode="markdown",reply_markup=lan_nopka)
    await call.message.delete()

@dp.callback_query_handler(text="zapis")
async def til_tanlash(call:CallbackQuery):
    javob110=f"*На какой курс вы хотите записаться?*"
    await call.message.answer(javob110,parse_mode="markdown",reply_markup=lan00_nopka)
    await call.message.delete()

################################################################################################################################

@dp.callback_query_handler(text='ar')
async def hghg(call:CallbackQuery):
    await call.answer("connected....",show_alert=True ) 

@dp.callback_query_handler(text='infoonas')
async def hghg(call:CallbackQuery):
    await call.answer("connected....",show_alert=True ) 


@dp.callback_query_handler(text="back112")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/zucco.jpg","rb"),
        caption=""" Bizning saytimiz ➡️ zucco.academy""",reply_markup= bosh_menu) 
    await call.message.answer("menu",reply_markup=pas_menu) 
    await call.message.delete()

@dp.callback_query_handler(text="back1121")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/zucco.jpg","rb"),
        caption=""" Наш сайт ➡️ zucco.academy""",reply_markup= glav_menu) 
    await call.message.answer("menu",reply_markup=vniz_menu) 
    await call.message.delete()


#####################################################################################################################

@dp.callback_query_handler(text="man")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/locat.jpg","rb"),
        caption=""" Navoiy shoh ko'chasi 32, Тошкент, Узбекистан\nТашкентский Химико-Технологический Институт""",reply_markup= locatsiya_nopka) 

    await call.message.delete()
    
 

@dp.callback_query_handler(text="nash")
async def til_tanlash(call:CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/locat.jpg","rb"),
        caption=""" Узбекистан, г. Ташкент, пр. Навои, 32 \nТашкентский химико-технологический институт""",reply_markup= locatsiya0_nopka) 
    await call.message.answer("menu",reply_markup=vniz_menu)
    await call.message.delete()

######################################################################################
@dp.message_handler(text='☎️Biz bilan bog\'lanish')
async def bbbb(message: types.Message):
    javobt=f"*Bizning raqamlarimiz\nAdmin: +99871 200-10-01☎️\n\nAdmin: +99893 202-00-01☎️*"
    await message.answer(javobt,parse_mode="markdown",reply_markup=pas_menu)

@dp.message_handler(text='☎️связаться с нами')
async def bbbb(message: types.Message):
    javobtas=f"*Наши номера\nAdmin: +998712001001☎️\n\nAdmin: +998932020101☎️*"
    await message.answer(javobtas,parse_mode="markdown",reply_markup=vniz_menu)


@dp.message_handler(text='⚙️Sozlamalar')
async def bbbb(message: types.Message):
    javobk=f"*LOADING....*"
    await message.answer(javobk,parse_mode="markdown",reply_markup=pas_menu)

@dp.message_handler(text='⚙️Настройки')
async def bbbb(message: types.Message):
    javobkas=f"*LOADING....*"
    await message.answer(javobkas,parse_mode="markdown",reply_markup=vniz_menu)



@dp.message_handler(text='🎁Yangliklar')
async def bbbb(message: types.Message):
    javobl=f"*TEZ KUNDA!🥳*"
    await message.answer(javobl,parse_mode="markdown",reply_markup=pas_menu)

@dp.message_handler(text='🎁Новости')
async def bbbb(message: types.Message):
    javoblas=f"*Скора!🥳*"
    await message.answer(javoblas,parse_mode="markdown",reply_markup=vniz_menu)


@dp.message_handler(text='✍️Ariza va Shikoyatlar')
async def echo(message: types.Message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    javob11=f"*Ariza Takliflarni kiriting✅*"
    await message.answer(javob11,parse_mode="markdown")
    @dp.message_handler(content_types=['text'])
    async def send_text(message: types.Message):
        conn = sqlite3.connect('zucco.db')
        c = conn.cursor()
        user_id = message.chat.id
        text_id = message.text
        c.execute(f"UPDATE user1 SET ariza_shikoyatlar = '{text_id}' WHERE id = {user_id}")    
        conn.commit()
        conn = sqlite3.connect('zucco.db')
        c = conn.cursor()
        c.execute(f"SELECT * FROM user1 WHERE id = {user_id}")
        data = c.fetchone()
        jaa = f"*Arizangiz qabul qlindi✅*"
        await message.answer(jaa,parse_mode ="markdown",reply_markup=op_nopka)
        await bot.send_message(Admin,f"ID: #{data[0]}\nUsername: @{data[1]}\nF.I.O: {data[2]}\nAriza Takliflar: {data[5]}")
       


@dp.message_handler(text='✍️Заявления и жалобы')
async def echo(message: types.Message):
    conn = sqlite3.connect('zucco.db')
    c = conn.cursor()
    javob1122=f"*Введите ваши предложения✅*"
    await message.answer(javob1122,parse_mode="markdown")
    @dp.message_handler()
    async def echo(message: types.Message):
        conn = sqlite3.connect('zucco.db')
        c = conn.cursor()
        user_id = message.chat.id
        usertext = message.text
        c.execute(f"UPDATE user1 SET ariza_shikoyatlar = '{usertext}' WHERE id = {user_id}")    
        conn.commit()
        conn = sqlite3.connect('zucco.db')
        c = conn.cursor()
        c.execute(f"SELECT * FROM user1 WHERE id = {user_id}")
        data = c.fetchone()
        jaa12 = f"*Ваша заявка принята✅*"
        await message.answer(jaa12,parse_mode ="markdown",reply_markup=op0_nopka)
        await bot.send_message(Admin,f"ID: #{data[0]}\nUsername: @{data[1]}\nF.I.O: {data[2]}\nAriza Takliflar: {data[5]}")
       

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)