"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений. done
2. Вывести айди пользователя, на сообщения которого больше всего отвечали. done
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей. done(?)
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов). done
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
from collections import Counter
import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

def most_common_message(history):
    lst = [user['sent_by'] for user in history]
    cnt = Counter(lst)
    return f"Больше всех сообщений у профиля {cnt.most_common(1)[0][0]}"

def most_common_reply(history):
     lst = sorted([user['sent_by'] for user in history if user['reply_for'] != None])
     cnt = Counter(lst)
     
     return cnt.most_common(10)

def unique_users_see(history):
    dic_lst = {}
    lst_2 = [user['sent_by'] for user in history]
    
    for cnt in lst_2:
        if cnt  not in dic_lst:
            dic_lst[cnt] = 1
        else:
            dic_lst[cnt] += 1
    
    max_count = max(dic_lst.values())
    
    unique_lst = [id for id,cnt in dic_lst.items() if cnt == max_count]
    
    return 'Больше всего уникальнх пользователей у :', *unique_lst

def time_chat(history):
    message_times = {'Утро' : 0, 
                     'День' : 0, 
                     'Вечер' : 0}
    
    for tm in history:
        if tm['sent_at'].hour < 12 :
            message_times['Утро'] += 1
            
        elif  12 <= tm['sent_at'].hour < 18 :
            message_times['День'] += 1
            
        else:
            message_times['Вечер'] += 1
    
    most_active = max(message_times, key = message_times.get)
    
    return most_active

def most_common_reply(history):
    dict_lst = {}
    
    for messange in history:
        reply_to = messange["reply_for"]
        
        if reply_to is None:
            continue
        
        if reply_to in dict_lst:
            dict_lst[reply_to] += 1
        
        else:
            dict_lst[reply_to] = 1
    
    max_count = max(dict_lst.values())
    
    longest_start_message = [ message for message,cnt in dict_lst.items() if cnt == max_count]
    return f'Самые длинные треды у сообщений:', *longest_start_message
    
    
history = generate_chat_history()



if __name__ == "__main__":
    print(most_common_message(history))
    print(*unique_users_see(history))
    print(time_chat(history))
    print(*most_common_reply(history))