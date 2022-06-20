
from slack import get_user_ids, send_mim_msg, send_pub_msg, get_conversations
import random
# 중복 피할 경우 db 필요
# from db import db_init, db_add_stars, db_get_matches, db_close


pub_msg_demand = '''
@channel 왈왈! 😅 어김없이 돌아온 수요일 랜덤 런치~ 🎉🎉\n
랜덤 런치는 팀 간 소통의 기회를 늘리고자 매주 시행하고 있어요👏\n
- 참가를 원하시면 이모지를 아무거나 :star:*1시간 내로*:star: 달아주세요!!\n
- 1시간 뒤 유토가 만들어주는 조별 DM에서 무엇을 먹을지 정해주세요~! 🍕🍖🍚🍣 \n
'''

if __name__ == '__main__':

    # 이모지를 누른 사람 리스트업
    recent_bot_message = get_conversations()
    for mes in recent_bot_message:
        try:
            # you need to know bot id you made for random lunch bot
            if mes["bot_id"] == 'B03G012J1UH':
                reactions = mes["reactions"]
                print(reactions)
                break
        except:
            print('key error occured')

    stars = []
    for reaction in reactions:
        stars.extend(reaction['users'])

    stars = list(set(stars))

    # Open local dbfile and add users
    # db_init()
    # db_add_stars(stars)

    # 셔플하기 3회
    random.shuffle(stars)
    random.shuffle(stars)
    random.shuffle(stars)

    # 네명씩 조짜기
    weekly = []
    cnt = 0
    tmp = []
    for star in stars:
        tmp.append(star)
        cnt += 1
        if cnt % 4 == 0:
            weekly.append(tmp)
            tmp = []
        if stars.index(star) == len(stars) - 1:
            weekly.append(tmp)

    pairs = 0
    # 조마다 DM 보내기(마지막조가 3명 또는 2명 또는 1명인 경우 포함)
    for group in weekly:
        if len(group) == 4:
            msg = msg_template.format(group[0], group[1], group[2], group[3])
            send_mim_msg(group, msg=msg)
            pairs = pairs + 1
        elif len(group) == 3:
            msg = msg_template3.format(group[0], group[1], group[2])
            send_mim_msg(group, msg=msg)
            pairs = pairs + 1
        elif len(group) == 2:
            msg = msg_template2.format(group[0], group[1])
            send_mim_msg(group, msg=msg)
            pairs = pairs + 1
        else:
            msg = msg_template1.format(group[0])
            send_mim_msg(group, msg=msg)
        # print(group)
        # DEBUG
        # star1 = 'UKAUCTSCV' # kanghee
        # star2 = 'U017FMWG9CJ' # who
        # Open mim and send a message
        # break ## Send only one for testing

    # Send public message
    pub_msg = pub_msg_template.format(pairs)
    send_pub_msg(pub_msg, group)

    # db_close()
