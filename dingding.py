import datetime
import json
import requests


def send_dingding_msg(content,robot_id='ea8e59555f5a1b466ceb8b384f5cbd79b137e9260d15927b19febf4f85ba8376'):
    try:
        msg={
            'msgtype':'text',
            'text':{'content':content+'\n'+datetime.datetime.now().strftime('%m-%d%H:%M:%S')}}

        Headers ={'Content-Type':'application/json;charset-utf-8'}

        url='https://oapi.dingtalk.com/robot/send?access_token='+robot_id
        body=json.dumps(msg)
        requests.post(url,data=body,headers=Headers)
    except Exception as err:
        print('钉钉发送失败',err)

content='你是熊笨蛋吗'
send_dingding_msg(content)
