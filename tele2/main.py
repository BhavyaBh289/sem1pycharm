import telebot
import requests
import json
import time

with open("t1.txt", "r") as f:
    for a in f:
        token = a
bot = telebot.TeleBot(token)
base_url = "https://api.telegram.org/bot" + token + "/sendPoll"
qno = 0
qans = (0, 1, 1, 1, 3, 1, 1, 0, 0, 0)
dictionary = {}


@bot.message_handler(commands=['greet', 'start'])
def greet(message):
    msg = ''' Hello, this is a chatbot \n If you wish to start a quiz type /startquiz '''
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=["startquiz"])
def greet(message):
    global qno, dictionary
    question_1 = {
        "chat_id": message.chat.id,
        "type": "quiz",
        "open_period": 5,
        "is_anonymous": False,
        "question": "Grand Central Terminal, Park Avenue, New York is the world’s:",
        "options": json.dumps(
            ["Largest railway station", "Highest railway station", "Longest railway station", "None of the above"]),
        "correct_option_id": 0
    }
    question_2 = {
        "chat_id": message.chat.id,
        "type": "quiz",
        "open_period": 5,
        "is_anonymous": False,
        "question": "Entomology is the science that studies:",
        "options": json.dumps(
            ["Behavior of human beings", "Insects", "The origin and history of technical and scientific terms",
             "The formation of rocks"]),
        "correct_option_id": 1
    }
    question_3 = {
        "chat_id": message.chat.id,
        "type": "quiz",
        "open_period": 5,
        "is_anonymous": False,
        "question": "Eritrea, which became the 182nd member of the UN in 1993, is in the continent of:",
        "options": json.dumps(["Asia", "Africa", "Europe", "Australia"]),
        "correct_option_id": 1
    }
    question_4 = {
        "chat_id": message.chat.id,
        "type": "quiz",
        "open_period": 5,
        "is_anonymous": False,
        "question": "Garampani sanctuary is located at:",
        "options": json.dumps(["Junagarh, Gujarat", "Diphu, Assam", "Kohima, Nagaland", "Gangtok, Sikkim"]),
        "correct_option_id": 1
    }
    question_5 = {
        "chat_id": message.chat.id,
        "type": "quiz",
        "open_period": 5,
        "is_anonymous": False,
        "question": "For which of the following disciplines is Nobel Prize awarded:",
        "options": json.dumps(
            ["Physics and Chemistry", "Physiology or Medicine", "Literature, Peace and Economics", "All of the above"]),
        "correct_option_id": 3
    }
    question_6 = {
        "chat_id": message.chat.id,
        "type": "quiz",
        "open_period": 5,
        "is_anonymous": False,
        "question": "Hitler party which came into power in 1933 is known as:",
        "options": json.dumps(["Labour Party", "Nazi Party", "Ku-Klux-Khan", "Democratic Party"]),
        "correct_option_id": 1
    }

    question_7 = {
        "chat_id": message.chat.id,
        "type": "quiz",
        "open_period": 5,
        "is_anonymous": False,
        "question": " FFC stands for:",
        "options": json.dumps(
            ["Foreign Finance Corporation", " Film Finance Corporation", " Federation of Football Council",
             " None of the above"]),
        "correct_option_id": 1
    }

    question_8 = {
        "chat_id": message.chat.id,
        "type": "quiz",
        "open_period": 5,
        "is_anonymous": False,
        "question": " Fastest shorthand writer was:",
        "options": json.dumps(["Dr. G. D. Bist", " J.R.D. Tata", " J.M. Tagore", " Khudada Khan"]),
        "correct_option_id": 0
    }

    question_9 = {
        "chat_id": message.chat.id,
        "type": "quiz",
        "open_period": 5,
        "is_anonymous": False,
        "question": " Epsom (England) is the place associated with:",
        "options": json.dumps(["Horse racing", " Polo", "Shooting", "Snooker"]),
        "correct_option_id": 0
    }

    question_10 = {
        "chat_id": message.chat.id,
        "type": "quiz",
        "open_period": 5,
        "is_anonymous": False,
        "question": " First human heart transplant operation conducted by Dr. Christiaan Barnard on Louis Washkansky, was conducted in:",
        "options": json.dumps(["1967", "1968", "1958", "1922"]),
        "correct_option_id": 0
    }
    requests.get(base_url, data=question_1)
    time.sleep(6)
    qno = 1
    requests.get(base_url, data=question_2)
    time.sleep(6)
    qno = 2
    requests.get(base_url, data=question_3)
    time.sleep(6)
    qno = 3
    requests.get(base_url, data=question_4)
    time.sleep(6)
    qno = 4
    requests.get(base_url, data=question_5)
    time.sleep(6)
    qno = 5
    requests.get(base_url, data=question_6)
    time.sleep(6)
    qno = 6
    requests.get(base_url, data=question_7)
    time.sleep(6)
    qno = 7
    requests.get(base_url, data=question_8)
    time.sleep(6)
    qno = 8
    requests.get(base_url, data=question_9)
    time.sleep(6)
    qno = 9
    requests.get(base_url, data=question_10)
    time.sleep(6)
    for a in dictionary:
        msg = f"User {a} has scored {dictionary[a]} marks"
        bot.send_message(message.chat.id, msg)


@bot.message_handler(func=lambda m: True)
def repeat(message):
    bot.send_message(message.chat.id, "invalid message")


@bot.poll_answer_handler()
def handle_poll_answer(pollAnswer):
    global qno, dictionary
    # print(pollAnswer.user.first_name,pollAnswer.option_ids)
    qans = (0, 1, 1, 1, 3, 1, 1, 0, 0, 0,0)
    # print(pollAnswer)
    print(pollAnswer.user.first_name,pollAnswer.option_ids,qans[qno],qno)
    usern = pollAnswer.user.first_name
    if (usern) in dictionary:
        if pollAnswer.option_ids == [qans[qno ]]:
            dictionary[usern] = int(dictionary[usern]) + 5
    else:
        if pollAnswer.option_ids == [qans[qno ]]:
            dictionary[usern] = 5
        else:
            dictionary[usern] = 0


def main():
    bot.polling()

if __name__ == '__main__':
    main()
