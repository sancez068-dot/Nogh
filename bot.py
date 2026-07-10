import telebot
from telebot import types
import sqlite3
import time
import random
import os
import sys

TOKEN = '8314523097:AAEk5Gah8rZmjeaEaPR50T6IWfs8glxNm1s'
bot = telebot.TeleBot(TOKEN)
BOT_USERNAME = "Панель СНГ (Выгодно)"

# АДМИНИСТРАТОРЫ ДЛЯ РАЗНЫХ КАТЕГОРИЙ ТОВАРОВ
ADMIN_LIKES_BOTS = "svat_iiiii"
ADMIN_PANELS_MODS = "merchantmodz"
ADMIN_ID = 7564448057  # Твой актуальный Telegram ID
ADMIN_ID_2 = 7558811554  # Второй администратор

PRODUCTS = {
    "likes_220": "❤️ Лайки 220шт. (25 RUB / 15🌟)",
    "likes_6600": "❤️ Лайки 6600шт. (350 RUB / 250🌟)",
    "likes_10000": "❤️ Лайки 10000шт. (500 RUB / 375🌟)",
    "likes_13200": "❤️ Лайки 13200шт. (575 RUB / 425🌟)",
    "likes_15000": "❤️ Лайки 15000шт. (700 RUB / 525🌟)",
    "likes_18000": "❤️ Лайки 18000шт. (800 RUB / 590🌟)",
    "likes_20000": "❤️ Лайки 20000шт. (900 RUB / 675🌟)",
    "likes_22000": "❤️ Лайки 22000шт. (999 RUB / 725🌟)",
    "bots_3": "🤖 Боты гильдии 3шт. (350 RUB / 5$)",
    "bots_6": "🤖 Боты гильдии 6шт. (650 RUB / 9$)",
    "bots_12": "🤖 Боты гильдии 12шт. (1100 RUB / 15$)",
    "drip_apk": "🧬 DRIP CLIENT - APK MOD",
    "drip_root": "⚡ DRIP CLIENT - КОРНЕВОЕ УСТРОЙСТВО",
    "drip_pc": "🎯 DRIP AIMKILL X86 PC",
    "pato_orange": "Команда Пато ApkMod Orange",
    "pato_blue": "Команда Пато ApkMod Blue",
    "hg_cheats_non_root": "HG CHEATS NON ROOT",
    "hg_cheats": "HG Cheats Apk+Root",
    "reaper_x_pro": "Reaper X pro",
    "spotify_root": "🎵 SPOTIFY FF ROOT",
    "strix_root": "СТРИКС БР РУТ",
    "hex_injector": "КОРЕНЬ ШЕСТИГРАННОЙ ФОРСУНКИ",
    "xreg_root": "Корневое устройство Xreg",
    "haxx_root": "HAXX CKER PRO - ROOT",
    "prime_mods": "Prime Mods Apkmod",
    "wing_root": "Корневой модуль крыла",
    "cert_ios": "Сертификат дизайна (iOS All)",
    "fluorite_ios": "Fluorite FF - iOS",
    "migul_ios": "Мигул FF iOS",
    "migul_pro": "Migul Pro FF iOS aimkill",
    "king_ios": "Король iOS",
    "vnhax_ios": "Vnhax Global [iOS]",
    "lk_pc": "Команда Lk Root+Pc",
    "br_root": "Br Mods Root",
    "br_pc": "Br Mods Pc",
    "br_bypass": "Br Mods PC+Bypass",
    "term_pc": "🎯 Терминал х ПК Aimkill",
    "term_cover": "🛡️ Terminal x PC Aimkill cover",
    "fluorite_mlbb": "💧 Флюорит MLBB IOS",
    "cloud_codm": "☁️ Cloud CODM IOS",
    "8ball_gbd": "🎱 8ball IOS GBD",
    "ezteam_8ball": "🎱 EzTeam 8boll pool Apk",
    "wizard_8bp": "🧙‍♂️ WizardiOS 8bp",
    "iosstar_8bp": "⭐ iOSSTAR 8bp",
    "pubg_zolo": "🗺️ PUBG Zolo Android",
    "alien_mlbb": "👾 Alien MLBB (Android)"
}

