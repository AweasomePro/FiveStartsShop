
import requests
from . import digestutil

COMPANY_ID = 'company_id'
MSG_TYPE = 'msg_type'
DATA = 'data'
DATA_DIGEST = 'data_digest'
SIGN = '1e3bad4a9517457d977865c7f86fe507'

HOST = 'http://japi.zto.cn/zto/api_utf8/'
PRICE = '/priceAndHourInterface'


company_id_string = '1e3bad4a9517457d977865c7f86fe507'
msg_type_string = {'priceAndHourInterface': 'GET_HOUR_PRICE'}


def postPriceAndHourInterface(sendProv='', sendCity='', dispProv='', dispCity=''):

    data = {
        "sendProv": sendProv,
        "sendCity": sendCity,
        "dispProv": dispProv,
        "dispCity": dispCity
    }

    json = {
        COMPANY_ID: company_id_string,
        MSG_TYPE: msg_type_string,
        DATA: data,
        DATA_DIGEST: digestutil.digest(data=str(data), sign=SIGN)
    }

    result = requests.post(HOST + PRICE, data=json, timeout=5)
    return result


