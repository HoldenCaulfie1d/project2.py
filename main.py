from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import logging
import nltk
from nltk.corpus import stopwords
import re
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.metrics.pairwise import cosine_similarity
import pymorphy2


driver = webdriver.Chrome()
def get_new_buildings():
    '''Функция для получения информации с сайта'''
    driver.get('https://www.sberbank.ru/ru/person/credits/home/buying_project')
    sleep(7)
    try:
        global get_ipotec1
        head_element = driver.find_elements(By.TAG_NAME, 'h1')
        information_element = driver.find_elements(By.TAG_NAME, 'h3')
        head = head_element[1].text
        head_res = ''.join(head)
        information = information_element[0].text
        information_res = ''.join(information)
        get_ipotec1 = f'{head_res} - ставка\nПервый взнос - {information_res}'
        return get_ipotec1
                
    except:
            print('Элемент не найден') 
    finally:
            driver.close
            driver.quit


def get_housing():
    driver.get('https://www.sberbank.ru/ru/person/credits/home/buying_complete_house')
    sleep(7)
    try:
        global get_ipotec2
        head_element = driver.find_elements(By.TAG_NAME, 'h1')
        information_element = driver.find_elements(By.TAG_NAME, 'h3')
        head = head_element[1].text
        head_res = ''.join(head)
        information = information_element[0].text
        information_res = ''.join(information)
        get_ipotec2 = f'{head_res} - ставка\nПервый взнос - {information_res}'
        return get_ipotec2
               
    except:
            print('Элемент не найден') 
    finally:
            driver.close
            driver.quit


def get_tobuild_house():
    driver.get('https://www.sberbank.ru/ru/person/credits/home/building')
    sleep(7)
    try:
        global get_ipotec3
        head_element = driver.find_elements(By.TAG_NAME, 'h1')
        information_element = driver.find_elements(By.TAG_NAME, 'h3')
        head = head_element[1].text
        head_res = ''.join(head)
        information = information_element[0].text
        information_res = ''.join(information)
        get_ipotec3 = f'{head_res} - ставка\nПервый взнос - {information_res}'
        return get_ipotec3      
    except:
            print('Элемент не найден') 
    finally:
            driver.close
            driver.quit


def get_country_house():
    driver.get('https://www.sberbank.ru/ru/person/credits/home/buying_cottage')
    sleep(7)
    try:
        global get_ipotec4
        head_element = driver.find_elements(By.TAG_NAME, 'h1')
        information_element = driver.find_elements(By.TAG_NAME, 'h3')
        head = head_element[1].text
        head_res = ''.join(head)
        information = information_element[0].text
        information_res = ''.join(information)
        get_ipotec4 = f'{head_res} - ставка\nПервый взнос - {information_res}'
        return get_ipotec4
                
    except:
            print('Элемент не найден') 
    finally:
            driver.close
            driver.quit

get_tobuild_house()
get_new_buildings()
get_housing()
get_country_house()

TOKEN = '5300898477:AAHpsKRPrbRR5u2wHcSbm1X2NtQvKi6T6QI'

logging.basicConfig(level =logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def cmd_test1(message: types.Message):
    await message.answer("Доброго времени суток! \nВведите категорию ипотеки:")

@dp.message_handler()
async def data_get(message: types.Message):

    list_var1 = ['новостройка', 'новое']
    list_var2 = ['вторичка', 'вторичный']
    list_var3 = ['постройка', 'построить', 'стройку', 'строительство','дом']
    list_var4 = ['загородный', 'дача', 'земельный', 'земля']
    
    message.text = message.text.lower()
    message.text = re.sub(r'\[[0-9]*\]', ' ', message.text)
    message.text = re.sub(r'\s+', ' ', message.text)
    article_words = nltk.word_tokenize(message.text)
    #text_no_stopwords = [word for word in article_words if word not in stopwords.words('russian')]
    morph = pymorphy2.MorphAnalyzer()
    token_list = []
    for word in article_words:
        p = morph.parse(word)[0]
        token_list.append(p.normal_form)

    for token in token_list:
        if token in list_var1:
            await message.answer(get_ipotec1)
            break
        if token in list_var2:
            await message.answer(get_ipotec2)
            break
        if token in list_var3:
            await message.answer(get_ipotec3)
            break
        if token in list_var4:
            await message.answer(get_ipotec4)
            break
    if token not in list_var1 and token not in list_var2 and token not in list_var3 and token not in list_var4:
        await message.answer('извините, данная категория не найдена..')
        
            

def main():
    executor.start_polling(dp, skip_updates=True)


if __name__=='__main__':
    main()