CONFIGS = {
    "conf_apple": (
        "🍏 <b>Превращаем твой iPhone в машину для хедшотов!</b>\n\n"
        "• Обзор: <code>198</code>\n"
        "• Коллиматор: <code>149</code>\n"
        "• 2X Прицел: <code>186</code>\n"
        "• 4X Прицел: <code>105</code>\n"
        "• Снайперский: <code>89</code>\n"
        "• Кнопка огня: <code>43%</code>\n"
        "• Ползунок 3D Touch: <i>Максимум (Быстро)</i>"
    ),
    "conf_xiaomi": (
        "🇨🇳 <b>Топовые настройки для Xiaomi / Redmi:</b>\n\n"
        "• Обзор: <code>189</code>\n"
        "• Коллиматор: <code>158</code>\n"
        "• 2X Прицел: <code>167</code>\n"
        "• 4X Прицел: <code>186</code>\n"
        "• Снайперский: <code>147</code>\n"
        "• Кнопка огня: <code>47%</code>\n"
        "• ⚙️ Рекомендуемый <b>DPI: 510</b>"
    ),
    "conf_poco": (
        "⚡ <b>Идеальная оттяжка под игровые девайсы POCO:</b>\n\n"
        "• Обзор: <code>178</code>\n"
        "• Коллиматор: <code>159</code>\n"
        "• 2X Прицел: <code>200</code>\n"
        "• 4X Прицел: <code>188</code>\n"
        "• Снайперский: <code>128</code>\n"
        "• Кнопка огня: <code>41%</code>\n"
        "• ⚙️ Рекомендуемый <b>DPI: 560</b> (Для плавного залета)"
    ),
    "conf_samsung": (
        "📱 <b>Пресет чувствительности для Samsung:</b>\n\n"
        "• Обзор: <code>194</code>\n"
        "• Коллиматор: <code>184</code>\n"
        "• 2X Прицел: <code>159</code>\n"
        "• 4X Прицел: <code>177</code>\n"
        "• Снайперский: <code>140</code>\n"
        "• Кнопка огня: <code>52%</code>\n"
        "• ⚙️ Рекомендуемый <b>DPI: 480</b>"
    ),
    "conf_realme": (
        "🦊 <b>Настройки оттяжки для Realme / Oppo:</b>\n\n"
        "• Обзор: <code>199</code>\n"
        "• Коллиматор: <code>177</code>\n"
        "• 2X Прицел: <code>193</code>\n"
        "• 4X Прицел: <code>163</code>\n"
        "• Снайперский: <code>122</code>\n"
        "• Кнопка огня: <code>45%</code>\n"
        "• ⚙️ Рекомендуемый <b>DPI: 520</b>"
    )
}

# === БАЗА ДАННЫХ ===
def init_db():
    conn = sqlite3.connect('users.db', timeout=20)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            balance INTEGER DEFAULT 0,
            referrer_id INTEGER DEFAULT 0,
            ref_count INTEGER DEFAULT 0,
            last_casino_time INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_user(user_id, referrer_id=0):
    conn = sqlite3.connect('users.db', timeout=20)
    cursor = conn.cursor()
    cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
    if cursor.fetchone() is None:
        bonus = 100
        if referrer_id != 0:
            cursor.execute('SELECT ref_count FROM users WHERE user_id = ?', (referrer_id,))
            ref_data = cursor.fetchone()
            if ref_data:
                current_refs = ref_data[0]
                if current_refs >= 15: 
                    bonus = 150
                elif current_refs >= 5: 
                    bonus = 120

        cursor.execute('INSERT INTO users (user_id, referrer_id) VALUES (?, ?)', (user_id, referrer_id))
        if referrer_id != 0:
            cursor.execute('UPDATE users SET balance = balance + ?, ref_count = ref_count + 1 WHERE user_id = ?', (bonus, referrer_id))
    conn.commit()
    conn.close()

def get_user_data(user_id):
    conn = sqlite3.connect('users.db', timeout=20)
    cursor = conn.cursor()
    cursor.execute('SELECT balance, ref_count, last_casino_time FROM users WHERE user_id = ?', (user_id,))
    data = cursor.fetchone()
    conn.close()
    return data if data else (0, 0, 0)

def update_balance(user_id, amount):
    conn = sqlite3.connect('users.db', timeout=20)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET balance = balance - ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()

def update_casino_time(user_id, current_time, prize):
    conn = sqlite3.connect('users.db', timeout=20)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET last_casino_time = ?, balance = balance + ? WHERE user_id = ?', (current_time, prize, user_id))
    conn.commit()
    conn.close()

def get_top_referrers():
    conn = sqlite3.connect('users.db', timeout=20)
    cursor = conn.cursor()
    cursor.execute('SELECT user_id, ref_count FROM users ORDER BY ref_count DESC LIMIT 10')
    top = cursor.fetchall()
    conn.close()
    return top

def get_user_status(ref_count):
    if ref_count >= 15: 
        return "👑 Магистр Накрутки (+15 RUB за друга)", 15
    elif ref_count >= 5: 
        return "⚡ Продвинутый Рефовод (+12 RUB за друга)", 12
    else: 
        return "🌱 Новичок (+10 RUB за друга)", 10

