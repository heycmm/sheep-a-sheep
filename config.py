
# token令牌 这个自己抓得到
t=''
count = 30000
# 刷次数排名的接口
rank_url = 'https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time=1&rank_role=1&skin=1'
# 第二关
second_map_url = 'https://cat-match.easygame2021.com/sheep/v1/game/map_info?map_id=90016'
# 第一关
first_map_url = 'https://cat-match.easygame2021.com/sheep/v1/game/map_info?map_id=80001'

headers = {
    'Content-Type': 'application/json',
    'Host': 'cat-match.easygame2021.com',
    't': t,
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b36) NetType/WIFI Language/zh_CN',
}