
from slack import get_user_ids, send_mim_msg, send_pub_msg, get_conversations
import random
# 중복 피할 경우 db 필요
# from db import db_init, db_add_stars, db_get_matches, db_close


msg_template = '''
멍멍! 이번주 당신의 랜덤 런치의 멤버는 <@{}>, <@{}>, <@{}>, <@{}>입니다. 무엇을 먹을지 간단히 논의해보시고\n
주말동안 있었던 일, 흥미로운 소식, 나누고 싶은 이야기 등으로 함께 편안한 시간 보내시며,\n
이번주도 모두 모두 화이팅할 수 있는 기운을 나눠주세요💪💪\n\n
멋진 시간 보낸 후 사진과 후기를 #team_zep_lunch 에 올려주세요.\n
'''
# 1명일 경우
msg_template1 = '''
안타깝게도 <@{}>님은 이번 주 랜덤 런치 매칭에 실패하였습니다. lunch 채널에서 팀을 찾아보세요!\n
'''

msg_template2 = '''
멍멍! 이번주 당신의 랜덤 런치의 멤버는 <@{}>, <@{}>입니다. 무엇을 먹을지 간단히 논의해보시고\n
주말동안 있었던 일, 흥미로운 소식, 나누고 싶은 이야기 등으로 함께 편안한 시간 보내시며,\n
이번주도 모두 모두 화이팅할 수 있는 기운을 나눠주세요💪💪\n\n
멋진 시간 보낸 후 사진과 후기를 #team_zep_lunch 에 올려주세요.\n
'''

msg_template3 = '''
멍멍! 이번주 당신의 랜덤 런치의 멤버는 <@{}>, <@{}>, <@{}>입니다. 무엇을 먹을지 간단히 논의해보시고\n
주말동안 있었던 일, 흥미로운 소식, 나누고 싶은 이야기 등으로 함께 편안한 시간 보내시며,\n
이번주도 모두 모두 화이팅할 수 있는 기운을 나눠주세요💪💪\n\n
멋진 시간 보낸 후 사진과 후기를 #team_zep_lunch 에 올려주세요.\n
'''

pub_msg_template = '''
🐶 월월! 🦴....\n
- 이번 주 매칭된 조 개수: {}개 \n
- 미션1(선택): 인증 사진으로 자랑하기 \n
- 미션2(선택): 운 없이 홀로 선정된 팀원 구해주기
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