# === МЕНЮШКИ ===
def get_main_menu(user_id):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("❤️ Лайки и Боты", callback_data="services")
    btn2 = types.InlineKeyboardButton("🖥️ Панели и Моды", callback_data="panels_menu")
    btn3 = types.InlineKeyboardButton("⚙️ Личный Кабинет", callback_data="cabinet")
    btn4 = types.InlineKeyboardButton("🎰 Халявное Казино", callback_data="casino_menu")
    btn5 = types.InlineKeyboardButton("⚡ Настройки Оттяжки", callback_data="aim_configs")
    btn6 = types.InlineKeyboardButton("🏆 ТОП Лидеров", callback_data="top_menu")
    btn7 = types.InlineKeyboardButton("🔥 Отзывы Like", url="https://t.me/otziv_freefiree")
    btn8 = types.InlineKeyboardButton("🔥 Отзывы panel", url="https://t.me/Sucks11")
    btn9 = types.InlineKeyboardButton("👑 Связь с Админом", callback_data="contact")
    btn10 = types.InlineKeyboardButton("Купить звёзды", url="https://t.me/by_stars_tg_bot?start=_tgr_R2gvsoYwOTQ6")
    btn11 = types.InlineKeyboardButton("Накрутка подписчиков", url="https://t.me/SefferiesHakrytka_bot?start=7564448057")
    btn12 = types.InlineKeyboardButton("Дешёвые Алмазы FF", url="https://donatov.net/inv/298492")
    btn13 = types.InlineKeyboardButton("Канал з панелями", url="https://t.me/merchantmodz1")
    btn14 = types.InlineKeyboardButton("Канал з лайками", url="https://t.me/freefire_like_office")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14)
    
    if user_id == ADMIN_ID or user_id == ADMIN_ID_2:
        markup.add(types.InlineKeyboardButton("🛠 Админ-панель", callback_data="admin_panel"))
        markup.add(types.InlineKeyboardButton("🛑 УНИЧТОЖИТЬ БОТА (АДМ)", callback_data="confirm_self_destruct"))
    return markup

def get_back_menu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 Назад в меню", callback_data="main_menu"))
    return markup

def get_cabinet_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("💸 Вывести деньги", callback_data="withdraw_methods"),
        types.InlineKeyboardButton("🔙 Назад в меню", callback_data="main_menu")
    )
    return markup

def get_admin_markup():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("📢 Рассылка", callback_data="admin_broadcast"),
        types.InlineKeyboardButton("💰 Наценки", callback_data="admin_markup"),
        types.InlineKeyboardButton("📊 Статистика", callback_data="admin_stats")
    )
    markup.add(types.InlineKeyboardButton("🔙 В главное меню", callback_data="main_menu"))
    return markup

def get_withdraw_methods_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("📲 Вывод по СБП (на карту)", callback_data="w_method_sbp"),
        types.InlineKeyboardButton("⭐ Вывод Звёздами Telegram", callback_data="w_method_stars"),
        types.InlineKeyboardButton("🔙 Назад в личный кабинет", callback_data="cabinet")
    )
    return markup

def get_likes_bots_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("❤️ Лайки 220шт. — 🟢ДОСТУПНО🟢", callback_data="buy_id_likes_220"),
        types.InlineKeyboardButton("❤️ Лайки 6600шт. — 🟢ДОСТУПНО🟢", callback_data="buy_id_likes_6600"),
        types.InlineKeyboardButton("❤️ Лайки 10000шт. — 🟢ДОСТУПНО🟢", callback_data="buy_id_likes_10000"),
        types.InlineKeyboardButton("❤️ Лайки 13200шт. — 🟢ДОСТУПНО🟢", callback_data="buy_id_likes_13200"),
        types.InlineKeyboardButton("❤️ Лайки 15000шт. — 🟢ДОСТУПНО🟢", callback_data="buy_id_likes_15000"),
        types.InlineKeyboardButton("❤️ Лайки 18000шт. — 🟢ДОСТУПНО🟢", callback_data="buy_id_likes_18000"),
        types.InlineKeyboardButton("❤️ Лайки 20000шт. — 🟢ДОСТУПНО🟢", callback_data="buy_id_likes_20000"),
        types.InlineKeyboardButton("❤️ Лайки 22000шт. — 🟢ДОСТУПНО🟢", callback_data="buy_id_likes_22000"),
        types.InlineKeyboardButton("🤖 Боты гильдии 3шт. — 🔴НЕ ДОСТУПНО🔴", callback_data="buy_id_bots_3"),
        types.InlineKeyboardButton("🤖 Боты гильдии 6шт. — 🔴НЕ ДОСТУПНО🔴", callback_data="buy_id_bots_6"),
        types.InlineKeyboardButton("🤖 Боты гильдии 12шт. — 🔴НЕ ДОСТУПНО🔴", callback_data="buy_id_bots_12"),
        types.InlineKeyboardButton("🔙 Назад в главное меню", callback_data="main_menu")
    )
    return markup

def get_panels_categories():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("🔥 DRIP CLIENT & Популярное", callback_data="p_cat_drip")
    btn2 = types.InlineKeyboardButton("🤖 Моды и Читы Android (Apk/Root)", callback_data="p_cat_android")
    btn3 = types.InlineKeyboardButton("🍏 Читы и Софт для iOS", callback_data="p_cat_ios")
    btn4 = types.InlineKeyboardButton("💻 Софт для ПК (PC / Bypass)", callback_data="p_cat_pc")
    btn5 = types.InlineKeyboardButton("🎮 Другие Игры (8ball, PUBG, MLBB, CODM)", callback_data="p_cat_others")
    btn_back = types.InlineKeyboardButton("🔙 Назад в главное меню", callback_data="main_menu")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn_back)
    return markup

def get_products_inline_menu(id_list, back_callback):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for prod_id in id_list:
        name = PRODUCTS.get(prod_id, prod_id)
        markup.add(types.InlineKeyboardButton(name, callback_data=f"buy_id_{prod_id}"))
    markup.add(types.InlineKeyboardButton("🔙 Назад к категориям", callback_data=back_callback))
    return markup

