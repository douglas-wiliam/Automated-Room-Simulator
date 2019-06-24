message_list = list()
list_limit = 5

def insert_message(msg):
    if(len(message_list) > list_limit):
        message_list.pop(-1)

    message_list.insert(0, msg)

def print_messages():
    for message in message_list:
        print(message)
    