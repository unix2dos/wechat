# coding=utf8
import itchat


def send_group(group, msg):
    rooms = itchat.get_chatrooms(update=True)
    rooms = itchat.search_chatrooms(name=group)
    if not rooms:
        print("None group found")
    else:
        itchat.send(msg, toUserName=rooms[0]["UserName"])


if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    send_group(u"一号白菜1", "test msg")
    itchat.run()
