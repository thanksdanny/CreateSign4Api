#!/usr/bin/python
#-*-coding:utf-8-*-
#subject:生成md5的签名

__author__ = 'thanksdanny'

import hashlib

# key
key = '123456'

# 若需要大写upper=1，否则upper=0


def create_sign(parameters, upper=0):
    temp = []
    es = sorted(parameters.iteritems(), reverse=False)
    for it in es:
        k = it[0]
        v = it[1]
        temp.append(k+"="+v+"&")
    temp.append("key="+key)
    # make list change to string
    stringA = ''.join(temp) 
    #md5
    m = hashlib.md5()
    m.update(stringA)
    m.digest()
    if upper: 
        return m.hexdigest().upper()
    else: 
        return m.hexdigest()
    return md5sign(stringA)


def main():
    param = {
        'xxx': 'xxx'
    }
    print '>>>生成签名<<<'
    print '========华丽的分割线========'
    target_apisign = '16edaf56d813c50fd8a7fbd0d1721f92'
    print "接口的签名是：" + target_apisign

    mysign = create_sign(param)
    print "我的签名是：" + mysign

    if target_apisign == mysign:
        print "恭喜你成功了"
    else:
        print "不一样啊锁嗨"


if __name__ == '__main__':
    main()