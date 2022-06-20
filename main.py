
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
    # 채널에 수요 조사 메시지 발송
    send_pub_msg(pub_msg_demand)
