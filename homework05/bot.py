import requests
import config
import telebot
from bs4 import BeautifulSoup
from time import time, localtime, strftime
import datetime

# telebot.apihelper.proxy = {'https': 'https://95.168.185.183:8080'}

bot = telebot.TeleBot(config.access_token)

d = {'monday': 1, 'tuesday': 2, 'wednesday': 3,
     'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}


def get_page(group, week):
    if week:
        week = str(week) + '/'
    url = '{domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        domain=config.domain,
        week=week,
        group=group)
    response = requests.get(url)
    web_page = response.text
    return web_page


def parse_schedule(web_page, day):

    soup = BeautifulSoup(web_page, "html5lib")

    # Получаем таблицу с расписанием на понедельник
    schedule_table = soup.find("table", attrs={"id": day})

    if schedule_table:
        # Время проведения занятий
        times_list = schedule_table.find_all("td", attrs={"class": "time"})
        times_list = [time.span.text for time in times_list]

        # Место проведения занятий
        locations_list = schedule_table.find_all("td", attrs={"class": "room"})
        locations_list = [room.span.text for room in locations_list]

        # Название дисциплин и имена преподавателей
        lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
        lessons_list = [lesson.text.split('\n\n') for lesson in lessons_list]
        lessons_list = [', '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]

        return times_list, locations_list, lessons_list
    return None


@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
def get_schedule(message):
    """ Получить расписание на указанный день """
    # PUT YOUR CODE HERE
    day, week, group = message.text.split()
    day = day[1:]
    day = str(d[day]) + 'day'
    web_page = get_page(group, week)
    if parse_schedule(web_page, day):
        times_lst, locations_lst, lessons_lst = \
            parse_schedule(web_page, day)
        resp = ''
        for time, location, lession in zip(times_lst, locations_lst, lessons_lst):
            resp += '<b>{}</b>, {}, {}\n'.format(time, location, lession)
        bot.send_message(message.chat.id, resp, parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, text='You are free on this day!')
    pass


@bot.message_handler(commands=['near'])
def get_near_lesson(message):
    """ Получить ближайшее занятие """
    # PUT YOUR CODE HERE
    _, group = message.text.split()

    x = localtime()
    b = int(strftime('%W', x))
    a = strftime('%A', x)
    a = a.lower()
    h = strftime('%H', x)
    m = strftime('%M', x)

    day = str(d[a]) + 'day'
    if b % 2 == 0:
        week = '1'
    else:
        week = '2'

    web_page = get_page(group, week)
    if parse_schedule(web_page, day):
        times_list, locations_list, lessons_list = parse_schedule(web_page, day)
        i = 0
        pair = 0
        for j in times_list:
            _, t_sch = j.split('-')
            th, tm = t_sch.split(':')
            t_sch = int(th + tm)
            t_now = int(h + m)
            if t_now < t_sch:
                resp = ''
                resp += '<b>{}</b>, {}, {}\n'.format(times_list[i], locations_list[i], lessons_list[i])
                bot.send_message(message.chat.id, resp, parse_mode='HTML')
                pair = 1
                break
            i += 1
        if pair == 0:
            bot.send_message(message.chat.id, text="Dobby is free for today")
    else:
        bot.send_message(message.chat.id, text="Today's weekend, dummy <3")
    pass


@bot.message_handler(commands=['tommorow'])
def get_tommorow(message):
    """ Получить расписание на следующий день """
    # PUT YOUR CODE HERE
    _, group = message.text.split()
    x = localtime()
    b = int(strftime('%W', x))
    a = strftime("%A", x)
    a = a.lower()
    if a != 'sunday':
        day = str(d[a]+1) + 'day'
    else:
        day = '1day'
        b += 1
    if b % 2 == 0:
        week = '1'
    else:
        week = '2'
    web_page = get_page(group, week)
    if parse_schedule(web_page, day):
        times_lst, locations_lst, lessons_lst = \
            parse_schedule(web_page, day)
        resp = ''

        for time, location, lession in zip(times_lst, locations_lst, lessons_lst):
            resp += '<b>{}</b>, {}, {}\n'.format(time, location, lession)
        bot.send_message(message.chat.id, resp, parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, text='You are free on this day!')
    pass


@bot.message_handler(commands=['all'])
def get_all_schedule(message):
    """ Получить расписание на всю неделю для указанной группы """
    # PUT YOUR CODE HERE
    _, week, group = message.text.split()
    web_page = get_page(group, week)
    for i in range(1, 7):
        day = str(i)+'day'
        if parse_schedule(web_page, day):
            times_lst, locations_lst, lessons_lst = \
                parse_schedule(web_page, day)
            resp = ''
            for time, location, lession in zip(times_lst, locations_lst, lessons_lst):
                resp += '<b>{}</b>, {}, {}\n'.format(time, location, lession)
            bot.send_message(message.chat.id, resp, parse_mode='HTML')

    pass


if __name__ == '__main__':
    bot.polling(none_stop=True)
