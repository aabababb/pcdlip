import random
from bs4 import BeautifulSoup
import datetime
import os
import sys
from prettytable import PrettyTable
import json
import requests
import time
import urllib3
import re



# 是否为数字
def num_judge(num):
    try:
        num_test = int(num)
        return True
    except:
        return False


def num_Range(num):
    if int(num) > 0 and int(num) < 7:
        return True
    else:
        return False



def class_pretty():
    x = PrettyTable(["序号", "操作"])
    x.align["序号"] = "2"
    x.padding_width = 1
    x.add_row(["1", '爬取今日'])
    x.add_row(["2", '查询最近'])
    x.add_row(["3", '查询所有'])
    x.add_row(["4", '日期查询'])
    x.add_row(["5", '更新原有'])
    x.add_row(["6", '测试'])
    print(x)

def userAgents():
    '''
    随机选择User-Agent
    '''
    USER_AGENTS = [
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
        'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
        'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        ]
    return random.choice(USER_AGENTS)

def proxyv():
    proxies = pickle_operation().pickle_read('Ally')
    proxylist1 = []
    #proxiesk = sorted(proxies.key())[0]
    try:
        proxiesv = proxies.values()
        #print('proxiesv=%' %proxiesv)        
        if proxies == False or proxiesv == None:
            return None
        else:
            proxylist = proxies
            #print('proxylist=%s' %proxylist)
            for k,v in proxylist.items():
                if v == None:
                    return None
                else:
                    for i in v:
                        proxylist1.append(i)
                       #print (iplist1)
            if proxylist1 == []:
                return None
            else:
                return (proxylist1)
    except AttributeError:
        print('proxy-AttributeError')
        return None
    except IndexError:
        print('proxy-IndexError')
        return None
    #print('proxies=%s' %proxiesv)


def proxyc():
    global checker
    global proxy1
    print('proxychecker=%s' %checker)
    if checker == False or proxy1 == None:
        return None
    else:
        
        return random.choice(proxy1)

def filepath():
    #global file_path
    if getattr(sys, 'frozen', False):
        file_path = os.path.dirname(sys.executable)
    elif __file__:
        file_path = os.path.dirname(__file__)
    return file_path

# pkl文件保存读写
class pickle_operation():
    
    def __init__(self, now=None):
        #global file_path
        file_path = filepath()
        now = datetime.datetime.now()
        self.now_start = now.strftime('%Y-%m-%d')
        #self.ip_existence = ''.join([sys.path[0], '\\myip_list.txt'])
        self.ip_existence = os.path.join(file_path,'myip_list.txt')
        #print('ipexistence=%s' %self.ip_existence)

    # 写入文件
    def pickle_save(self, ip_list):
        my_list = {}
        my_list1 = {}
        my_list2 = {}
        #print('saveiplist=%s' %ip_list)
        # 判断文件是否存在，存在读取字典，不存在创建字典
        if os.path.exists(self.ip_existence):
            try:
                #pickle_du = open(sys.path[0]+'\\myip_list.txt', 'r')
                pickle_du = open(self.ip_existence,'r')
                data = pickle_du.read()
                #print('savedata=%s' %data)
                #print(type(data))

                my_list2 = json.loads(data)
                #print('my_list2=%s' %my_list2)
                #print(type(my_list2))
                #print('saveiplist=%s' %ip_list)
                if not ip_list == None:
                    my_list1[self.now_start] = ip_list
                    #print('my_list2%s' %my_list2)
                    #print('my_list1%s' %my_list1)
                    
                    for key in my_list1.keys():
                        my_list[key]=list(my_list1[key])
                        for key in my_list2.keys():
                            if key in my_list:
                                for v in my_list2[key]:
                                    if not v in my_list[key]:
                                        my_list[key].append(v)
                            else:
                                my_list[key]=list(my_list2[key])
                else:
                    my_list = my_list2

                
                #print('my_listread%s' %my_list)
                pickle_du.close()
            except EOFError:
                print('pickle_saveEOFError')
                my_list[self.now_start] = ip_list
                #print(ip_list)
                #print(my_list)
            except TypeError:
                print('pickle_saveTypeError')
                my_list[self.now_start] = ip_list
                #my_list = my_list2
                #print('myip_list=%s' %ip_list)
            except json.decoder.JSONDecodeError:
                print('pickle_savejson.decoder.JSONDecodeError')
                my_list[self.now_start] = ip_list
                #print('myip_list=%s' %ip_list)
              
        else:
            my_list[self.now_start] = ip_list
        
        #pickle_file = open(sys.path[0]+'\\myip_list.txt', 'w')
        pickle_file = open(self.ip_existence,'w')
        #print('sys.path[0]=%s' %pickle_file)
        #print('ip_existence=%s' %pickle_file)
        print('eof-mylist=%s' %my_list)

        #print(type(my_list))
        writes = json.dump(my_list, pickle_file)
        #print('writes=%s' %writes)
        
        pickle_file.close()
        number_result = '---更新成功---'
        
        return number_result

    def pickle_save2(self, ip_list):
        # 判断文件是否存在，存在读取字典，不存在创建字典
        if os.path.exists(self.ip_existence):
            my_list = {}
        my_list[self.now_start] = ip_list
        #print('savemylist=%s' %my_list)
        #pickle_file = open(sys.path[0]+'\\myip_list.txt', 'w')
        pickle_file = open(self.ip_existence,'w')
        json.dump(my_list, pickle_file)        
        pickle_file.close()
        number_result = '---更新成功---'
        return number_result

    # 读取文件
    def pickle_read(self, state, Interface=None):
        # state = Lately 查询最近
        # state = Ally 查询所有
        # state = Date 查询日期
        # Interface = 1 接口调用
        if os.path.exists(self.ip_existence):
            #pickle_du = open(sys.path[0]+'\\myip_list.txt','r')
            pickle_du = open(self.ip_existence,'r')        
            data = pickle_du.read()
            #print('datatype=%s' %type(data))
            #print(data)
            try:
                #my_list2 = dict(data)
                my_list2 = json.loads(data)
                #print('readmylist2=%s' %my_list2)
            except EOFError:
                print('pickle_read-EOFError: Ran out of input')
                my_list2 = {}
                return False
            except TypeError:
                print('pickle_readTypeError')
                my_list2 = {}
                return False
            except json.decoder.JSONDecodeError:
                print('pickle_read-json.decoder.JSONDecodeError')
                my_list2 = {}
                return False
            pickle_du.close()
            
        else:
            print('查询为空,请先更新')
            return False
        if state == 'Lately':
            number = sorted(my_list2.keys())[len(my_list2)-1]
            number_list = my_list2[number]
            if Interface == 1:
                number_result = {'代理IP': number_list}
            else:
                number_result = {'最近更新日期': number, '代理IP': number_list}
        elif state == 'Ally':
            number_result = my_list2
        elif state == 'Date':
            while True:
                date = input('请输入要查询的日期(格式:%Y-%M-%D)：')
                if date in my_list2.keys():
                    number_result = {'代理IP': my_list2[date]}
                    break
                else:
                    print('填写日期有误，请重新填写')
        #print('readnmuber_result=%s' %number_result)
        return number_result


# 爬代理


class ip_Crawler():

    def __init__(self,url1):
        global proxy1
        #url1 = purl()
        print('url1=%s' %url1)
        userAgentsc = userAgents()
        #print('userAgentsc=%s' %userAgentsc)
        self.header = {'User-Agent': userAgentsc}
        attempts = 0
        success = False
        while attempts < 5 and not success:
            try:
                prolist = proxyc()
                print('craw-proxy=%s' %prolist)
                self.html = requests.get(url=url1, headers=self.header,proxies=prolist,timeout=15)
                #print('self.html=%s' %self.html)                    
                success = True
                #print('crawtry')
            except Exception as e:
                  #raise e
                print('%s'%e)
                attempts += 1
                time.sleep(3)
                proxy1.remove(prolist)


        #print('self.html=%s' % self.html.text)

    def ip_start(self):
        #print('ipstart')
        attempts = 0
        try:
            htmlrs = self.html
            htmlrs.encoding = 'utf-8'
            soup = BeautifulSoup(htmlrs.text, "html5lib")        
            ip_result = []
            ip_dict = {}
            i = 0
            #fa = soup.find_all('tr',class_='odd')
            fa = soup.find_all('tr')
            lfa = len(list(fa[1:]))
            if not fa == []:
                #print('fa=%s' %fa[1:])
                #print('len-fa=%s' %lfa)
                for each in fa[1:]:
                    ip_gao = str(each.select('td')[4].text)
                    #print('ipgao=%s' % ip_gao)
                    if '2019' in ip_gao: 
                        #ip_http = str(each.select('td')[3].text).strip()
                        ip_http = 'http'
                        ip_num = str(each.select('td')[0].text).strip()
                        #print('num=%s' % ip_num)
                        ip_dk = str(each.select('td')[1].text).strip()
                        #print('dk=%s' % ip_dk)
                        ip_list = ''.join([ip_num, ':', ip_dk])
                        #print('iplist=%s' % ip_list)
                        ip_dict = {ip_http: ip_list}
                        ip_result.append(ip_dict)
                        #print('ipdict=%s' % ip_dict)
                        #print('ipresult=%s' % ip_result)
                        #print(type(ip_result))
                    i = i + 1
                    if i == lfa:
                        list_ip = len(ip_result)
                        print('ipresult=%s' % ip_result)
                        print('已爬取%s 个ip...' % list_ip)

                        return(ip_result)
            else:
                soupfind = re.findall('Too Many Requests',str(soup))
                print('soupfind=%s' %soupfind)
                print('soup=%s' %soup)
                if soupfind == True:
                
                    print('soup=%s' %soup)
                    ip_result = {}
                    return(ip_result)

        except AttributeError:
            print('ip_start-AttributeError')
            attempts += 1
            time.sleep(3)
            if attempts == 5:
                print('ip_start-AttributeError-%s' %attempts)
                return

            	

# 检测代理ip是否可用
def ip_testing(ip_list):
    print('---检测是否可用---')
    #print(type(ip_list))
    #print('ip_list＝%s' %ip_list)
    userAgentsc = userAgents()
    #print('userAgentsc=%s' %userAgentsc)
    header = {'User-Agent':userAgentsc}
    result_last = []
    a = 1
    my_ip = myself_ip(header)
    iptest = ip_list
    print('iptest=%s' %iptest)
    iptest2 = {}

    for k,v in iptest.items():
        
        for j in v:
            iptest2.update(j)
            result ={}
            ip_http = sorted(iptest2.keys())[0]
            ip_num = sorted(iptest2.values())[0]
            proxy_support = {ip_http: ip_num}
            #proxy_support = urllib.request.ProxyHandler({'HTTPS': '121.231.154.12:6666'})
            print('support=%s' % proxy_support)
            #print('iptest2=%s' %iptest2)
            url = 'http://pv.sohu.com/cityjson'
            #url = 'http://ip.chinaz.com/getip.aspx'
            try:
                r = requests.get(url, headers=header, proxies=iptest2,timeout=15)
                ip = r'(?:(?:(?:25[0-5]|2[0-4]\d|(?:(?:1\d{2})|(?:[1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|(?:(?:1\d{2})|(?:[1-9]?\d))))'
                time.sleep(5)
                print('r.text=%s' % r.text)
                print('r.text-len=%s' %len(r.text))
                print('my_ip=%s' % my_ip)
                rtext = re.findall(ip,r.text)
                myiptext = re.findall(ip,my_ip)
                print('rtext=%s' %rtext)
                if r.text == my_ip or rtext == [] or rtext == myiptext or len(r.text) > 95:
                    print('continue')
                    continue
                else:
                    print('else')
                    result[ip_http] = ip_num
                    #result = iptest2
                    #print('result=%s' % result)
                    result_last.append(result)
                    print('可用\nresult_last=%s' % result_last)
            except Exception as e:
                #raise e
                print('%s'%e)                      
            a += 1
    return result_last


# 查询自己的ip
def myself_ip(header):
    attempts = 0
    success = False
    while attempts < 5 and not success:
        try:
            url = 'http://pv.sohu.com/cityjson'
            #url = 'http://ip.chinaz.com/getip.aspx'
            html = requests.get(url, headers=header,timeout=15)
            ip = r'(?:(?:(?:25[0-5]|2[0-4]\d|(?:(?:1\d{2})|(?:[1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|(?:(?:1\d{2})|(?:[1-9]?\d))))'           
            
            fip = re.findall(ip,html.text)
            print('fip=%s' %fip)
            if not fip == []:
                success = True
                return html.text
            else:
                attempts += 1
                time.sleep(5)
                print('timesleep-%s' %attempts)
                if attempts==5:
                    print('attemptsConnectTimeout-%s' %attempts)
                    return
        except Exception as e:
            #raise e
            print('%s'%e)
            attempts += 1
            time.sleep(3)
            if attempts==5:
                return

def fh():
    try:
        
        print('fhcontinue=%s' %a)
    except NameError:
        print('NameError')
        return

def inivate(num):
    global checker
    global proxy1
    global file_path
    # 爬取今日
    if num == '1':
        print('---爬取今日的高匿代理ip---')
        for i in range(1,50):
            url_i = 'http://www.89ip.cn/index_'+ str(i)+'.html'
            ip_move = ip_Crawler(url_i).ip_start()
            #print('ipmove=%s' %ip_move)
            result = pickle_operation().pickle_save(ip_move)
            time.sleep(6)
    # 查询最近 lately
    elif num == '2':
        result = pickle_operation().pickle_read('Lately')
    # 查询所有 ally
    elif num == '3':
        result = pickle_operation().pickle_read('Ally')
    # 查询日期 Date
    elif num == '4':
        result = pickle_operation().pickle_read('Date')
    elif num == '5':
        ip_move = pickle_operation().pickle_read('Ally')
        ip_test = ip_testing(ip_move)
        result = pickle_operation().pickle_save2(ip_test)        
        checker = True
        #print('numchecker=%s' %checker)        
    elif num == '6':
        iplist = proxyc()
        #fh1 = fh()
        print('iprandomc=%s' %iplist)
        if not iplist == None:
            proxy1.remove(iplist)
            print(proxy1)
        else:
            print('6notcheck')
        result = False
    else:
        print('输入错误')
        result = ''
    if result is not False:
        try:
            #print('rsult=%s' %result)
            #print(type(result))
            return result
        except TypeError:
            print('inivateTypeError')


if __name__ == '__main__':
    #global checker
    checker = False
    proxy1 = proxyv()
    #file_path = filepath()
    while True:
        class_pretty()        
        num = input("序号 =>  ")
        if num_judge(num) is False or num_Range(num) is False:
            print('请输入正确序号')
            continue
        else:
            result_json = inivate(num)
        if result_json is None:
            continue
        if num == '2':
            keys_data = sorted(result_json.keys())[1]
            keys_ip = sorted(result_json.keys())[0]
            result_data = ''.join([keys_data, ' => ', result_json[keys_data]])
            result_ip = ''.join([keys_ip, ' => ', str(result_json[keys_ip])])
            print(result_data)
            print(result_ip)
        elif num == '3' or num == '1':
            print(result_json)            
        elif num == '5':
            print(result_json)

        elif num == '6':
            print(result_json) 
        elif num == '4':
            keys_data01 = sorted(result_json.keys())[0]
            result_dately = ''.join([keys_data01, ' => ', str(result_json[keys_data01])])
            print(result_dately)
        print('')
