import hashlib
import base64


def digest(data='', sign='', charset='utf-8'):
    if data == '' or sign == '':
        return ''
    m = hashlib.md5()
    m.update(bytes(data + sign, charset))
    md5value = m.digest()
    return base64.b64encode(md5value).decode(charset)


if __name__ == '__main__':
    print(digest("{ \"sendProv\": \"湖北\", \"sendCity\": \"荆州市\", \"dispProv\": \"浙江\", \"dispCity\": \"金华市\" }",
           "15f65487ffda"))
