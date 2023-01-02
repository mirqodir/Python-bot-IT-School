from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup


# til = ReplyKeyboardMarkup(
# 	keyboard =[
# 		[
# 			KeyboardButton("🇺🇿 Uzbek"),

# 		],
# 		[
# 			KeyboardButton("🇷🇺 Русский"),

# 		],
# 	],
# 	resize_keyboard=True
	

# )
##############################################################################################
bosh_menu = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton('📝Kurslarga yozilish',callback_data = 'biz'),
			InlineKeyboardButton('📃Kurslar haqida ',callback_data = 'haq'),

		],
		[
			InlineKeyboardButton('📍Manzilimiz',callback_data = 'man'),
			InlineKeyboardButton('💻Biz haqimizda malumot',callback_data = 'ar'),

		],

	],
)
####rus
glav_menu = InlineKeyboardMarkup(
	inline_keyboard = [
		[
			InlineKeyboardButton('📝Запись на курсы',callback_data = 'zap'),
			InlineKeyboardButton('📃О курсах',callback_data = 'okur'),

		],
		[
			InlineKeyboardButton('📍Наш адрес',callback_data = 'nash'),
			InlineKeyboardButton('💻Информация о нас',callback_data = 'infoonas'),

		],

	],
)




######################################################################################################
pas_menu = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton('☎️Biz bilan bog\'lanish'),
			KeyboardButton("✍️Ariza va Shikoyatlar"),

		],
		[
			KeyboardButton('⚙️Sozlamalar'),
			KeyboardButton('🎁Yangliklar'),

		],

	],
	resize_keyboard=True
)
###############rus
vniz_menu = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton('☎️связаться с нами'),
			KeyboardButton("✍️Заявления и жалобы"),

		],
		[
			KeyboardButton('⚙️Настройки'),
			KeyboardButton('🎁Новости'),

		],

	],
	resize_keyboard=True
)

###################################################################################


lan_nopka = ReplyKeyboardMarkup(
	keyboard = [
			[
			KeyboardButton("💻 IT Project Menejment "),
			KeyboardButton("✅ IT start"),
			],
			[
			KeyboardButton("📃 Savodxonlik"),
			KeyboardButton("🚀 Flatter"),
			],
			[
			KeyboardButton("🌐 Frontend Developer"),
			KeyboardButton("💠 Vuejes"),
			],
			[
			KeyboardButton("📂 PHP"),
			KeyboardButton("🖥 JAVA"),
			],
			[
			KeyboardButton("🎬 Cinema 4"),
			KeyboardButton("🧩 Unity"),
			],
			[
			KeyboardButton("📈 Unreal engine"),
			],
			[
			KeyboardButton("🔙orqaga"),
			],
		
		
	],
	resize_keyboard=True
) 
######################rus
lan00_nopka = ReplyKeyboardMarkup(
	keyboard = [
			[
			KeyboardButton("💻 IT Project Menejment "),
			KeyboardButton("✅ IT start"),
			],
			[
			KeyboardButton("📃 Грамотность"),
			KeyboardButton("🚀 Flatter"),
			],
			[
			KeyboardButton("🌐 Frontend Developer"),
			KeyboardButton("💠 Vuejes"),
			],
			[
			KeyboardButton("📂 PHP"),
			KeyboardButton("🖥 JAVA"),
			],
			[
			KeyboardButton("🎬 Cinema 4"),
			KeyboardButton("🧩 Unity"),
			],
			[
			KeyboardButton("📈 Unreal engine"),
			],
			[
			KeyboardButton("🔙назад"),
			],
		
		
	],
	resize_keyboard=True
) 


###################################################################################

lan1_nopka = InlineKeyboardMarkup(
	inline_keyboard = [
			[
			InlineKeyboardButton("💻 IT Project Menejment ",callback_data = "project"),
			InlineKeyboardButton("✅ IT start",callback_data = "start"),
			],
			[
			InlineKeyboardButton("📃 Savodxonlik",callback_data = "savod"),
			InlineKeyboardButton("🚀 Flatter",callback_data = "flatter"),
			],
			[
			InlineKeyboardButton("🌐 Frontend Developer",callback_data = "front"),
			InlineKeyboardButton("💠 Vuejes",callback_data = "vu"),
			],
			[
			InlineKeyboardButton("📂 PHP",callback_data = "php"),
			KeyboardButton("🖥 JAVA",callback_data = "java"),
			],
			[
			InlineKeyboardButton("🎬 Cinema 4",callback_data = "cinema"),
			InlineKeyboardButton("🧩 Unity",callback_data = "unity"),
			],
			[
			InlineKeyboardButton("📈 Unreal engine",callback_data = "unreal"),
			],
			
			[
			InlineKeyboardButton("🔙orqaga",callback_data = 'back1'),
			],
			
		
		
	],
	
) 
#############################################rus
lan100_nopka = InlineKeyboardMarkup(
	inline_keyboard = [
			[
			InlineKeyboardButton("💻 IT Project Menejment ",callback_data = "pro"),
			InlineKeyboardButton("✅ IT start",callback_data = "it"),
			],
			[
			InlineKeyboardButton("📃 Грамотность",callback_data = "gram"),
			InlineKeyboardButton("🚀 Flatter",callback_data = "flotter"),
			],
			[
			InlineKeyboardButton("🌐 Frontend Developer",callback_data = "dev"),
			InlineKeyboardButton("💠 Vuejes",callback_data = "vuej"),
			],
			[
			InlineKeyboardButton("📂 PHP",callback_data = "phpee"),
			KeyboardButton("🖥 JAVA",callback_data = "javaaa"),
			],
			[
			InlineKeyboardButton("🎬 Cinema 4",callback_data = "cinemaaa"),
			InlineKeyboardButton("🧩 Unity",callback_data = "unityaa"),
			],
			[
			InlineKeyboardButton("📈 Unreal engine",callback_data = "unrealaa"),
			],
			
			[
			InlineKeyboardButton("🔙назад",callback_data = "backkk"),
			],
			
		
		
	],
	
) 

########################################################################################################



con_nopka = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton('Telefon nomer☎️',request_contact = True),
		],
	],
	resize_keyboard=True
) 

#######################rus
con0_nopka = ReplyKeyboardMarkup(
	keyboard = [
		[
			KeyboardButton('Телефонный номер☎️',request_contact = True),
		],
	],
	resize_keyboard=True
) 


###############################################################
menu1 = InlineKeyboardMarkup(
		inline_keyboard =[
		[
			InlineKeyboardButton("📝O'quv kursga yozilish",callback_data = 'yoz'),
		],
		[
			InlineKeyboardButton("🔙orqaga",callback_data = 'back2'),
		],
	],
)

###############rus
menu100 = InlineKeyboardMarkup(
		inline_keyboard =[
		[
			InlineKeyboardButton("📝Запись на курс обучения",callback_data = 'zapis'),
		],
		[
			InlineKeyboardButton("🔙назад",callback_data = 'back200'),
		],
	],
)










locatsiya_nopka = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("🔙orqaga",callback_data = 'back9'),
		],

	],
)


locatsiya0_nopka = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("🔙назад",callback_data = 'back900'),
		],

	],
)

#####################################################################
op_nopka = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("🔙orqaga",callback_data = 'back112'),
		],

	],
	
	
)
op0_nopka = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("🔙назад",callback_data = 'back1121'),
		],

	],
	
	
)