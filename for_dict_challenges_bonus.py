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
    lst = sorted([(user['sent_by'],len(set(user['seen_by']))) for user in history], key = lambda x: x[:][1], reverse= True)
    max_count = lst[0][1]

    return 'Больше всего уникальнх пользователей у :', set([id for id,cnt in lst if cnt == max_count])

def time_chat(history):
    count_morning = 0
    count_afternoon = 0
    count_evening = 0
    
    for tm in history:
        if tm['sent_at'].hour < 12 :
            count_morning += 1
            
        elif  12 <= tm['sent_at'].hour < 18 :
            count_afternoon += 1
            
        else:
            count_evening += 1
    
    if max([count_morning, count_afternoon, count_evening]) == count_morning :        
        return f"Больше всего сообщений утром"
    
    elif max([count_morning, count_afternoon, count_evening]) == count_afternoon:        
        return "Больше всего сообщений днем"
    
    else:       
        return "Больше всего сообщений вечером"

def most_common_reply(history):
    lst = [users['reply_for'] for users in history if users['reply_for'] != None ]
    count = Counter(lst)
    max_count = count.most_common()[0][1]
    return f'Самые длинные треды у :', *[id for id,cnt in count.most_common() if cnt == max_count] # не придумал, как раскрыть через ","
    
    
history = generate_chat_history()



if __name__ == "__main__":
    # print(generate_chat_history())
    print(most_common_message(history))
    print(*unique_users_see(history))
    print(time_chat(history))
    print(*most_common_reply(history))