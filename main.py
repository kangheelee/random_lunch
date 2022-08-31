
from slack import get_user_ids, send_mim_msg, send_pub_msg, get_conversations
import random
# 중복 피할 경우 db 필요
# from db import db_init, db_add_stars, db_get_matches, db_close


pub_msg_demand = '''
@channel 왈왈! 😅 어김없이 돌아온 수요일 랜덤 런치~ 🎉🎉\n
랜덤 런치는 팀 간 소통의 기회를 늘리고자 매주 시행하고 있어요👏\n
- 참가를 원하시면 이모지를 아무거나 :star:*12시 전까지*:star: 달아주세요!!\n
- 12시 전후로 유토가 만들어주는 조별 DM에서 무엇을 먹을지 정해주세요~! 🍕🍖🍚🍣 \n
할 말이 없다면 아래 대화 주제로 얘기해보는 것은 어떨까요?\n
- 요즘 재밌게 본 영화나 드마나, 유튜브 공유\n
- 직장에서 중요한 것은 성장? 연봉? 복지? 재택?\n
- ZEP에 들어오게 된 계기는 무엇인가요?\n
'''

if __name__ == '__main__':
    # 채널에 수요 조사 메시지 발송
    send_pub_msg(pub_msg_demand)
