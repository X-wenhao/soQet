'''
全局公用变量控制台
'''

__AUTHORS__ = ['smdsbz', 'yjweng01', 'X-wenhao', 'Endless-Run']


import os




######### Folder Settings ########

ROOT_PATH = os.path.split(os.path.realpath(__file__))[0]

#### Database ####

# 数据库文件夹
DB_FOLDER = os.path.join(ROOT_PATH, 'database')

# 用户信息 - 账号、密码、附加一个TITLES
USER_DB = os.path.join(DB_FOLDER, 'user.db')

# 聊天室聊天记录
CHAT_ROOM_FOLDER = os.path.join(DB_FOLDER, 'chat_rooms')
'''
计划是给每一个聊天室实例创建一个TBALE
'''

# 个人聊天记录
P2P_CHAT_FOLDER = os.path.join(DB_FOLDER, 'P2P_chats')
'''
每一个小窗口实例创建一个TABLE
'''

#### User Info ####
pass



#### Security ####

# 用户密码hash前简单加密用
SALT = "I've got Linear Algebra test in Week 13!!!"

# 邀请码（暂时不需要）
INVITATION_CODE = "edoc_noitativni"





######## DEBUGGING ########

if __name__ == '__main__':
    print(USER_DB)
