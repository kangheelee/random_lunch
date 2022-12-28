if __name__ == '__test__':
    print(__name__)
    print("hi")
    recent_bot_message = get_conversations()
    for mes in recent_bot_message:
        try:
            if mes["bot_id"] == 'B03G012J1UH':
                reactions = mes["reactions"]
                print(reactions)
                break
        except:
            print('key error occured')
