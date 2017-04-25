'''
全局公用变量控制台
'''

__AUTHORS__ = ['smdsbz', 'yjweng01', 'X-wenhao', 'Endless-Run']


import os



ROOT_PATH = os.path.split(os.path.realpath(__file__))[0]


DB_FOLDER = os.path.join(ROOT_PATH, 'database')
USER_DB = os.path.join(DB_FOLDER, 'user.db')
CHAT_ROOM_FOLDER = os.path.join(DB_FOLDER, 'chat_rooms')
P2P_CHAT_FOLDER = os.path.join(DB_FOLDER, 'P2P_chats')



if __name__ == '__main__':
    print(USER_DB)