def get_brands_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🍏 iPhone (iOS)", callback_data="show_conf_apple"),
        types.InlineKeyboardButton("🇨🇳 Xiaomi / Redmi", callback_data="show_conf_xiaomi"),
        types.InlineKeyboardButton("⚡ POCO", callback_data="show_conf_poco"),
        types.InlineKeyboardButton("📱 Samsung", callback_data="show_conf_samsung"),
        types.InlineKeyboardButton("🦊 Realme / Oppo", callback_data="show_conf_realme"),
        types.InlineKeyboardButton("🔙 Назад в меню", callback_data="main_menu")
    )
    return markup

# === КОМАНДЫ ===
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    args = message.text.split()
    referrer_id = 0
    if len(args) > 1 and args[1].isdigit() and int(args[1]) != user_id:
        referrer_id = int(args[1])
    
    add_user(user_id, referrer_id)
    
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "🔥 Добро пожаловать в автоматизированный бот-магазин по накрутке Free Fire!\n"
        "⚡ Здесь ты можешь прокачать свой аккаунт или приобрести топовые софты/панели.\n\n"
        "👇 Выбери интересующий раздел в меню ниже:",
        reply_markup=get_main_menu(user_id)
    )

# === ОБРАБОТКА КНОПОК ===
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    user_id = call.from_user.id
    
    # === ЛОГИКА АДМИН-ПАНЕЛИ ===
    if call.data == "admin_panel" and (user_id == ADMIN_ID or user_id == ADMIN_ID_2):
        bot.edit_message_text("🛠 <b>Админ-панель</b>\nВыберите действие:",
                              call.message.chat.id, call.message.message_id,
                              reply_markup=get_admin_markup(), parse_mode="HTML")
    
    elif call.data == "admin_stats" and (user_id == ADMIN_ID or user_id == ADMIN_ID_2):
        conn = sqlite3.connect('users.db')
        count = conn.cursor().execute('SELECT count(*) FROM users').fetchone()[0]
        conn.close()
        bot.answer_callback_query(call.id, f"👥 Всего пользователей: {count}", show_alert=True)
    
    elif call.data == "admin_broadcast" and (user_id == ADMIN_ID or user_id == ADMIN_ID_2):
        msg = bot.send_message(call.message.chat.id, "Введите текст рассылки:")
        bot.register_next_step_handler(msg, broadcast_message)
    
    elif call.data == "admin_markup" and (user_id == ADMIN_ID or user_id == ADMIN_ID_2):
        text = (
            "💰 <b>Раздел: Изменение цен</b>\n\n"
            "Пришли сообщение в формате:\n"
            "<code>ID_товара Цена_RUB Цена_USD Звезды</code>\n\n"
            "Пример:\n<code>likes_220 30 0.5 20</code>"
        )
        msg = bot.send_message(call.message.chat.id, text, parse_mode="HTML")
        bot.register_next_step_handler(msg, update_product_price)
    
    if call.data == "services":
        text = "<b>Выбери интересующую услугу накрутки лайков или ботов:</b>"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_likes_bots_menu(), parse_mode="HTML")
    
    elif call.data == "panels_menu":
        text = "<b>Выбери категорию интересующих панелей и приватных софтов:</b>"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_panels_categories(), parse_mode="HTML")
    
    elif call.data == "p_cat_drip":
        ids = ["drip_apk", "drip_root", "drip_pc"]
        bot.edit_message_text("🔥 <b>Линейка DRIP CLIENT и эксклюзивы:</b>", call.message.chat.id, call.message.message_id, reply_markup=get_products_inline_menu(ids, "panels_menu"), parse_mode="HTML")
    
    elif call.data == "p_cat_android":
        ids = ["pato_orange", "pato_blue", "hg_cheats_non_root", "hg_cheats", "reaper_x_pro", "strix_root", "hex_injector", "xreg_root", "haxx_root", "prime_mods", "wing_root"]
        bot.edit_message_text("🤖 <b>Читы и Моды на Android (Root / APK):</b>", call.message.chat.id, call.message.message_id, reply_markup=get_products_inline_menu(ids, "panels_menu"), parse_mode="HTML")
    
    elif call.data == "p_cat_ios":
        ids = ["cert_ios", "fluorite_ios", "migul_ios", "migul_pro", "king_ios", "vnhax_ios"]
        bot.edit_message_text("🍏 <b>Софты и настройки для iOS:</b>", call.message.chat.id, call.message.message_id, reply_markup=get_products_inline_menu(ids, "panels_menu"), parse_mode="HTML")
    
    elif call.data == "p_cat_pc":
        ids = ["lk_pc", "br_root", "br_pc", "br_bypass", "term_pc", "term_cover"]
        bot.edit_message_text("💻 <b>Приватный софт на ПК (PC / Эмуляторы):</b>", call.message.chat.id, call.message.message_id, reply_markup=get_products_inline_menu(ids, "panels_menu"), parse_mode="HTML")
    
    elif call.data == "p_cat_others":
        ids = ["fluorite_mlbb", "cloud_codm", "8ball_gbd", "ezteam_8ball", "wizard_8bp", "iosstar_8bp", "pubg_zolo", "alien_mlbb"]
        bot.edit_message_text("🎮 <b>Читы и панели для других мобильных игр:</b>", call.message.chat.id, call.message.message_id, reply_markup=get_products_inline_menu(ids, "panels_menu"), parse_mode="HTML")
    
    elif call.data == "aim_configs":
        text = (
            "⚡ <b>БАЗА БЕСПЛАТНЫХ НАСТРОЕК И ОТТЯЖЕК</b> ⚡\n\n"
            "Выбери бренд своего мобильного устройства из списка ниже, чтобы получить идеальные параметры чувствительности экрана и DPI для стрельбы:"
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_brands_menu(), parse_mode="HTML")
    
    elif call.data.startswith("show_conf_"):
        brand_id = call.data.replace("show_conf_", "conf_")
        config_text = CONFIGS.get(brand_id, "⚠️ Настройки для этого бренда обновляются. Зайдите позже!")
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 Назад к выбору брендов", callback_data="aim_configs"))
        bot.edit_message_text(config_text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="HTML")
    
    elif call.data.startswith("buy_id_"):
        prod_id = call.data.replace("buy_id_", "")
        product_name = PRODUCTS.get(prod_id, "Неизвестный товар")
        markup = types.InlineKeyboardMarkup(row_width=1)
        
        if "likes_" in prod_id or "bots_" in prod_id: 
            current_admin = ADMIN_LIKES_BOTS
        else: 
            current_admin = ADMIN_PANELS_MODS
        
        admin_chat_url = f"https://t.me/{current_admin}"
        
        # === НАСТРОЙКА ЦЕН ===
        if prod_id == "drip_apk":
            text = (
                "<b>🧬 DRIP CLIENT - APK MOD</b>\n\n"
                "📊 Доступные тарифы подписки:\n"
                "• 1 день — <b>100₽ / 1.5$</b>\n"
                "• 3 дня — <b>200₽ / 3$</b>\n"
                "• 7 дней — <b>300₽ / 4$</b>\n"
                "• 15 дней — <b>500₽ / 7$</b>\n"
                "• 30 дней — <b>650₽ / 9$</b>\n\n"
                f"✨ Для покупки софта переходи по кнопке в чат к менеджеру @{current_admin}."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        elif prod_id == "pato_orange":
            text = (
                "<b>Команда Пато ApkMod Orange</b>\n\n"
                "📊 Доступные тарифы подписки:\n"
                "• 3 дня — <b>345₽ / 5$</b>\n"
                "• 7 дней — <b>510₽ / 7$</b>\n"
                "• 15 дней — <b>777₽ / 11$</b>\n\n"
                f"✨ Для покупки софта переходи по кнопке в чат к менеджеру @{current_admin}."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        elif prod_id == "pato_blue":
            text = (
                "<b>Команда Пато ApkMod Blue</b>\n\n"
                "📊 Доступные тарифы подписки:\n"
                "• 3 дня — <b>280₽ / 4$</b>\n"
                "• 7 дней — <b>450₽ / 6$</b>\n"
                "• 15 дней — <b>650₽ / 9$</b>\n\n"
                f"✨ Для покупки софта переходи по кнопке в чат к менеджеру @{current_admin}."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        elif prod_id == "hg_cheats_non_root":
            text = (
                "<b>HG CHEATS NON ROOT</b>\n\n"
                "📊 Доступные тарифы подписки:\n"
                "• 10 дней — <b>500₽ / 7$</b>\n"
                "• 30 дней — <b>1100₽ / 15$</b>\n\n"
                f"✨ Для покупки софта переходи по кнопке в чат к менеджеру @{current_admin}."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        elif prod_id == "hg_cheats":
            text = (
                "<b>HG Cheats Apk+Root</b>\n\n"
                "📊 Доступные тарифы подписки:\n"
                "• 1 день — <b>140₽ / 2$</b>\n"
                "• 7 дней — <b>310₽ / 4.5$</b>\n"
                "• 10 дней — <b>370₽ / 5$</b>\n"
                "• 30 дней — <b>699₽ / 10$</b>\n\n"
                f"✨ Для покупки софта переходи по кнопке в чат к менеджеру @{current_admin}."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        elif prod_id == "reaper_x_pro":
            text = (
                "<b>Reaper X pro</b>\n\n"
                "📊 Доступные тарифы подписки:\n"
                "• 10 дней — <b>500₽ / 7$</b>\n"
                "• 30 дней — <b>1000₽ / 14$</b>\n\n"
                f"✨ Для покупки софта переходи по кнопке в чат к менеджеру @{current_admin}."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        elif prod_id == "strix_root":
            text = (
                "<b>СТРИКС БР РУТ</b>\n\n"
                "📊 Доступные тарифы подписки:\n"
                "• 1 день — <b>50₽ / 1$</b>\n"
                "• 5 дней — <b>100₽ / 1.5$</b>\n"
                "• 7 дней — <b>150₽ / 2$</b>\n"
                "• 15 дней — <b>400₽ / 5.5$</b>\n"
                "• 30 дней — <b>700₽ / 9.5$</b>\n\n"
                f"✨ Для покупки софта переходи по кнопке в чат к менеджеру @{current_admin}."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        elif prod_id == "cert_ios":
            text = (
                "<b>Сертификат дизайна (iOS All)</b>\n\n"
                "📊 Доступные тарифы подписки:\n"
                "• На год с гарантией 30 дней — <b>600₽ / 8$</b>\n"
                "• На год с гарантией 60 дней — <b>800₽ / 11$</b>\n"
                "• На год с гарантией 180 дней — <b>1400₽ / 19$</b>\n\n"
                f"✨ Для покупки софта переходи по кнопке в чат к менеджеру @{current_admin}."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        elif prod_id == "fluorite_ios":
            text = (
                "<b>Fluorite FF - iOS</b>\n\n"
                "📊 Доступные тарифы подписки:\n"
                "• 1 день — <b>400₽ / 5.5$</b>\n"
                "• 7 дней — <b>1200₽ / 16$</b>\n"
                "• 30 дней — <b>2150₽ / 29$</b>\n\n"
                f"✨ Для покупки софта переходи по кнопке в чат к менеджеру @{current_admin}."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        elif prod_id == "lk_pc":
            text = (
                "<b>Команда Lk Root+Pc</b>\n\n"
                "📊 Доступные тарифы подписки:\n"
                "• 1 день — <b>80₽ / 1.5$</b>\n"
                "• 5 дней — <b>150₽ / 2$</b>\n"
                "• 10 дней — <b>300₽ / 4$</b>\n"
                "• 30 дней — <b>550₽ / 7.5$</b>\n\n"
                f"✨ Для покупки софта переходи по кнопке в чат к менеджеру @{current_admin}."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        elif prod_id == "br_root":
            text = (
                "<b>Br Mods Root</b>\n\n"
                "📊 Доступные тарифы подписки:\n"
                "• 1 день — <b>150₽ / 2$</b>\n"
                "• 7 дней — <b>500₽ / 7$</b>\n"
                "• 30 дней — <b>1000₽ / 14$</b>\n\n"
                f"✨ Для покупки софта переходи по кнопке в чат к менеджеру @{current_admin}."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        elif prod_id == "br_pc":
            text = (
                "<b>Br Mods Pc</b>\n\n"
                "📊 Доступные тарифы подписки:\n"
                "• 1 день — <b>150₽ / 2$</b>\n"
                "• 7 дней — <b>500₽ / 7$</b>\n"
                "• 30 дней — <b>900₽ / 12$</b>\n\n"
                f"✨ Для покупки софта переходи по кнопке в чат к менеджеру @{current_admin}."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        elif prod_id == "br_bypass":
            text = (
                "<b>Br Mods PC+Bypass</b>\n\n"
                "📊 Доступные тарифы подписки:\n"
                "• 1 день — <b>200₽ / 3$</b>\n"
                "• 10 дней — <b>800₽ / 11$</b>\n"
                "• 30 дней — <b>1300₽ / 17.5$</b>\n\n"
                f"✨ Для покупки софта переходи по кнопке в чат к менеджеру @{current_admin}."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        elif prod_id == "prime_mods":
            text = (
                "<b>Prime Mods Apkmod</b>\n\n"
                "📊 Доступные тарифы подписки:\n"
                "• 1 день — <b>111₽ / 1.5$</b>\n"
                "• 3 дня — <b>222₽ / 3$</b>\n"
                "• 7 дней — <b>333₽ / 4.5$</b>\n\n"
                f"✨ Для покупки софта переходи по кнопке в чат к менеджеру @{current_admin}."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        elif prod_id in ["likes_220", "likes_6600", "likes_13200", "likes_15000", "likes_18000", "likes_20000", "likes_22000", "bots_3", "bots_6", "bots_12"]:
            text = (
                f"📦 <b>Оформление заказа</b>\n\n"
                f"🛒 Товар: <code>{product_name}</code>\n\n"
                f"✨ Нажми на кнопку ниже, чтобы написать менеджеру @{current_admin} и оформить заказ."
            )
            markup.add(types.InlineKeyboardButton("📥 Купить (Написать менеджеру)", url=admin_chat_url))
        
        else:
            # === ТОВАРА НЕТ В НАЛИЧИИ (ОСТАЛЬНЫЕ ПОЗИЦИИ) ===
            text = (
                f"📦 <b>Информация о товаре</b>\n\n"
                f"🛒 Товар: <code>{product_name}</code>\n\n"
                f"❌ <b>Нету в наличии. Напишите продавцу!</b>\n"
                f"🗣️ Чтобы узнать подробности, забронировать или сделать предзаказ — перейдите к менеджеру по кнопке ниже:"
            )
            markup.add(types.InlineKeyboardButton("📥 Написать продавцу", url=admin_chat_url))
        
        markup.add(types.InlineKeyboardButton("🔙 Вернуться в главное меню", callback_data="main_menu"))
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="HTML")
    
    elif call.data == "cabinet":
        balance, ref_count, _ = get_user_data(user_id)
        status_text, current_payout = get_user_status(ref_count)
        ref_link = f"https://t.me/panelVM_bot?start={user_id}"
        
        text = (
            "⚙️ <b>Мой профиль и статистика:</b>\n\n"
            f"👤 Имя: {call.from_user.first_name}\n"
            f"🆔 Твой ID: <code>{user_id}</code>\n"
            f"💎 Баланс: <b>{balance} RUB / {round(balance/75, 2)}$</b>\n"
            f"🎖️ Твой ранг: <b>{status_text}</b>\n\n"
            "🎁 <b>Зарабатывай на рефералах:</b>\n"
            "🔗 Твоя личная ссылка:\n"
            f"{ref_link}\n\n"
            "📈 <b>Квесты активности:</b>\n"
            "• Пригласи 5 друзей -> Бонус за каждого станет <b>12 RUB</b>\n"
            "• Пригласи 15 друзей -> Бонус за каждого станет <b>15 RUB</b>\n\n"
            "💬 Копируй ссылку и бросай друзьям, руби легкий кеш на игры!"
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_cabinet_menu(), parse_mode="HTML")
    
    elif call.data == "casino_menu":
        balance, ref_count, last_time = get_user_data(user_id)
        now = int(time.time())
        cooldown = 24 * 60 * 60
        markup = types.InlineKeyboardMarkup(row_width=1)
        
        if now - last_time < cooldown:
            time_left = cooldown - (now - last_time)
            hours = time_left // 3600
            minutes = (time_left % 3600) // 60
            text = (
                "🎰 <b>ЕЖЕДНЕВНОЕ КАЗИНО И ХАЛЯВА</b> 🎰\n\n"
                "❌ Ты уже забирал свой бонус сегодня!\n"
                f"⏳ Следующий прокрут кейса будет доступен через: <b>{hours}ч. {minutes}м.</b>\n\n"
                "Приходи завтра и испытай свою удачу снова!"
            )
        else:
            text = (
                "🎰 <b>ЕЖЕДНЕВНОЕ КАЗИНО И ХАЛЯВА</b> 🎰\n\n"
                "🎁 У тебя есть <b>1 бесплатная попытка</b> открыть секретный кейс!\n"
                "💰 Внутри спрятаны денежные призы: <b>от 5 до 100 RUB!</b>\n\n"
                "💵 Испытай свою фортуну прямо сейчас, нажав кнопку ниже:"
            )
            markup.add(types.InlineKeyboardButton("🎰 Открыть Бесплатный Кейс", callback_data="spin_casino"))
        
        markup.add(types.InlineKeyboardButton("🔙 В главное меню", callback_data="main_menu"))
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="HTML")
    
    elif call.data == "spin_casino":
        balance, ref_count, last_time = get_user_data(user_id)
        now = int(time.time())
        if now - last_time < 24 * 60 * 60:
            bot.answer_callback_query(call.id, "⏳ Рано! Кейс еще перезаряжается.", show_alert=True)
            return
        
        bot.edit_message_text("🎰 <i>Крутим барабан... Мутим кеш... 🎲</i>", call.message.chat.id, call.message.message_id, parse_mode="HTML")
        time.sleep(1.2)
        
        prizes = [5, 11, 22, 33, 44, 55, 66]
        weights = [45, 25, 15, 8, 4, 2, 1]
        prize = random.choices(prizes, weights=weights)[0]
        
        update_casino_time(user_id, now, prize)
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 Забрать приз и выйти", callback_data="main_menu"))
        
        text = (
            "🎉<b>ПОЗДРАВЛЯЕМ! КЕЙС ОТКРЫТ!</b> 🎉\n\n"
            f"🎰 Твой выигрыш составил: <b>+{prize} RUB / {round(prize/75, 2)}$</b> на игровой баланс!\n"
            "Деньги уже зачислены.\n\n"
            "🍀 Возвращайся ровно через 24 часа 59 минут 59 секунд за новой дозой халявы!"
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="HTML")
    
    elif call.data == "top_menu":
        top_users = get_top_referrers()
        text = "🏆 <b>ТОП-10 КОРОЛЕЙ РЕФЕРАЛОВ БОТА</b> 🏆\n────────────────────\n"
        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        for index, row in enumerate(top_users):
            u_id, r_count = row
            medal = medals[index] if index < len(medals) else "👤"
            text += f"{medal} Наш партнер — Игрок <code>{str(u_id)[:5]}***</code> (привел {r_count} друзей)\n"
        text += "────────────────────\n🚀 Приглашай друзей по своей ссылке и взлетай в топ!"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_back_menu(), parse_mode="HTML")
    
    elif call.data == "withdraw_methods":
        balance, _, _ = get_user_data(user_id)
        if balance < 555:
            bot.answer_callback_query(call.id, "❌ Минимальная сумма вывода — 555 RUB.", show_alert=True)
            return
        text = "💸 <b>Выбери удобный способ для вывода средств:</b>"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_withdraw_methods_menu(), parse_mode="HTML")
    
    elif call.data == "w_method_sbp":
        msg = bot.send_message(call.message.chat.id, "📲 <b>Вывод по СБП</b>\n\nВведите номер телефона и название банка:", parse_mode="HTML")
        bot.register_next_step_handler(msg, process_withdraw_requisites, "СБП (Карта)")
    
    elif call.data == "w_method_stars":
        msg = bot.send_message(call.message.chat.id, "⭐ <b>Вывод Звёздами Telegram</b>\n\nВведите ваш @username или ID Telegram:", parse_mode="HTML")
        bot.register_next_step_handler(msg, process_withdraw_requisites, "Telegram Stars")
    
    elif call.data == "contact":
        text = (
            "👑 <b>Связь с создателями:</b>\n\n"
            f"❤️ Накрутка лайков и ботов:\n👉 @{ADMIN_LIKES_BOTS}\n\n"
            f"🖥️ Читы, панели и моды:\n👉 @{ADMIN_PANELS_MODS}\n\n"
            "⚡ Пишите сразу по делу!"
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_back_menu(), parse_mode="HTML")
    
    elif call.data == "main_menu":
        text = "👇 Выбери нужный раздел меню:"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=get_main_menu(user_id), parse_mode="HTML")
    
    elif call.data == "confirm_self_destruct":
        if user_id != ADMIN_ID and user_id != ADMIN_ID_2:
            return
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("💥 ДА, УДАЛИТЬ ВСЁ НАХУЙ", callback_data="execute_self_destruct"))
        markup.add(types.InlineKeyboardButton("❌ ОТМЕНА", callback_data="main_menu"))
        bot.edit_message_text("⚠️ <b>ВНИМАНИЕ!</b> Ты собираешься удалить файлы скрипта и базу данных. Выполнить?", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="HTML")
    
    elif call.data == "execute_self_destruct":
        if user_id != ADMIN_ID and user_id != ADMIN_ID_2:
            return
        bot.edit_message_text("🚀 <b>Запуск протокола самоликвидации...</b> Файлы уничтожены.", call.message.chat.id, call.message.message_id, parse_mode="HTML")
        bot.stop_polling()
        if os.path.exists("bot.py"): os.remove("bot.py")
        if os.path.exists("users.db"): os.remove("users.db")
        sys.exit()

# === ЛОГИКА ВЫВОДА СРЕДСТВ ===
def process_withdraw_requisites(message, method):
    requisites = message.text
    user_id = message.from_user.id
    balance, _, _ = get_user_data(user_id)
    msg = bot.send_message(message.chat.id, f"💰 Твой текущий баланс: {balance} RUB\n\nВведите сумму вывода:")
    bot.register_next_step_handler(msg, process_withdraw_amount, method, requisites)

def process_withdraw_amount(message, method, requisites):
    user_id = message.from_user.id
    balance, _, _ = get_user_data(user_id)
    amount_str = message.text
    if not amount_str.isdigit():
        bot.send_message(message.chat.id, "❌ Ошибка! Сумма должна состоять из цифр.")
        return
    amount = int(amount_str)
    if amount < 555 or amount > balance:
        bot.send_message(message.chat.id, "❌ Неправильно написал или ты бомжара.")
        return
    
    update_balance(user_id, amount)
    admin_text = f"🚨 <b>ВЫВОД СРЕДСТВ</b> 🚨\n\n👤 ID: <code>{user_id}</code>\n📊 Способ: <code>{method}</code>\n💳 Реквизиты: <code>{requisites}</code>\n💰 Сумма: <b>{amount} RUB</b>"
    if ADMIN_ID != 0:
        try: bot.send_message(ADMIN_ID, admin_text, parse_mode="HTML")
        except: pass
    try: bot.send_message(ADMIN_ID_2, admin_text, parse_mode="HTML")
    except: pass
    print(f"Заявка на вывод: {admin_text}")
    bot.send_message(message.chat.id, f"✅ <b>Заявка создана!</b>\nСписано: <b>{amount} RUB / {round(amount/75, 2)}$</b>\nОжидайте обработки администратором.", parse_mode="HTML")

# === ФУНКЦИЯ РАССЫЛКИ ===
def broadcast_message(message):
    text = message.text
    conn = sqlite3.connect('users.db')
    users = conn.cursor().execute('SELECT user_id FROM users').fetchall()
    conn.close()
    
    count = 0
    for user in users:
        try:
            bot.send_message(user[0], text)
            count += 1
        except:
            pass
    bot.send_message(message.chat.id, f"✅ Рассылка завершена. Сообщение получили {count} пользователей.")

def update_product_price(message):
    try:
        data = message.text.split()
        if len(data) != 4:
            bot.send_message(message.chat.id, "❌ Ошибка! Формат: <code>ID_товара Рубли Доллары Звезды</code>\nПример: <code>likes_220 30 0.5 20</code>", parse_mode="HTML")
            return
        
        prod_id, rub, usd, stars = data[0], data[1], data[2], data[3]
        
        if prod_id in PRODUCTS:
            PRODUCTS[prod_id] = f"❤️ {prod_id.replace('_', ' ').title()} — {rub} RUB / {usd}$ / {stars}🌟"
            bot.send_message(message.chat.id, f"✅ Товар {prod_id} обновлен:\n{rub} RUB | {usd}$ | {stars} 🌟")
        else:
            bot.send_message(message.chat.id, "❌ ID товара не найден!")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Ошибка: {e}")

if __name__ == '__main__':
    init_db()
    try:
        bot.remove_webhook()
    except:
        pass
    
    print("🤖 Бот запущен и ждет команд...")
    
    # Плавный запуск с увеличенной паузой при ошибке
    while True:
        try:
            bot.infinity_polling(skip_pending=True)
        except Exception as e:
            print(f"⚠️ Ошибка соединения: {e}. Жду 10 секунд и пробую снова...")
            time.sleep(10)
