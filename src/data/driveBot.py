import telebot
import gspread
import os
import json
import pandas as pd

CHAVE_API = "5668253553:AAFk8c8x9KjxrCJTBX_x-JM9jK_gjWe3_MM"

bot = telebot.TeleBot(CHAVE_API)


class driveBot:
    def __init__(self):
        self.gc = gspread.service_account(filename = "credenciais.json")
    
    def get_data(self):
        link_google_sheet = os.getenv("LINK_SHEET")
        sh = self.gc.open_by_key(link_google_sheet)
        worksheet = sh.sheet1
        dataframe = pd.DataFrame(worksheet.get_all_records())
        return dataframe