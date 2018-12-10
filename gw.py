# -*- coding: utf-8 -*-
# Support ===ZNF TEAM BOTZ===
from angrust import *
from ang.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
import pytz, pafy, time, asyncio, random, multiprocessing, timeit, sys, json, codecs, tweepy, glob, re, ast, six, os, subprocess, wikipedia, goslate, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
import youtube_dl
#==============================================================================#

cl = LINE("EvJOQRu5rt8USwco5JB4.Ob/xLexK+PHdjZfsE4KOTa.hm/6Kp67MNCKtH3GRBH9GKh8cdF5JuWepxweuzUqGjA=")
cl.log("Auth Token : " + str(cl.authToken))
channelToken = cl.getChannelResult()

ka = LINE("Ev2CJpHNGbp5kFQCkH18.xBc9fnXHk92MuhPkVlftga.xfgo2J9a4uyTM16Qgsr7zx/MZ6Virqs8uzm9B5lyO7E=")
ka.log("Auth Token : " + str(ka.authToken))

kb = LINE("EvCh1uXFdwiXqmcugqae.kUMjugFkf1sovGNP5PiIRG.Gynuy4K94JTg7ft6Gt6qcIjuZW1K71/GyBMnzZxG5Uc=")
kb.log("Auth Token : " + str(kb.authToken))

kc = LINE("Evj5WS1QOrjTCfXyfCn9.MQIKdcTcEIJHMOOfq8ibwq.jrefyb7sV6VIuh155cJ/VufFHu77WOEAobnHx7JoDMA=")
kc.log("Auth Token : " + str(kc.authToken))

kd = LINE("EvTGZwp1PT87IR6mesla.TDGZO7ZTYrztJvs3uHZAEG.7OscyLHWGj0doyQtcUJ/4BLcPM4of34VKukQlplId5c=")
kd.log("Auth Token : " + str(kd.authToken))

ke = LINE("EvZSuenMd28Lgxksj7Z9.nQceCpxmUTKQnTN8tCEroq.JmYOiSf95cfaTs+DmtiAoOgKsgU4NfrbUPTtDpW61J8=")
ke.log("Auth Token : " + str(ke.authToken))

k1 = LINE("Evdo9Wzlx6zazLDBqUgc.52ArcoauOU31pDYzN9mJla.fVx4lVwRm4MjzbpE3oi6Dmio4K2lwKSerm2qWigd+l0=")
k1.log("Auth Token : " + str(k1.authToken))

oepoll = OEPoll(cl)
K1C=[cl,ka,kb,kc,kd,ke]
K2C=[ka,kb,kc,kd,ke]
mid = cl.getProfile().mid
Amid = ka.getProfile().mid
Bmid = kb.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Smid = k1.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Smid]

whitelist=[""]
msg_dict = {}

helpMessage ="""
╔══════════════╗
║   「ZNF TEAM」
╠══════════════╝
║┍∘· Help
║┝∘· Help sett
║┝∘· Me
║┝∘· Sp
║┝∘· Gift
║┝∘· Spbot
║┝∘· kill「@」
║┝∘· tw1-5 kick「@」
║┝∘· Bantaii「cleanse grup」
║┝∘· Respon
║┝∘· Myid
║┝∘· Ourl
║┝∘· Gurl
║┝∘· Curl
║┝∘· Mybot
║┝∘· Botname
║┝∘· Runtime
║┝∘· Reboot
║┝∘· Ginfo
║┝∘· Gcreator
║┝∘· Dp「@」
║┝∘· Mid「@」
║┝∘· Info「@」
║┝∘· Cover「@」
║┝∘· Contact「@」
║┝∘· Tagall
║┝∘· Masukin coy
║┝∘· Bomat
║┝∘· /bye
║┝∘· tw1-5 bye
║┝∘· tw1-5 join
║┝∘· invite on
║┝∘· tw1-5 invite
║┝∘· Mygrup
║┝∘· tw1-5 grup
║┝∘· tw1-5 inv me:「Namagrup」
║┝∘· Leave all grup
║┝∘· Leave「Namagrup」
║┝∘· List member
║┝∘· Rechat
║┝∘· Add friend「send contact」
║┝∘· Del friend「send contact」
║┝∘· List friend
║┝∘· Clear friend
║┝∘· Add blacklist「send contact」
║┝∘· Del blacklist「send contact」
║┝∘· Banlist
║┝∘· Clear ban
║┝∘· Inta「mode nyusup」
║┝∘· ....
║┝∘· Clear inta
║┝∘· Gname:「text」
║┝∘· Cname:「text」
║┝∘· tw1-5 cn:「text」
║┝∘· Lurk「on/off」
║┝∘· Lurkers
║┝∘· Sider「on/off」
║┕∘· Broadcast:「Text」
╠══════════════╗
║  「ZNF TEAM BOT」
╠══════════════╝
║┍∘· ID line:「Id Line nya」
║┝∘· Sholat:「Nama Kota」
║┝∘· Cuaca:「Nama Kota」
║┝∘· Lokasi:「Nama Kota」
║┝∘· Music:「Judul Lagu」
║┝∘· Image:「text」
║┝∘· Fancytext:「text」
║┝∘· Yt:「Judul Lagu」
║┝∘· Ytvid:「Judul Video」
║┝∘· Profileig:「Nama IG」
║┝∘· Kalender
║┝∘· Time
║┝∘· Vn:「text」
║┝∘· Say:「text」
║┝∘· Sider:「text」
║┝∘· Welcome:「text」
║┝∘· Left:「text」
║┝∘· Tag:「text」
║┝∘· Coment:「text」
║┝∘· Add:「text」
║┝∘· Check all msg
║┝∘· Jumlah:「angka」
║┝∘· Spamtag「@」
║┝∘· Spamcall:「jumlahnya」
║┕∘· Spamcall
╠══════════════╗
║     「ANTIJS VERSION」
╚══════════════╝
"""
helpSetting ="""
╔══════════════╗
║      「Setting Protection」
╠══════════════╝
║┍⌾∘· Allprotect「on/off」
║┝⌾∘· Proinvite「on/off」
║┝⌾∘· Procancel「on/off」
║┝⌾∘· Proqr「on/off」
║┝⌾∘· Prokick「on/off」
║┝⌾∘· Notag「on/off」
║┝⌾∘· Projs「on/off」
║┕⌾∘· Grup set
╠═══════
║┍⌾∘· Sticker「on/off」
║┝⌾∘· Respon「on/off」
║┝⌾∘· Autojoin「on/off」
║┝⌾∘· Autoadd「on/off」
║┝⌾∘· Welcome「on/off」
║┝⌾∘· Left「on/off」
║┝⌾∘· Like「on/off」
║┕⌾∘· Post「on/off」
╠══════════════╗
║         「Setting Kicker」
╠══════════════╝
║┍⌾∘· Kicker「on/off」
║┝⌾∘· Kicker join
║┝⌾∘· Kicker bye
║┝⌾∘· Kicker kick 「@」
║┝⌾∘· Kicker cancel
║┝⌾∘· Kicker cn:「text」
║┝⌾∘· Kicker stay
║┝⌾∘· ZNF stay
║┝⌾∘· Kicker gift
║┝⌾∘· Kicker absen
║┕⌾∘· Kicker Kickall
╠══════════════╗
║     「ANTIJS VERSION」
╚══════════════╝
"""

wait = {
    "limit": 1,
    "spamr":False,
    "welmsg":"",
    "leftmsg":"",
    "Invi":False,
    "ainvite":False,
    "binvite":False,
    "cinvite":False,
    "dinvite":False,
    "einvite":False,
    "finvite":False,
    "atarget":False,
    "dtarget":False,
    "afriend":False,
    "dfriend":False,
    "atebz":False,
    "dtebz":False,
    "autoJoinTicket":False,
    "unsendMessage":False,
    "Tagg":False,
    "Tags":False,
    "ablacklist":False,
    "dblacklist":False,
    "ablack":False,
    "dblack":False,
    "reader":False,
    "Siri":False,
    "Sticker":False,
    "Autojoin":False,
    "Timeline":False,
    "LikeOn":False,
    "commentOn":False,
    "Mentionkick":False,
    "mimic":False,
    "message":"",
    "comment":"",
    "cctvteks":"",
    "teksp":"",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

org = {
    "tmimic":{},
    "Target":{},
    "Tebz":{},
    "Friend":{},
    "invitan":{}
    }

pro = {
    'proPoint':{},
    'proTime':{},
    'proJs':{},
    'Protectgr':{},
    'Protectcancl':{},
    'Protectinvite':{},
    'wellcome':{},
    'bymsg':{},
    'intaPoint':{},
    "Autokick":{},
    'intaTime':{}
    }

wait2 = {
    'readPoint':{},
    'Maxlimit':{},
    'blacklist':{},
    'readMember':{},
    'commentBlack':{},
    'setTime':{},
    'ROM':{}
    }

ciduk = {
    "cyduk":{},
    "ceadPoint":{},
    "ceadMember":{}
    }
data = {
    'info':{},
    'audio':{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

with open('setting.json', 'r') as fp:
    wait = json.load(fp)
with open('pro.json', 'r') as fp:
    pro = json.load(fp)
with open('org.json', 'r') as fp:
    org = json.load(fp)
with open('wait2.json', 'r') as fp:
    wait2 = json.load(fp)

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
#============================#
contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact1 = ka.getProfile()
backup1 = ka.getProfile()
backup1.displayName = contact1.displayName
backup1.statusMessage = contact1.statusMessage
backup1.pictureStatus = contact1.pictureStatus

contact2 = kb.getProfile()
backup2 = kb.getProfile()
backup2.displayName = contact2.displayName
backup2.statusMessage = contact2.statusMessage
backup2.pictureStatus = contact2.pictureStatus

contact3 = kc.getProfile()
backup3 = kc.getProfile()
backup3.displayName = contact3.displayName
backup3.statusMessage = contact3.statusMessage
backup3.pictureStatus = contact3.pictureStatus

contact4 = kd.getProfile()
backup4 = kd.getProfile()
backup4.displayName = contact4.displayName
backup4.statusMessage = contact4.statusMessage
backup4.pictureStatus = contact4.pictureStatus

contact5 = ke.getProfile()
backup5 = ke.getProfile()
backup5.displayName = contact5.displayName
backup5.statusMessage = contact5.statusMessage
backup5.pictureStatus = contact5.pictureStatus

contact7 = k1.getProfile()
backup7 = k1.getProfile()
backup7.displayName = contact7.displayName
backup7.statusMessage = contact7.statusMessage
backup7.pictureStatus = contact7.pictureStatus
#====================================================#
def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "⸢{} user reading ⸥\nhai ka ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["cctvteks"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══⸢ {} ⸥".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+" Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n Group : "+str(len(gid))+"\n Teman : "+str(len(teman))+"\n Expired : In "+hari+"\n Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n Runtime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def autolike():
    for zx in range(0,500):
      hasil = cl.activity(limit=500)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == True:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postid'],wait["comment"])
          ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ka.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],wait["comment"])
          kb.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kb.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],wait["comment"])
          kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],wait["comment"])
          kd.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kd.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],wait["comment"])
          ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ke.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],wait["comment"])
          print ("Like Success")
        except:
          pass
      else:
          print ("Already Liked")

def summon(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "╔═════[ Mentones ]═══════\n╠☛ 1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠☛  {}. ".format(str(no))
            else:
                textx += "╚══════════════════\n\n╔══════════════════\n  「 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀ : {} 」\n╚══════════════════".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def RECEIVE_MESSAGE(op):
    msg = op.message
    text = msg.text
    msg_id = msg.id
    receiver = msg.to
    sender = msg._from
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg._from in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg._from]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
                sys.exit(0)
    except Exception as error:
        print (error)
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            print ("[0] END OF OPERATION")
            return
        if op.type == 5:
            print ("[5] AUTO ADD")
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendMessage(op.param1,str(wait["message"]))
        if op.type == 11:
            if op.param1 in pro['intaPoint']:
                if op.param2 in Bots:
                    pass
                if op.param2 in org["friend"]:
                    pass
                else:
                    X = cl.getGroup(op.param1)
                    if X.preventedJoinByTicket == True:
                        pass
                    else:
                        cl.updateGroup(X)
                        invsend = 0
                        Ti = cl.reissueGroupTicket(op.param1)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        kb.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
        if op.type == 11:
            if op.param1 in pro["protectgr"]:
                if cl.getGroup(op.param1).preventedJoinByTicket == False:
                    if op.param2 not in Bots and op.param2 not in org["friend"]:
                        random.choice(K2C).reissueGroupTicket(op.param1)
                        X = random.choice(K2C).getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        random.choice(K2C).updateGroup(X)
                        random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])

            if op.param2 in wait2["blacklist"]:
                if cl.getGroup(op.param1).preventedJoinByTicket == False:
                    if op.param2 not in Bots and op.param2 not in org["friend"]:
                        random.choice(K2C).reissueGroupTicket(op.param1)
                        X = random.choice(K2C).getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        random.choice(K2C).updateGroup(X)
                        random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])


        if op.type == 13:
            if mid in op.param3:
                if wait["autojoin"] == True:
                    if op.param2 not in Bots and op.param2 not in org["friend"]:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Halo member " + str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Halo member " + str(ginfo.name))

            if op.param3 in Amid:
                if wait["autojoin"] == True:
                    if op.param2 not in Bots and op.param2 not in org["friend"]:
                        ka.acceptGroupInvitation(op.param1)
                        ginfo = ka.getGroup(op.param1)
                        ka.sendMessage(op.param1,"Halo member " + str(ginfo.name))
                        ka.leaveGroup(op.param1)
                    else:
                        ka.acceptGroupInvitation(op.param1)
                        ginfo = ka.getGroup(op.param1)
                        ka.sendMessage(op.param1,"Halo member " + str(ginfo.name))

            if op.param3 in Bmid:
                if wait["autojoin"] == True:
                    if op.param2 not in Bots and op.param2 not in org["friend"]:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Halo member " + str(ginfo.name))
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.sendMessage(op.param1,"Halo member " + str(ginfo.name))

            if op.param3 in Cmid:
                if wait["autojoin"] == True:
                    if op.param2 not in Bots and op.param2 not in org["friend"]:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Halo member " + str(ginfo.name))
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Halo member " + str(ginfo.name))

            if op.param3 in Dmid:
                if wait["autojoin"] == True:
                    if op.param2 not in Bots and op.param2 not in org["friend"]:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.sendMessage(op.param1,"Halo member " + str(ginfo.name))
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.sendMessage(op.param1,"Halo member " + str(ginfo.name))

            if op.param3 in Emid:
                if wait["autojoin"] == True:
                    if op.param2 not in Bots and op.param2 not in org["friend"]:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.sendMessage(op.param1,"Halo member " + str(ginfo.name))
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.sendMessage(op.param1,"Halo member " + str(ginfo.name))

            if op.param3 in Smid:
                if wait["autojoin"] == True:
                    if op.param2 not in Bots and op.param2 not in org["friend"]:
                        k1.acceptGroupInvitation(op.param1)
                        ginfo = k1.getGroup(op.param1)
                        k1.sendMessage(op.param1,"Halo member " + str(ginfo.name))
                        k1.leaveGroup(op.param1)
                    else:
                        k1.acceptGroupInvitation(op.param1)
                        ginfo = k1.getGroup(op.param1)
                        k1.sendMessage(op.param1,"Halo member " + str(ginfo.name))
#===============================================#
        if op.type == 13:
            if op.param2 in wait2["blacklist"]:
                random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                random.choice(K2C).cancelGroupInvitation(op.param1, [op.param3])
                try:
                    kc.cancelGroupInvitation(op.param1,[op.param3])
                    kd.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        ka.cancelGroupInvitation(op.param1,[op.param3])
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kb.cancelGroupInvitation(op.param1,[op.param3])
                            kc.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kd.cancelGroupInvitation(op.param1,[op.param3])
                                ke.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ka.cancelGroupInvitation(op.param1,[op.param3])
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kc.cancelGroupInvitation(op.param1,[op.param3])
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return

            if op.param1 in pro["protectinvite"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in org["friend"]:
                    pass
                else:
                    try:
                        if op.param2 not in Bots and op.param2 not in org["friend"]:
                            wait2["blacklist"][op.param2] = True
                            with open('wait2.json','w') as fp:
                                json.dump(wait2, fp, sort_keys=True, indent=4)
                            group = cl.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(K2C).cancelGroupInvitation(op.param1,[_mid])
                                random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                        else:
                            pass
                    except:
                        pass

            if op.param3 in wait2["blacklist"]:
                if op.param2 not in Bots and op.param2 not in org["friend"]:
                    random.choice(K2C).cancelGroupInvitation(op.param1,[op.param3])
                    wait2["blacklist"][op.param2] = True
                    with open('wait2.json','w') as fp:
                        json.dump(wait2, fp, sort_keys=True, indent=4)
                    random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])

#===========================================================#
        if op.type == 15:
            print ("[15] OP BYMSG")
            if op.param1 in pro["bymsg"]:
                if op.param2 in Bots:
                    return
                else:
                    cl.sendText(op.param1, wait["leftmsg"])
                    print ("member leave")
#==============[ PROTECT JOIN ]==================#
            if op.param1 in pro["wellcome"]:
                if op.param2 in Bots:
                    pass
                else:
                    ginfo = cl.getGroup(op.param1)
                    cp = cl.getContact(op.param2)
                    cl.sendMessage(op.param1, "halo..  ☛❲" + str(cp.displayName) + "❳☚\nselamat datang di☛❲ " + str(ginfo.name) +"❳☚\n"+ wait["welmsg"])
                    cl.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + cp.pictureStatus) 
#==================[ AUTO KICK MODE ]====================#
        if op.type == 19:
            if op.param1 in pro["autokick"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in org["friend"]:
                    pass
                else:
                    try:
                        if op.param2 not in Bots and op.param2 not in org["friend"]:
                            wait2["blacklist"][op.param2] = True
                            with open('wait2.json','w') as fp:
                                json.dump(wait2, fp, sort_keys=True, indent=4)
                            user = cl.getContact(op.param2)
                            cl.sendMessage(op.param1,"wooi jan main kick!! " + str(user.displayName))
                            try:
                                ka.kickoutFromGroup(op.param1,[op.param2])
                                ka.findAndAddContactsByMid(op.param3)
                                ka.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.findAndAddContactsByMid(op.param3)
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.findAndAddContactsByMid(op.param3)
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param3)
                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.findAndAddContactsByMid(op.param3)
                                                ke.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    k1.acceptGroupInvitation(op.param1)
                                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                                    k1.findAndAddContactsByMid(op.param3)
                                                    k1.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                    X = k1.getGroup(op.param1)
                                                    X.preventedJoinByTicket = False
                                                    k1.updateGroup(X)
                                                    invsend = 0
                                                    Ti = k1.reissueGroupTicket(op.param1)
                                                    cl.acceptGroupInvitationByTicket(msg.to,Ti)
                                                    ka.acceptGroupInvitationByTicket(msg.to,Ti)
                                                    kb.acceptGroupInvitationByTicket(msg.to,Ti)
                                                    kc.acceptGroupInvitationByTicket(msg.to,Ti)
                                                    kd.acceptGroupInvitationByTicket(msg.to,Ti)
                                                    ke.acceptGroupInvitationByTicket(msg.to,Ti)
                                                    Ti = k1.reissueGroupTicket(op.param1)
                                                    k1.leaveGroup(X)
                                                except:
                                                    pass
                        else:
                            pass
                    except:
                        pass

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                else:
                    wait2["blacklist"][op.param2] = True
                    try:
                        k1.acceptGroupInvitation(op.param1)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.findAndAddContactsByMid(op.param3)
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        x = k1.getGroup(op.param1)
                        x.preventedJoinByTicket = False
                        k1.updateGroup(x)
                        invsend = 0
                        Ti = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        kb.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        Ti = k1.reissueGroupTicket(op.param1)
                        k1.leaveGroup(op.param1)
                    except:
                        try:
                            znf = [Smid]
                            ke.inviteIntoGroup(op.param1, znf)
                        except:
                            pass

#=================================#
        if op.type == 19 or op.type == 11 or op.type == 17 or op.type == 13 or op.type == 32:
            if mid in op.param3:
                if op.param2 not in Bots and op.param2 not in org["friend"]:
                    wait2["blacklist"][op.param2] = True
                    with open('wait2.json','w') as fp:
                        json.dump(wait2, fp, sort_keys=True, indent=4)
                    random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                    cl.acceptGroupInvitation(op.param1)
                    random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(K2C).cancelGroupInvitation(op.param1,[op.param3])
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        kb.findAndAddContactsByMid(op.param3)
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        kc.cancelGroupInvitation(op.param1,[op.param3])
                    except:
                       try:
                           kb.kickoutFromGroup(op.param1,[op.param2])
                           kc.findAndAddContactsByMid(op.param3)
                           kc.inviteIntoGroup(op.param1,[op.param3])
                           cl.acceptGroupInvitation(op.param1)
                           kd.cancelGroupInvitation(op.param1,[op.param3])
                       except:
                           try:
                               kc.kickoutFromGroup(op.param1,[op.param2])
                               kd.findAndAddContactsByMid(op.param3)
                               kd.inviteIntoGroup(op.param1,[op.param3])
                               cl.acceptGroupInvitation(op.param1)
                               ke.cancelGroupInvitation(op.param1,[op.param3])
                           except:
                               try:
                                   kd.kickoutFromGroup(op.param1,[op.param2])
                                   ke.findAndAddContactsByMid(op.param3)
                                   ke.inviteIntoGroup(op.param1,[op.param3])
                                   cl.acceptGroupInvitation(op.param1)
                                   ka.cancelGroupInvitation(op.param1,[op.param3])
                               except:
                                   try:
                                       ke.kickoutFromGroup(op.param1,[op.param2])
                                       ka.findAndAddContactsByMid(op.param3)
                                       ka.inviteIntoGroup(op.param1,[op.param3])
                                       cl.acceptGroupInvitation(op.param1)
                                       kb.cancelGroupInvitation(op.param1,[op.param3])
                                   except:
                                       try:
                                           k1.acceptGroupInvitation(op.param1)
                                           k1.kickoutFromGroup(op.param1,[op.param2])
                                           k1.findAndAddContactsByMid(op.param3)
                                           k1.inviteIntoGroup(op.param1,[op.param3])
                                           cl.acceptGroupInvitation(op.param1)
                                           X = k1.getGroup(op.param1)
                                           X.preventedJoinByTicket = False
                                           k1.updateGroup(X)
                                           invsend = 0
                                           Ti = k1.reissueGroupTicket(op.param1)
                                           cl.acceptGroupInvitationByTicket(msg.to,Ti)
                                           ka.acceptGroupInvitationByTicket(msg.to,Ti)
                                           kb.acceptGroupInvitationByTicket(msg.to,Ti)
                                           kc.acceptGroupInvitationByTicket(msg.to,Ti)
                                           kd.acceptGroupInvitationByTicket(msg.to,Ti)
                                           Ti = k1.reissueGroupTicket(op.param1)
                                           k1.leaveGroup(X)
                                       except:
                                           pass
                return
#=================================#
        if op.type == 19 or op.type == 11 or op.type == 17 or op.type == 13 or op.type == 32:
            if Amid in op.param3:
                if op.param2 not in Bots and op.param2 not in org["friend"]:
                    wait2["blacklist"][op.param2] = True
                    with open('wait2.json','w') as fp:
                        json.dump(wait2, fp, sort_keys=True, indent=4)
                    random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                    ka.acceptGroupInvitation(op.param1)
                    random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(K2C).cancelGroupInvitation(op.param1,[op.param2])
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kc.findAndAddContactsByMid(op.param3)
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        ka.acceptGroupInvitation(op.param1)
                        kd.cancelGroupInvitation(op.param1,[op.param3])
                    except:
                       try:
                           kc.kickoutFromGroup(op.param1,[op.param2])
                           kd.findAndAddContactsByMid(op.param3)
                           kd.inviteIntoGroup(op.param1,[op.param3])
                           ka.acceptGroupInvitation(op.param1)
                           ke.cancelGroupInvitation(op.param1,[op.param3])
                       except:
                           try:
                               kd.kickoutFromGroup(op.param1,[op.param2])
                               ke.findAndAddContactsByMid(op.param3)
                               ke.inviteIntoGroup(op.param1,[op.param3])
                               ka.acceptGroupInvitation(op.param1)
                               kb.cancelGroupInvitation(op.param1,[op.param3])
                           except:
                               try:
                                   ke.kickoutFromGroup(op.param1,[op.param2])
                                   kb.findAndAddContactsByMid(op.param3)
                                   kb.inviteIntoGroup(op.param1,[op.param3])
                                   ka.acceptGroupInvitation(op.param1)
                                   kc.cancelGroupInvitation(op.param1,[op.param3])
                               except:
                                   try:
                                       k1.acceptGroupInvitation(op.param1)
                                       k1.kickoutFromGroup(op.param1,[op.param2])
                                       k1.findAndAddContactsByMid(op.param3)
                                       k1.inviteIntoGroup(op.param1,[op.param3])
                                       cl.acceptGroupInvitation(op.param1)
                                       X = k1.getGroup(op.param1)
                                       X.preventedJoinByTicket = False
                                       k1.updateGroup(X)
                                       invsend = 0
                                       Ti = k1.reissueGroupTicket(op.param1)
                                       cl.acceptGroupInvitationByTicket(msg.to,Ti)
                                       ka.acceptGroupInvitationByTicket(msg.to,Ti)
                                       kb.acceptGroupInvitationByTicket(msg.to,Ti)
                                       kc.acceptGroupInvitationByTicket(msg.to,Ti)
                                       kd.acceptGroupInvitationByTicket(msg.to,Ti)
                                       Ti = k1.reissueGroupTicket(op.param1)
                                       k1.leaveGroup(X)
                                   except:
                                       pass
                return
        if op.type == 19 or op.type == 11 or op.type == 17 or op.type == 13 or op.type == 32:
            if Bmid in op.param3:
                if op.param2 not in Bots and op.param2 not in org["friend"]:
                    wait2["blacklist"][op.param2] = True
                    with open('wait2.json','w') as fp:
                        json.dump(wait2, fp, sort_keys=True, indent=4)
                    random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                    kb.acceptGroupInvitation(op.param1)
                    random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(K2C).cancelGroupInvitation(op.param1,[op.param2])
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kd.findAndAddContactsByMid(op.param3)
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                        kd.cancelGroupInvitation(op.param1,[op.param3])
                    except:
                       try:
                           kd.kickoutFromGroup(op.param1,[op.param2])
                           ke.findAndAddContactsByMid(op.param3)
                           ke.inviteIntoGroup(op.param1,[op.param3])
                           kb.acceptGroupInvitation(op.param1)
                           ka.cancelGroupInvitation(op.param1,[op.param3])
                       except:
                           try:
                               ke.kickoutFromGroup(op.param1,[op.param2])
                               ka.findAndAddContactsByMid(op.param3)
                               ka.inviteIntoGroup(op.param1,[op.param3])
                               kb.acceptGroupInvitation(op.param1)
                               ka.cancelGroupInvitation(op.param1,[op.param3])
                           except:
                               try:
                                   ka.kickoutFromGroup(op.param1,[op.param2])
                                   kc.findAndAddContactsByMid(op.param3)
                                   kc.inviteIntoGroup(op.param1,[op.param3])
                                   kb.acceptGroupInvitation(op.param1)
                                   kd.cancelGroupInvitation(op.param1,[op.param3])
                               except:
                                   try:
                                       kd.kickoutFromGroup(op.param1,[op.param2])
                                       kd.findAndAddContactsByMid(op.param3)
                                       kd.inviteIntoGroup(op.param1,[op.param3])
                                       kb.acceptGroupInvitation(op.param1)
                                       kc.cancelGroupInvitation(op.param1,[op.param3])
                                   except:
                                       try:
                                           kc.kickoutFromGroup(op.param1,[op.param2])
                                           kc.findAndAddContactsByMid(op.param3)
                                           kc.inviteIntoGroup(op.param1,[op.param3])
                                           kb.acceptGroupInvitation(op.param1)
                                           ka.cancelGroupInvitation(op.param1,[op.param3])
                                       except:
                                           try:
                                               ka.kickoutFromGroup(op.param1,[op.param2])
                                               ka.findAndAddContactsByMid(op.param3)
                                               ka.inviteIntoGroup(op.param1,[op.param3])
                                               kb.acceptGroupInvitation(op.param1)
                                               kc.cancelGroupInvitation(op.param1,[op.param3])
                                           except:
                                               try:
                                                   kc.kickoutFromGroup(op.param1,[op.param2])
                                                   kc.findAndAddContactsByMid(op.param3)
                                                   kc.inviteIntoGroup(op.param1,[op.param3])
                                                   kb.acceptGroupInvitation(op.param1)
                                                   kd.cancelGroupInvitation(op.param1,[op.param3])
                                               except:
                                                   try:
                                                       kd.kickoutFromGroup(op.param1,[op.param2])
                                                       kd.findAndAddContactsByMid(op.param3)
                                                       kd.inviteIntoGroup(op.param1,[op.param3])
                                                       kb.acceptGroupInvitation(op.param1)
                                                       ke.cancelGroupInvitation(op.param1,[op.param3])
                                                   except:
                                                       try:
                                                           ke.kickoutFromGroup(op.param1,[op.param2])
                                                           ke.findAndAddContactsByMid(op.param3)
                                                           ke.inviteIntoGroup(op.param1,[op.param3])
                                                           kb.acceptGroupInvitation(op.param1)
                                                           ka.cancelGroupInvitation(op.param1,[op.param3])
                                                       except:
                                                           try:
                                                               ka.kickoutFromGroup(op.param1,[op.param2])
                                                               ka.findAndAddContactsByMid(op.param3)
                                                               ka.inviteIntoGroup(op.param1,[op.param3])
                                                               kb.acceptGroupInvitation(op.param1)
                                                               kc.cancelGroupInvitation(op.param1,[op.param3])
                                                           except:
                                                               try:
                                                                   kc.kickoutFromGroup(op.param1,[op.param2])
                                                                   kc.findAndAddContactsByMid(op.param3)
                                                                   kc.inviteIntoGroup(op.param1,[op.param3])
                                                                   kb.acceptGroupInvitation(op.param1)
                                                                   kd.cancelGroupInvitation(op.param1,[op.param3])
                                                               except:
                                                                   try:
                                                                       kd.kickoutFromGroup(op.param1,[op.param2])
                                                                       kd.findAndAddContactsByMid(op.param3)
                                                                       kd.inviteIntoGroup(op.param1,[op.param3])
                                                                       kb.acceptGroupInvitation(op.param1)
                                                                       ke.cancelGroupInvitation(op.param1,[op.param3])
                                                                   except:
                                                                       try:
                                                                           ke.kickoutFromGroup(op.param1,[op.param2])
                                                                           ke.findAndAddContactsByMid(op.param3)
                                                                           ke.inviteIntoGroup(op.param1,[op.param3])
                                                                           kb.acceptGroupInvitation(op.param1)
                                                                           cl.cancelGroupInvitation(op.param1,[op.param3])
                                                                       except:
                                                                           try:
                                                                               cl.kickoutFromGroup(op.param1,[op.param2])
                                                                               cl.findAndAddContactsByMid(op.param3)
                                                                               cl.inviteIntoGroup(op.param1,[op.param3])
                                                                               kb.acceptGroupInvitation(op.param1)
                                                                               kd.cancelGroupInvitation(op.param1,[op.param3])
                                                                           except:
                                                                               try:
                                                                                   k1.acceptGroupInvitation(op.param1)
                                                                                   k1.kickoutFromGroup(op.param1,[op.param2])
                                                                                   k1.findAndAddContactsByMid(op.param3)
                                                                                   k1.inviteIntoGroup(op.param1,[op.param3])
                                                                                   kb.acceptGroupInvitation(op.param1)
                                                                                   X = k1.getGroup(op.param1)
                                                                                   X.preventedJoinByTicket = False
                                                                                   k1.updateGroup(X)
                                                                                   invsend = 0
                                                                                   Ti = k1.reissueGroupTicket(op.param1)
                                                                                   cl.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   ka.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   kb.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   kc.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   kd.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   Ti = k1.reissueGroupTicket(op.param1)
                                                                                   k1.leaveGroup(X)
                                                                               except:
                                                                                   pass
                return

        if op.type == 19 or op.type == 11 or op.type == 17 or op.type == 13 or op.type == 32:
            if Cmid in op.param3:
                if op.param2 not in Bots and op.param2 not in org["friend"]:
                    wait2["blacklist"][op.param2] = True
                    with open('wait2.json','w') as fp:
                        json.dump(wait2, fp, sort_keys=True, indent=4)
                    random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                    kc.acceptGroupInvitation(op.param1)
                    random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(K2C).cancelGroupInvitation(op.param1,[op.param2])
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        ke.findAndAddContactsByMid(op.param3)
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                        ka.cancelGroupInvitation(op.param1,[op.param3])
                    except:
                       try:
                           ke.kickoutFromGroup(op.param1,[op.param2])
                           ka.findAndAddContactsByMid(op.param3)
                           ka.inviteIntoGroup(op.param1,[op.param3])
                           kc.acceptGroupInvitation(op.param1)
                           kb.cancelGroupInvitation(op.param1,[op.param3])
                       except:
                           try:
                               ka.kickoutFromGroup(op.param1,[op.param2])
                               kb.findAndAddContactsByMid(op.param3)
                               kb.inviteIntoGroup(op.param1,[op.param3])
                               kc.acceptGroupInvitation(op.param1)
                               kd.cancelGroupInvitation(op.param1,[op.param3])
                           except:
                               try:
                                   kb.kickoutFromGroup(op.param1,[op.param2])
                                   kd.findAndAddContactsByMid(op.param3)
                                   kd.inviteIntoGroup(op.param1,[op.param3])
                                   kc.acceptGroupInvitation(op.param1)
                                   ke.cancelGroupInvitation(op.param1,[op.param3])
                               except:
                                   try:
                                       ke.kickoutFromGroup(op.param1,[op.param2])
                                       ke.findAndAddContactsByMid(op.param3)
                                       ke.inviteIntoGroup(op.param1,[op.param3])
                                       kc.acceptGroupInvitation(op.param1)
                                       ka.cancelGroupInvitation(op.param1,[op.param3])
                                   except:
                                       try:
                                           ka.kickoutFromGroup(op.param1,[op.param2])
                                           ka.findAndAddContactsByMid(op.param3)
                                           ka.inviteIntoGroup(op.param1,[op.param3])
                                           kc.acceptGroupInvitation(op.param1)
                                           kb.cancelGroupInvitation(op.param1,[op.param3])
                                       except:
                                           try:
                                               kb.kickoutFromGroup(op.param1,[op.param2])
                                               kb.findAndAddContactsByMid(op.param3)
                                               kb.inviteIntoGroup(op.param1,[op.param3])
                                               kc.acceptGroupInvitation(op.param1)
                                               kd.cancelGroupInvitation(op.param1,[op.param3])
                                           except:
                                               try:
                                                   kd.kickoutFromGroup(op.param1,[op.param2])
                                                   kd.findAndAddContactsByMid(op.param3)
                                                   kd.inviteIntoGroup(op.param1,[op.param3])
                                                   kc.acceptGroupInvitation(op.param1)
                                                   ke.cancelGroupInvitation(op.param1,[op.param3])
                                               except:
                                                   try:
                                                       ke.kickoutFromGroup(op.param1,[op.param2])
                                                       ke.findAndAddContactsByMid(op.param3)
                                                       ke.inviteIntoGroup(op.param1,[op.param3])
                                                       kc.acceptGroupInvitation(op.param1)
                                                       ka.cancelGroupInvitation(op.param1,[op.param3])
                                                   except:
                                                       try:
                                                           ka.kickoutFromGroup(op.param1,[op.param2])
                                                           ka.findAndAddContactsByMid(op.param3)
                                                           ka.inviteIntoGroup(op.param1,[op.param3])
                                                           kc.acceptGroupInvitation(op.param1)
                                                           kb.cancelGroupInvitation(op.param1,[op.param3])
                                                       except:
                                                           try:
                                                               kb.kickoutFromGroup(op.param1,[op.param2])
                                                               kb.findAndAddContactsByMid(op.param3)
                                                               kb.inviteIntoGroup(op.param1,[op.param3])
                                                               kc.acceptGroupInvitation(op.param1)
                                                               kd.cancelGroupInvitation(op.param1,[op.param3])
                                                           except:
                                                               try:
                                                                   kd.kickoutFromGroup(op.param1,[op.param2])
                                                                   kd.findAndAddContactsByMid(op.param3)
                                                                   kd.inviteIntoGroup(op.param1,[op.param3])
                                                                   kc.acceptGroupInvitation(op.param1)
                                                                   ke.cancelGroupInvitation(op.param1,[op.param3])
                                                               except:
                                                                   try:
                                                                       ke.kickoutFromGroup(op.param1,[op.param2])
                                                                       ke.findAndAddContactsByMid(op.param3)
                                                                       ke.inviteIntoGroup(op.param1,[op.param3])
                                                                       kc.acceptGroupInvitation(op.param1)
                                                                       ka.cancelGroupInvitation(op.param1,[op.param3])
                                                                   except:
                                                                       try:
                                                                           ka.kickoutFromGroup(op.param1,[op.param2])
                                                                           ka.findAndAddContactsByMid(op.param3)
                                                                           ka.inviteIntoGroup(op.param1,[op.param3])
                                                                           kc.acceptGroupInvitation(op.param1)
                                                                           cl.cancelGroupInvitation(op.param1,[op.param3])
                                                                       except:
                                                                           try:
                                                                               cl.kickoutFromGroup(op.param1,[op.param2])
                                                                               cl.findAndAddContactsByMid(op.param3)
                                                                               cl.inviteIntoGroup(op.param1,[op.param3])
                                                                               kc.acceptGroupInvitation(op.param1)
                                                                               kd.cancelGroupInvitation(op.param1,[op.param3])
                                                                           except:
                                                                               try:
                                                                                   k1.acceptGroupInvitation(op.param1)
                                                                                   k1.kickoutFromGroup(op.param1,[op.param2])
                                                                                   k1.findAndAddContactsByMid(op.param3)
                                                                                   k1.inviteIntoGroup(op.param1,[op.param3])
                                                                                   kc.acceptGroupInvitation(op.param1)
                                                                                   X = k1.getGroup(op.param1)
                                                                                   X.preventedJoinByTicket = False
                                                                                   k1.updateGroup(X)
                                                                                   invsend = 0
                                                                                   Ti = k1.reissueGroupTicket(op.param1)
                                                                                   cl.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   ka.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   kb.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   kc.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   kd.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   Ti = k1.reissueGroupTicket(op.param1)
                                                                                   k1.leaveGroup(X)
                                                                               except:
                                                                                   pass
                return

        if op.type == 19 or op.type == 11 or op.type == 17 or op.type == 13 or op.type == 32:
            if Dmid in op.param3:
                if op.param2 not in Bots and op.param2 not in org["friend"]:
                    wait2["blacklist"][op.param2] = True
                    with open('wait2.json','w') as fp:
                        json.dump(wait2, fp, sort_keys=True, indent=4)
                    random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                    kd.acceptGroupInvitation(op.param1)
                    random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(K2C).cancelGroupInvitation(op.param1,[op.param2])
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ka.findAndAddContactsByMid(op.param3)
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                        kb.cancelGroupInvitation(op.param1,[op.param3])
                    except:
                       try:
                           ka.kickoutFromGroup(op.param1,[op.param2])
                           kb.findAndAddContactsByMid(op.param3)
                           kb.inviteIntoGroup(op.param1,[op.param3])
                           kd.acceptGroupInvitation(op.param1)
                           kc.cancelGroupInvitation(op.param1,[op.param3])
                       except:
                           try:
                               kb.kickoutFromGroup(op.param1,[op.param2])
                               kc.findAndAddContactsByMid(op.param3)
                               kc.inviteIntoGroup(op.param1,[op.param3])
                               kd.acceptGroupInvitation(op.param1)
                               kd.cancelGroupInvitation(op.param1,[op.param3])
                           except:
                               try:
                                   kc.kickoutFromGroup(op.param1,[op.param2])
                                   ke.findAndAddContactsByMid(op.param3)
                                   ke.inviteIntoGroup(op.param1,[op.param3])
                                   kd.acceptGroupInvitation(op.param1)
                                   ka.cancelGroupInvitation(op.param1,[op.param3])
                               except:
                                   try:
                                       ke.kickoutFromGroup(op.param1,[op.param2])
                                       ka.findAndAddContactsByMid(op.param3)
                                       ka.inviteIntoGroup(op.param1,[op.param3])
                                       kd.acceptGroupInvitation(op.param1)
                                       kb.cancelGroupInvitation(op.param1,[op.param3])
                                   except:
                                       try:
                                           ka.kickoutFromGroup(op.param1,[op.param2])
                                           kb.findAndAddContactsByMid(op.param3)
                                           kb.inviteIntoGroup(op.param1,[op.param3])
                                           kd.acceptGroupInvitation(op.param1)
                                           kc.cancelGroupInvitation(op.param1,[op.param3])
                                       except:
                                           try:
                                               kb.kickoutFromGroup(op.param1,[op.param2])
                                               kc.findAndAddContactsByMid(op.param3)
                                               kc.inviteIntoGroup(op.param1,[op.param3])
                                               kd.acceptGroupInvitation(op.param1)
                                               ke.cancelGroupInvitation(op.param1,[op.param3])
                                           except:
                                               try:
                                                   ke.kickoutFromGroup(op.param1,[op.param2])
                                                   ke.findAndAddContactsByMid(op.param3)
                                                   ke.inviteIntoGroup(op.param1,[op.param3])
                                                   kd.acceptGroupInvitation(op.param1)
                                                   ka.cancelGroupInvitation(op.param1,[op.param3])
                                               except:
                                                   try:
                                                       ka.kickoutFromGroup(op.param1,[op.param2])
                                                       ka.findAndAddContactsByMid(op.param3)
                                                       ka.inviteIntoGroup(op.param1,[op.param3])
                                                       kd.acceptGroupInvitation(op.param1)
                                                       kb.cancelGroupInvitation(op.param1,[op.param3])
                                                   except:
                                                       try:
                                                           kb.kickoutFromGroup(op.param1,[op.param2])
                                                           kb.findAndAddContactsByMid(op.param3)
                                                           kb.inviteIntoGroup(op.param1,[op.param3])
                                                           kd.acceptGroupInvitation(op.param1)
                                                           kc.cancelGroupInvitation(op.param1,[op.param3])
                                                       except:
                                                           try:
                                                               kc.kickoutFromGroup(op.param1,[op.param2])
                                                               kc.findAndAddContactsByMid(op.param3)
                                                               kc.inviteIntoGroup(op.param1,[op.param3])
                                                               kd.acceptGroupInvitation(op.param1)
                                                               ke.cancelGroupInvitation(op.param1,[op.param2])
                                                           except:
                                                               try:
                                                                   ke.kickoutFromGroup(op.param1,[op.param2])
                                                                   ke.findAndAddContactsByMid(op.param3)
                                                                   ke.inviteIntoGroup(op.param1,[op.param3])
                                                                   kd.acceptGroupInvitation(op.param1)
                                                                   ka.cancelGroupInvitation(op.param1,[op.param3])
                                                               except:
                                                                   try:
                                                                       ka.kickoutFromGroup(op.param1,[op.param2])
                                                                       ka.findAndAddContactsByMid(op.param3)
                                                                       ka.inviteIntoGroup(op.param1,[op.param3])
                                                                       kd.acceptGroupInvitation(op.param1)
                                                                       kb.cancelGroupInvitation(op.param1,[op.param3])
                                                                   except:
                                                                       try:
                                                                           kb.kickoutFromGroup(op.param1,[op.param2])
                                                                           kb.findAndAddContactsByMid(op.param3)
                                                                           kb.inviteIntoGroup(op.param1,[op.param3])
                                                                           kd.acceptGroupInvitation(op.param1)
                                                                           cl.cancelGroupInvitation(op.param1,[op.param3])
                                                                       except:
                                                                           try:
                                                                               cl.kickoutFromGroup(op.param1,[op.param2])
                                                                               cl.findAndAddContactsByMid(op.param3)
                                                                               cl.inviteIntoGroup(op.param1,[op.param3])
                                                                               kd.acceptGroupInvitation(op.param1)
                                                                               ka.cancelGroupInvitation(op.param1,[op.param3])
                                                                           except:
                                                                               try:
                                                                                   k1.acceptGroupInvitation(op.param1)
                                                                                   k1.kickoutFromGroup(op.param1,[op.param2])
                                                                                   k1.findAndAddContactsByMid(op.param3)
                                                                                   k1.inviteIntoGroup(op.param1,[op.param3])
                                                                                   kd.acceptGroupInvitation(op.param1)
                                                                                   X = k1.getGroup(op.param1)
                                                                                   X.preventedJoinByTicket = False
                                                                                   k1.updateGroup(X)
                                                                                   invsend = 0
                                                                                   Ti = k1.reissueGroupTicket(op.param1)
                                                                                   cl.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   ka.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   kb.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   kc.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   kd.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   Ti = k1.reissueGroupTicket(op.param1)
                                                                                   k1.leaveGroup(X)
                                                                               except:
                                                                                   pass
                return

        if op.type == 19 or op.type == 11 or op.type == 17 or op.type == 13 or op.type == 32:
            if Emid in op.param3:
                if op.param2 not in Bots and op.param2 not in org["friend"]:
                    wait2["blacklist"][op.param2] = True
                    with open('wait2.json','w') as fp:
                        json.dump(wait2, fp, sort_keys=True, indent=4)
                    random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                    kd.acceptGroupInvitation(op.param1)
                    random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(K2C).cancelGroupInvitation(op.param1,[op.param2])
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        kb.findAndAddContactsByMid(op.param3)
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                        kc.cancelGroupInvitation(op.param1,[op.param3])
                    except:
                       try:
                           kb.kickoutFromGroup(op.param1,[op.param2])
                           kc.findAndAddContactsByMid(op.param3)
                           kc.inviteIntoGroup(op.param1,[op.param3])
                           ke.acceptGroupInvitation(op.param1)
                           kd.cancelGroupInvitation(op.param1,[op.param3])
                       except:
                           try:
                               kc.kickoutFromGroup(op.param1,[op.param2])
                               kd.findAndAddContactsByMid(op.param3)
                               kd.inviteIntoGroup(op.param1,[op.param3])
                               ke.acceptGroupInvitation(op.param1)
                               kd.cancelGroupInvitation(op.param1,[op.param3])
                           except:
                               try:
                                   kd.kickoutFromGroup(op.param1,[op.param2])
                                   kd.findAndAddContactsByMid(op.param3)
                                   kd.inviteIntoGroup(op.param1,[op.param3])
                                   ke.acceptGroupInvitation(op.param1)
                                   ka.cancelGroupInvitation(op.param1,[op.param3])
                               except:
                                   try:
                                       ka.kickoutFromGroup(op.param1,[op.param2])
                                       ka.findAndAddContactsByMid(op.param3)
                                       ka.inviteIntoGroup(op.param1,[op.param3])
                                       ke.acceptGroupInvitation(op.param1)
                                       kb.cancelGroupInvitation(op.param1,[op.param3])
                                   except:
                                       try:
                                           kb.kickoutFromGroup(op.param1,[op.param2])
                                           kb.findAndAddContactsByMid(op.param3)
                                           kb.inviteIntoGroup(op.param1,[op.param3])
                                           ke.acceptGroupInvitation(op.param1)
                                           kc.cancelGroupInvitation(op.param1,[op.param3])
                                       except:
                                           try:
                                               kc.kickoutFromGroup(op.param1,[op.param2])
                                               kc.findAndAddContactsByMid(op.param3)
                                               kc.inviteIntoGroup(op.param1,[op.param3])
                                               ke.acceptGroupInvitation(op.param1)
                                               kd.cancelGroupInvitation(op.param1,[op.param3])
                                           except:
                                               try:
                                                   kd.kickoutFromGroup(op.param1,[op.param2])
                                                   kd.findAndAddContactsByMid(op.param3)
                                                   kd.inviteIntoGroup(op.param1,[op.param3])
                                                   ke.acceptGroupInvitation(op.param1)
                                                   ka.cancelGroupInvitation(op.param1,[op.param3])
                                               except:
                                                   try:
                                                       ka.kickoutFromGroup(op.param1,[op.param2])
                                                       ka.findAndAddContactsByMid(op.param3)
                                                       ka.inviteIntoGroup(op.param1,[op.param3])
                                                       ke.acceptGroupInvitation(op.param1)
                                                       kb.cancelGroupInvitation(op.param1,[op.param3])
                                                   except:
                                                       try:
                                                           kb.kickoutFromGroup(op.param1,[op.param2])
                                                           kb.findAndAddContactsByMid(op.param3)
                                                           kb.inviteIntoGroup(op.param1,[op.param3])
                                                           ke.acceptGroupInvitation(op.param1)
                                                           kc.cancelGroupInvitation(op.param1,[op.param3])
                                                       except:
                                                           try:
                                                               kc.kickoutFromGroup(op.param1,[op.param2])
                                                               kc.findAndAddContactsByMid(op.param3)
                                                               kc.inviteIntoGroup(op.param1,[op.param3])
                                                               ke.acceptGroupInvitation(op.param1)
                                                               kd.cancelGroupInvitation(op.param1,[op.param3])
                                                           except:
                                                               try:
                                                                   kd.kickoutFromGroup(op.param1,[op.param2])
                                                                   kd.findAndAddContactsByMid(op.param3)
                                                                   kd.inviteIntoGroup(op.param1,[op.param3])
                                                                   ke.acceptGroupInvitation(op.param1)
                                                                   ka.cancelGroupInvitation(op.param1,[op.param3])
                                                               except:
                                                                   try:
                                                                       ka.kickoutFromGroup(op.param1,[op.param2])
                                                                       ka.findAndAddContactsByMid(op.param3)
                                                                       ka.inviteIntoGroup(op.param1,[op.param3])
                                                                       ke.acceptGroupInvitation(op.param1)
                                                                       kb.cancelGroupInvitation(op.param1,[op.param3])
                                                                   except:
                                                                       try:
                                                                           kb.kickoutFromGroup(op.param1,[op.param2])
                                                                           kb.findAndAddContactsByMid(op.param3)
                                                                           kb.inviteIntoGroup(op.param1,[op.param3])
                                                                           ke.acceptGroupInvitation(op.param1)
                                                                           cl.cancelGroupInvitation(op.param1,[op.param3])
                                                                       except:
                                                                           try:
                                                                               cl.kickoutFromGroup(op.param1,[op.param2])
                                                                               cl.findAndAddContactsByMid(op.param3)
                                                                               cl.inviteIntoGroup(op.param1,[op.param3])
                                                                               ke.acceptGroupInvitation(op.param1)
                                                                               ka.cancelGroupInvitation(op.param1,[op.param3])
                                                                           except:
                                                                               try:
                                                                                   k1.acceptGroupInvitation(op.param1)
                                                                                   k1.kickoutFromGroup(op.param1,[op.param2])
                                                                                   k1.findAndAddContactsByMid(op.param3)
                                                                                   k1.inviteIntoGroup(op.param1,[op.param3])
                                                                                   ke.acceptGroupInvitation(op.param1)
                                                                                   X = k1.getGroup(op.param1)
                                                                                   X.preventedJoinByTicket = False
                                                                                   k1.updateGroup(X)
                                                                                   invsend = 0
                                                                                   Ti = k1.reissueGroupTicket(op.param1)
                                                                                   cl.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   ka.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   kb.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   kc.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   kd.acceptGroupInvitationByTicket(msg.to,Ti)
                                                                                   Ti = k1.reissueGroupTicket(op.param1)
                                                                                   k1.leaveGroup(X)
                                                                               except:
                                                                                   pass
                return

        if op.type == 19 or op.type == 11 or op.type == 17 or op.type == 13 or op.type == 32:
            if Smid in op.param3:
                if op.param2 not in Bots and op.param2 not in org["friend"]:
                    wait2["blacklist"][op.param2] = True
                    with open('wait2.json','w') as fp:
                        json.dump(wait2, fp, sort_keys=True, indent=4)
                    user = random.choice(K2C).getContact(op.param2)
                    random.choice(K2C).sendMessage(op.param1,"kehed.. " + str(user.displayName))
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kc.findAndAddContactsByMid(op.param3)
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kd.cancelGroupInvitation(op.param1,[op.param3])
                    except:
                       try:
                           kc.kickoutFromGroup(op.param1,[op.param2])
                           kd.findAndAddContactsByMid(op.param3)
                           kd.inviteIntoGroup(op.param1,[op.param3])
                           ke.cancelGroupInvitation(op.param1,[op.param3])
                       except:
                           try:
                               kd.kickoutFromGroup(op.param1,[op.param2])
                               ke.findAndAddContactsByMid(op.param3)
                               ke.inviteIntoGroup(op.param1,[op.param3])
                               ka.cancelGroupInvitation(op.param1,[op.param3])
                           except:
                               try:
                                   ke.kickoutFromGroup(op.param1,[op.param2])
                                   ka.findAndAddContactsByMid(op.param3)
                                   ka.inviteIntoGroup(op.param1,[op.param3])
                                   kb.cancelGroupInvitation(op.param1,[op.param3])
                               except:
                                   try:
                                       ka.kickoutFromGroup(op.param1,[op.param2])
                                       kb.findAndAddContactsByMid(op.param3)
                                       kb.inviteIntoGroup(op.param1,[op.param3])
                                       kc.cancelGroupInvitation(op.param1,[op.param3])
                                   except:
                                       try:
                                           kb.kickoutFromGroup(op.param1,[op.param2])
                                           kc.findAndAddContactsByMid(op.param3)
                                           kc.inviteIntoGroup(op.param1,[op.param3])
                                           kd.cancelGroupInvitation(op.param1,[op.param3])
                                       except:
                                           try:
                                               kc.kickoutFromGroup(op.param1,[op.param2])
                                               kd.findAndAddContactsByMid(op.param3)
                                               kd.inviteIntoGroup(op.param1,[op.param3])
                                               ke.cancelGroupInvitation(op.param1,[op.param3])
                                           except:
                                               try:
                                                   kd.kickoutFromGroup(op.param1,[op.param2])
                                                   ke.findAndAddContactsByMid(op.param3)
                                                   ke.inviteIntoGroup(op.param1,[op.param3])
                                                   ka.cancelGroupInvitation(op.param1,[op.param3])
                                               except:
                                                   try:
                                                       ke.kickoutFromGroup(op.param1,[op.param2])
                                                       ka.findAndAddContactsByMid(op.param3)
                                                       ka.inviteIntoGroup(op.param1,[op.param3])
                                                       kb.cancelGroupInvitation(op.param1,[op.param3])
                                                   except:
                                                       try:
                                                           ka.kickoutFromGroup(op.param1,[op.param2])
                                                           kb.findAndAddContactsByMid(op.param3)
                                                           kb.inviteIntoGroup(op.param1,[op.param3])
                                                           kc.cancelGroupInvitation(op.param1,[op.param3])
                                                       except:
                                                           try:
                                                               kb.kickoutFromGroup(op.param1,[op.param2])
                                                               kc.findAndAddContactsByMid(op.param3)
                                                               kc.inviteIntoGroup(op.param1,[op.param3])
                                                               kd.cancelGroupInvitation(op.param1,[op.param3])
                                                           except:
                                                               try:
                                                                   kc.kickoutFromGroup(op.param1,[op.param2])
                                                                   kd.findAndAddContactsByMid(op.param3)
                                                                   kd.inviteIntoGroup(op.param1,[op.param3])
                                                                   ke.cancelGroupInvitation(op.param1,[op.param3])
                                                               except:
                                                                   try:
                                                                       kd.kickoutFromGroup(op.param1,[op.param2])
                                                                       ke.findAndAddContactsByMid(op.param3)
                                                                       ke.inviteIntoGroup(op.param1,[op.param3])
                                                                       ka.cancelGroupInvitation(op.param1,[op.param3])
                                                                   except:
                                                                       try:
                                                                           ke.kickoutFromGroup(op.param1,[op.param2])
                                                                           ka.findAndAddContactsByMid(op.param3)
                                                                           ka.inviteIntoGroup(op.param1,[op.param3])
                                                                           kb.cancelGroupInvitation(op.param1,[op.param3])
                                                                       except:
                                                                           pass
                return

#=================================#
        if op.type == 19 or op.type == 11 or op.type == 17 or op.type == 13 or op.type == 32:
            if org["friend"] in op.param3:
                if op.param2 in Bots:
                    pass
                elif op.param2 in org["friend"]:
                    pass
                else:
                    wait2["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.findAndAddContactsByMid(op.param3)
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        kc.cancelGroupInvitation(op.param1,[op.param3])
                    except:
                       try:
                           kc.kickoutFromGroup(op.param1,[op.param2])
                           kc.findAndAddContactsByMid(op.param3)
                           kc.inviteIntoGroup(op.param1,[op.param3])
                           kd.cancelGroupInvitation(op.param1,[op.param3])
                       except:
                           try:
                               kd.kickoutFromGroup(op.param1,[op.param2])
                               kd.findAndAddContactsByMid(op.param3)
                               kd.inviteIntoGroup(op.param1,[op.param3])
                               ka.cancelGroupInvitation(op.param1,[op.param3])
                           except:
                               try:
                                   ke.kickoutFromGroup(op.param1,[op.param2])
                                   ke.findAndAddContactsByMid(op.param3)
                                   ke.inviteIntoGroup(op.param1,[op.param3])
                                   ka.cancelGroupInvitation(op.param1,[op.param3])
                               except:
                                   try:
                                       ka.kickoutFromGroup(op.param1,[op.param2])
                                       ka.findAndAddContactsByMid(op.param3)
                                       ka.inviteIntoGroup(op.param1,[op.param3])
                                       kb.cancelGroupInvitation(op.param1,[op.param3])
                                   except:
                                       try:
                                           kb.kickoutFromGroup(op.param1,[op.param2])
                                           kb.findAndAddContactsByMid(op.param3)
                                           kb.inviteIntoGroup(op.param1,[op.param3])
                                           kc.cancelGroupInvitation(op.param1,[op.param3])
                                       except:
                                           try:
                                               kc.kickoutFromGroup(op.param1,[op.param2])
                                               kc.findAndAddContactsByMid(op.param3)
                                               kc.inviteIntoGroup(op.param1,[op.param3])
                                               kd.cancelGroupInvitation(op.param1,[op.param3])
                                           except:
                                               try:
                                                   kd.kickoutFromGroup(op.param1,[op.param2])
                                                   kd.findAndAddContactsByMid(op.param3)
                                                   kd.inviteIntoGroup(op.param1,[op.param3])
                                                   ke.cancelGroupInvitation(op.param1,[op.param3])
                                               except:
                                                   try:
                                                       ke.kickoutFromGroup(op.param1,[op.param2])
                                                       ke.findAndAddContactsByMid(op.param3)
                                                       ke.inviteIntoGroup(op.param1,[op.param3])
                                                       ka.cancelGroupInvitation(op.param1,[op.param3])
                                                   except:
                                                       try:
                                                           ka.kickoutFromGroup(op.param1,[op.param2])
                                                           ka.findAndAddContactsByMid(op.param3)
                                                           ka.inviteIntoGroup(op.param1,[op.param3])
                                                           kb.cancelGroupInvitation(op.param1,[op.param3])
                                                       except:
                                                           try:
                                                               kb.kickoutFromGroup(op.param1,[op.param2])
                                                               kb.findAndAddContactsByMid(op.param3)
                                                               kb.inviteIntoGroup(op.param1,[op.param3])
                                                               kc.cancelGroupInvitation(op.param1,[op.param3])
                                                           except:
                                                               try:
                                                                   kc.kickoutFromGroup(op.param1,[op.param2])
                                                                   kc.findAndAddContactsByMid(op.param3)
                                                                   kc.inviteIntoGroup(op.param1,[op.param3])
                                                                   kd.cancelGroupInvitation(op.param1,[op.param3])
                                                               except:
                                                                   try:
                                                                       kd.kickoutFromGroup(op.param1,[op.param2])
                                                                       kd.findAndAddContactsByMid(op.param3)
                                                                       kd.inviteIntoGroup(op.param1,[op.param3])
                                                                       ke.cancelGroupInvitation(op.param1,[op.param3])
                                                                   except:
                                                                       try:
                                                                           ke.kickoutFromGroup(op.param1,[op.param2])
                                                                           ke.findAndAddContactsByMid(op.param3)
                                                                           ke.inviteIntoGroup(op.param1,[op.param3])
                                                                           kb.cancelGroupInvitation(op.param1,[op.param3])
                                                                       except:
                                                                           pass
                return

        if op.type == 19:
            if op.param3 in Bots and op.param3 in org["friend"]:
                random.choice(K2C).findAndAddContactsByMid(op.param3)
                random.choice(K2C).inviteIntoGroup(op.param1,[op.param3])
                if op.param2 not in Bots and op.param2 not in org["friend"]:
                    wait2["blacklist"][op.param2] = True
                    with open('wait2.json','w') as fp:
                        json.dump(wait2, fp, sort_keys=True, indent=4)
                    random.choice(K2C).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 32:
            if op.param1 in pro["Protectcancl"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in org["friend"]:
                    pass
                else:
                    try:
                        if op.param2 not in Bots and op.param2 not in org["friend"]:
                            wait2["blacklist"][op.param2] = True
                            with open('wait2.json','w') as fp:
                                json.dump(wait2, fp, sort_keys=True, indent=4)
                            user = cl.getContact(op.param2)
                            ka.sendMessage(op.param1,"jangan di cancel wooii!! " + str(user.displayName))
                            try:
                                if op.param3 not in wait2["blacklist"]:
                                    ke.findAndAddContactsByMid(op.param3)
                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait2["blacklist"]:
                                        kd.findAndAddContactsByMid(op.param3)
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait2["blacklist"]:
                                            kc.findAndAddContactsByMid(op.param3)
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait2["blacklist"]:
                                                kb.findAndAddContactsByMid(op.param3)
                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in wait2["blacklist"]:
                                                    ka.findAndAddContactsByMid(op.param3)
                                                    ka.inviteIntoGroup(op.param1,[op.param3])
                                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                pass
                        else:
                            pass
                    except:
                        pass

#=================================#
        if op.type == 25:
            print ("[25] OP MSSG")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 and msg.toType == 2:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if msg.text in ["Help"]:
                    cl.sendMessage(to,helpMessage)

                elif msg.text in ["Help sett"]:
                    cl.sendMessage(to,helpSetting)

                elif msg.text in ["My id"]:
                    cl.sendMessage(to,mid)

                elif msg.text in ["Ginfo"]:
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://cl.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔═════[ Group Info ]═══════"
                    ret_ += "\n╠ ☛ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ☛ ID Group : {}".format(group.id)
                    ret_ += "\n╠ ☛ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ ☛ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ ☛ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ ☛ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ ☛ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══════════════════════════"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)

                elif msg.text in ["Me"]:
                    me = cl.getContact(mid)
                    cl.sendMessage(msg.to,"╔══════════════\n║" + me.displayName + "\n╚══════════════")
                    cl.sendContact(msg.to,mid)

                elif msg.text in ["Gcreator"]:
                  if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    cl.sendContact(to, gCreator)
                    cl.sendMessage(to,"╔══════════════\n╠☛ dia creator grup ini\n╚══════════════")

                elif msg.text in ["Gurl"]:
                    if msg.toType == 2:
                        x = cl.getGroup(msg.to)
                        if x.preventedJoinByTicket == True:
                            cl.sendText(receiver,"╔══════════════\n╠☛ buka dulu qr nya boss\n╚══════════════")
                        elif x.preventedJoinByTicket == False:
                            cl.updateGroup(x)
                            gurl = cl.reissueGroupTicket(msg.to)
                            cl.sendText(receiver,"line://ti/g/" + gurl)
                        else:
                            pass

                elif msg.text in ["Ourl"]:
                    X = cl.getGroup(msg.to)
                    if X.preventedJoinByTicket == False:
                        cl.sendText(receiver,"╔══════════════\n╠☛ qr sudah terbuka boss\n╚══════════════")
                    else:
                        X.preventedJoinByTicket = False
                        cl.updateGroup(X)
                        cl.sendText(receiver,"╔══════════════\n╠☛ done boss\n╚══════════════")
                        print ("qr opened")

                elif msg.text in ["Curl"]:
                    X = cl.getGroup(msg.to)
                    if X.preventedJoinByTicket == True:
                        cl.sendText(receiver,"╔══════════════\n╠☛ qr sudah tertutup boss\n╚══════════════")
                    else:
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                        cl.sendText(receiver,"╔══════════════\n╠☛ done boss\n╚══════════════")
                        print ("qr closed")

                elif "Gname: " in msg.text:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gname: ","")
                        cl.updateGroup(X)

                elif msg.text in ["/reject"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                        cl.rejectGroupInvitation(i)
                        cl.rejectGroupInvitation(i)
                        cl.rejectGroupInvitation(i)
                        cl.rejectGroupInvitation(i)
                        cl.rejectGroupInvitation(i)
                        cl.sendMessage(to,"done reject")

                elif msg.text in ["/reject all"]:
                    gid = ka.getGroupIdsInvited()
                    gid = kb.getGroupIdsInvited()
                    gid = kc.getGroupIdsInvited()
                    gid = kd.getGroupIdsInvited()
                    gid = ke.getGroupIdsInvited()
                    gid = k1.getGroupIdsInvited()
                    for i in gid:
                        try:
                            ka.rejectGroupInvitation(i)
                            kb.rejectGroupInvitation(i)
                            kc.rejectGroupInvitation(i)
                            kd.rejectGroupInvitation(i)
                            ke.rejectGroupInvitation(i)
                            k1.rejectGroupInvitation(i)
                            ka.sendMessage(to,"done reject")
                        except:
                            ka.sendMessage(to,"╔══════════════\n╠☛ tidak ada invitan group\n╚══════════════")

                elif "Broadcast: " in msg.text:
                    bc = msg.text.replace("Broadcast: ","")
                    gid = cl.getGroupIdsJoined()
                    for i in gid:
                            cl.sendMessage(i, bc)
                            cl.sendMessage(to,"done boss")
                            print ("BC done")

                elif msg.text in ["Sticker on"]:
                    wait["sticker"] = True
                    cl.sendMessage(to,"Allready on")

                elif msg.text in ["Sticker off"]:
                    wait["sticker"] = False
                    cl.sendMessage(to,"Allready off")

                elif "Yt: " in msg.text:
                    query = msg.text.replace("Yt: ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                        cl.sendMessage(to,hasil)

                elif "Mid @" in msg.text:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                cl.sendMessage(to,str(mention['M']))
                            except Exception as e:
                                pass

                elif "Contact @" in msg.text:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)

                elif "Cover @" in msg.text:
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(to, str(path))

                elif "Dp @" in msg.text:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                profile = cl.getContact(mention['M'])
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+profile.pictureStatus)
                            except Exception as e:
                                pass

                elif "Info @" in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cl.sendMessage(to,"╔══════════════\n╠☛ Name :"+ contact.displayName + "\n╚══════════════" )
                        cl.sendMessage(to,"╔══════════════\n╠☛ Status :"+ contact.statusMessage + "\n╚══════════════" )
                        cl.sendImageWithURL(msg.to,image)
                    except:
                        pass

                elif "Bio @" in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(key1)
                    try:
                        cl.sendMessage(to,contact.statusMessage)
                    except:
                        cl.sendMessage(to,"bio empty")

                elif "Gpict" in msg.text:
                        group = cl.getGroup(msg.to)
                        path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                        cl.sendImageWithURL(msg.to,path)

                elif "iginfo" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(wait["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ Total Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            cl.sendImageWithURL(to, str(path))
                            cl.sendMessage(to, str(ret_))
                        except:
                            cl.sendMessage(to, "Pengguna tidak ditemukan")

                elif "igpost" in msg.text.lower():
                    separate = msg.text.split(" ")
                    user = msg.text.replace(separate[0] + " ","")
                    profile = "https://www.instagram.com/" + user
                    with requests.session() as x:
                        x.headers['user-agent'] = 'Mozilla/5.0'
                        end_cursor = ''
                        for count in range(1, 999):
                            print('PAGE: ', count)
                            r = x.get(profile, params={'max_id': end_cursor})
                            data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                            j    = json.loads(data)
                            for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                if node['is_video']:
                                    page = 'https://www.instagram.com/p/' + node['code']
                                    r = x.get(page)
                                    url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                    print(url)
                                    cl.sendVideoWithURL(msg.to,url)
                                else:
                                    print (node['display_src'])
                                    cl.sendImageWithURL(msg.to,node['display_src'])
                            end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)

                elif "simage" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(wait["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            cl.sendImageWithURL(to, str(path))

                elif "Fancy text: " in msg.text:
                    txt = msg.text.replace("Fancy text: ", "")
                    t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                    t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                    cl.sendMessage(to, t1 + txt + t2)

                elif "Ig " in msg.text:
                    try:
                        instagram = msg.text.lower().replace("Ig ","")
                        html = requests.get('https://www.instagram.com/' + instagram + '/?')
                        soup = BeautifulSoup(html.text, 'html5lib')
                        data = soup.find_all('meta', attrs={'property':'og:description'})
                        text = data[0].get('content').split()
                        data1 = soup.find_all('meta', attrs={'property':'og:image'})
                        text1 = data1[0].get('content').split()
                        user = "Name: " + text[-2] + "\n"
                        user1 = "Username: " + text[-1] + "\n"
                        followers = "Followers: " + text[0] + "\n"
                        following = "Following: " + text[2] + "\n"
                        post = "Post: " + text[4] + "\n"
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        detail = "========INSTAGRAM INFO USER========\n"
                        details = "\n========INSTAGRAM INFO USER========"
                        cl.sendMessage(to, detail + user + user1 + followers + following + post + link + details)
                        cl.sendImageWithURL(msg.to, text1[0])
                    except Exception as njer:
                    	cl.sendMessage(to, str(njer))

                elif "Say: " in msg.text:
                    bctxt = msg.text.replace("Say: ","")
                    ka.sendMessage(to,(bctxt))
                    kb.sendMessage(to,(bctxt))
                    kc.sendMessage(to,(bctxt))
                    kd.sendMessage(to,(bctxt))
                    ke.sendMessage(to,(bctxt))

                elif "Zodiak " in msg.text:
                    tanggal = msg.text.replace("Zodiak ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    lahir = data["data"]["lahir"]
                    usia = data["data"]["usia"]
                    ultah = data["data"]["ultah"]
                    zodiak = data["data"]["zodiak"]
                    cl.sendMessage(to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)

                elif "Wiki: " in msg.text:
                    try:
                        wiki = msg.text.lower().replace("Wiki: ","")
                        wikipedia.set_lang("id")
                        pesan="Title ("
                        pesan+=wikipedia.page(wiki).title
                        pesan+=")\n\n"
                        pesan+=wikipedia.summary(wiki, sentences=1)
                        pesan+="\n"
                        pesan+=wikipedia.page(wiki).url
                        cl.sendMessage(to, pesan)
                    except:
                            try:
                                pesan="Over Text Limit! Please Click link\n"
                                pesan+=wikipedia.page(wiki).url
                                cl.sendMessage(to, pesan)
                            except Exception as e:
                                cl.sendMessage(to, str(e))

                elif "Vn: " in msg.text:
                    say = msg.text.replace("Vn: ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.m4a")
                    cl.sendAudio(to,"hasil.m4a")

                elif "Vn-en: " in msg.text:
                    say = msg.text.replace("Vn-en: ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.m4a")
                    cl.sendAudio(to,"hasil.m4a")
#-------------------------------------------------------------------
                elif msg.text in ["/reboot"]:
                        print ("[Command]Like executed")
                        try:
                            cl.sendMessage(to,"restart...")
                            restart_program()
                        except:
                            cl.sendMessage(to,"☛tunggu..\n☛sabar..")
                            restart_program()
                            pass

                elif msg.text in ["Botname"]:
                    profile = ka.getProfile()
                    text = profile.displayName + ""
                    ka.sendMessage(to, text)
                    time.sleep(0.15)
                    profile = kb.getProfile()
                    text = profile.displayName + ""
                    kb.sendMessage(to, text)
                    time.sleep(0.15)
                    profile = kc.getProfile()
                    text = profile.displayName + ""
                    kc.sendMessage(to, text)
                    time.sleep(0.15)
                    profile = kd.getProfile()
                    text = profile.displayName + ""
                    kd.sendMessage(to, text)
                    time.sleep(0.15)
                    profile = ke.getProfile()
                    text = profile.displayName + ""
                    ke.sendMessage(to, text)
                    time.sleep(0.15)
                    ka.sendMessage(to,"☛done boss.")

                elif msg.text in ["/bot"]:
                        ka.sendContact(to, Amid)
                        time.sleep(0.15)
                        kb.sendContact(to, Bmid)
                        time.sleep(0.15)
                        kc.sendContact(to, Cmid)
                        time.sleep(0.15)
                        kd.sendContact(to, Dmid)
                        time.sleep(0.15)
                        ke.sendContact(to, Emid)
                        print ("ok")

                elif msg.text in ["Respon"]:
                    ka.sendMessage(to,"stay bosqu")
                    kb.sendMessage(to,"stay bosqu")
                    kc.sendMessage(to,"stay bosqu")
                    kd.sendMessage(to,"stay bosqu")
                    ke.sendMessage(to,"stay bosqu")

                elif msg.text in [".sp"]:
                        start = time.time()
                        ka.sendMessage("ub4324e1584145571d7e1b566bbfcf6bd", '.')
                        elapsed_time = time.time() - start
                        ka.sendMessage(msg.to, "%s second" % (elapsed_time))

                        start2 = time.time()
                        kb.sendMessage("ub4324e1584145571d7e1b566bbfcf6bd", '.')
                        elapsed_time = time.time() - start2
                        kb.sendMessage(msg.to, "%s second" % (elapsed_time))

                        start3 = time.time()
                        kc.sendMessage("ub4324e1584145571d7e1b566bbfcf6bd", '.')
                        elapsed_time = time.time() - start3
                        kc.sendMessage(msg.to, "%s second" % (elapsed_time))

                        start4 = time.time()
                        kd.sendMessage("ub4324e1584145571d7e1b566bbfcf6bd", '.')
                        elapsed_time = time.time() - start4
                        kd.sendMessage(msg.to, "%s second" % (elapsed_time))

                        start5 = time.time()
                        ke.sendMessage("ub4324e1584145571d7e1b566bbfcf6bd", '.')
                        elapsed_time = time.time() - start5
                        ke.sendMessage(msg.to, "%s second" % (elapsed_time))

                elif msg.text in ["Sp"]:
                    start = time.time()
                    cl.sendMessage(to, "••••")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to, "%ss" % (elapsed_time))

                elif msg.text in ["/bot:restart"]:
                        cl.sendMessage(to, "╔══════════════\n╠☛ restart succsess\n╚══════════════")
                        restart_program()
                        print ("@Restart")

                elif msg.text in ["Time"]:
                    timeNow = datetime.now()
                    timeHours = datetime.strftime(timeNow,"(%H:%M)")
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    inihari = datetime.today()
                    hr = inihari.strftime('%A')
                    bln = inihari.strftime('%m')
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                    cl.sendMessage(to, rst)

                elif msg.text in ["Runtime"]:
                    eltime = time.time() - mulai
                    van = "╔═══════════════════\n╠☛ Bot was run "+ waktu(eltime) + "\n╚═══════════════════"
                    cl.sendMessage(to,van)

                elif msg.text in ["Kalender"]:
                    wait2['setTime'][msg.to] = datetime.today().strftime('TANGGAL : %Y-%m-%d \nHARI : %A \nJAM : %H:%M:%S')
                    cl.sendMessage(to, "         KALENDER\n\n" + (wait2['setTime'][msg.to]))
#---------------------------------------------------------
                elif msg.text in ["Post on"]:
                    wait["timeline"]=True
                    cl.sendMessage(to,"╔══════════════\n╠☛ done active\n╚══════════════")
                    print ("Get post on")
                elif msg.text in ["Post off"]:
                    wait["timeline"]=False
                    cl.sendMessage(to,"╔══════════════\n╠☛ done off\n╚══════════════")
                    print ("Get post off")
                elif msg.text in ["Like on"]:
                    wait["likeOn"]=True
                    cl.sendMessage(to,"╔══════════════\n╠☛ done active\n╚══════════════")
                elif msg.text in ["Like off"]:
                    wait["likeOn"]=False
                    cl.sendMessage(to,"╔══════════════\n╠☛ done off\n╚══════════════")
                elif msg.text in ["Coment on"]:
                    wait["commentOn"]=True
                    cl.sendMessage(to,"╔══════════════\n╠☛ done active\n╚══════════════")
                elif msg.text in ["Coment off"]:
                    wait["commentOn"]=False
                    cl.sendMessage(to,"╔══════════════\n╠☛ done off\n╚══════════════")
#--------------------------------------------------------
                elif "/spam" in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("/spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               cl.sendMessage(to, teks)
                        else:
                            kr.sendMessage(to, "╔══════════════\n╠☛ out off range!!\n╚══════════════")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            cl.sendMessage(to, tulisan)
                        else:
                            cl.sendMessage(to, "╔══════════════\n╠☛ out off range!\n╚══════════════")
                    else:
                        pass
                elif "/sptag @" in msg.text:
                    _name = msg.text.replace("/sptag @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+"􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿􏿿"
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                            cl.sendMessage(msg)
                            cl.sendMessage(msg)
                            cl.sendMessage(msg)
                            cl.sendMessage(msg)
                            cl.sendMessage(msg)
                            cl.sendMessage(msg)
                            cl.sendMessage(msg)
                            cl.sendMessage(msg)
                            cl.sendMessage(msg)
                            cl.sendMessage(msg)
                            cl.sendMessage(msg)
                            cl.sendMessage(msg)
                            print ("Spamtag Berhasil.")
                elif msg.text in ["/blank"]:
                    msg.contentType = 13
                    msg.text = None
                    msg.contentMetadata = {'mid': "'"}
                    cl.sendMessage(msg)
#--------------------------------------------------------
                elif msg.text in ["Bantaii"]:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        group = ka.getGroup(msg.to)
                        group = kb.getGroup(msg.to)
                        group = kc.getGroup(msg.to)
                        group = kd.getGroup(msg.to)
                        group = ke.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
                        for x in nama:
                            if x not in Bots:
                                if x not in org["friend"]:
                                    try:
                                        klist=[ka,kb,kc,kd,ke]
                                        angrust=random.choice(klist)
                                        angrust.kickoutFromGroup(msg.to,[x])
                                    except:
                                        print ("limit")

#--------------------------------------------------------
                elif "Kill @" in msg.text:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                cl.kickoutFromGroup(msg.to, [mention['M']])
                            except:
                                cl.sendMessage(to, "limit")
                elif "tw1 kick @" in msg.text:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                ka.kickoutFromGroup(msg.to, [mention['M']])
                            except:
                                ka.sendMessage(to, "limit")
                elif "tw2 kick @" in msg.text:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                kb.kickoutFromGroup(msg.to, [mention['M']])
                            except:
                                kb.sendMessage(to, "limit")
                elif "tw3 kick @" in msg.text:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                kc.kickoutFromGroup(msg.to, [mention['M']])
                            except:
                                kc.sendMessage(to, "limit")
                elif "tw4 kick @" in msg.text:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                kd.kickoutFromGroup(msg.to, [mention['M']])
                            except:
                                kd.sendMessage(to, "limit")

                elif "tw5 kick @" in msg.text:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                ke.kickoutFromGroup(msg.to, [mention['M']])
                            except:
                                ke.sendMessage(to, "limit")

                elif "/kick @" in msg.text:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                random.choice(K2C).kickoutFromGroup(msg.to, [mention['M']])
                            except:
                                ka.sendMessage(to, "limit")

                elif "Kicker kick @" in msg.text:
                    _name = msg.text.replace("Kicker kick @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    gs.preventedJoinByTicket = False
                    cl.updateGroup(gs)
                    Invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    k1.acceptGroupInvitationByTicket(msg.to,Ti)
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            try:
                                k1.kickoutFromGroup(msg.to, [mention['M']])
                            except:
                                k1.sendMessage(to, "limit")
                    gs = k1.getGroup(msg.to)
                    gs.preventedJoinByTicket = True
                    k1.updateGroup(gs)
                    k1.leaveGroup(msg.to)
#-------------------------------------------------------
                elif msg.text in ["Allprotect on"]:
                        pro["protectgr"][msg.to] = True
                        pro["protectcancl"][msg.to] = True
                        pro["proJs"][msg.to] = True
                        pro["protectinvite"][msg.to] = True
                        pro["autokick"][msg.to] = True
                        with open('pro.json', 'w') as fp:
                            json.dump(pro, fp, sort_keys=True, indent=4)
                        cl.sendMessage(to,"╔════════════\n╠☛ protection on\n╚════════════")
                        print ("All protection on")
                elif msg.text in ["Allprotect off"]:
                    if msg.to in pro["protectgr"]:
                        try:
                            del pro["protectgr"][msg.to]
                        except:
                            pass
                    if msg.to in pro["protectcancl"]:
                        try:
                            del pro["protectcancl"][msg.to]
                        except:
                            pass
                    if msg.to in pro["proJs"]:
                        try:
                            del pro["proJs"][msg.to]
                        except:
                            pass
                    if msg.to in pro["protectinvite"]:
                        try:
                            del pro["protectinvite"][msg.to]
                        except:
                            pass
                    if msg.to in pro["autokick"]:
                        try:
                            del pro["autokick"][msg.to]
                        except:
                            pass
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔════════════\n╠☛ protection off\n╚════════════")
#---------------------------------------------------------
                elif msg.text in ["Proqr on"]:
                    pro["protectgr"][msg.to] = True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔════════════\n╠☛ protect qr on\n╚════════════")

                elif msg.text in ["Proqr off"]:
                    del pro["protectgr"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔════════════\n╠☛ protect qr off\n╚════════════")

#---------------------------------------------------------
                elif msg.text in ["Proinvite on"]:
                    pro["protectinvite"][msg.to]=True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔════════════\n╠☛ protect invite on\n╚════════════")

                elif msg.text in ["Proinvite off"]:
                    del pro["protectinvite"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔════════════\n╠☛ protect invite off\n╚════════════")

                elif msg.text in ["Projs on"]:
                    pro["proJs"][msg.to]=True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔════════════\n╠☛ Protection Alphat Js on\n╚════════════")

                elif msg.text in ["Projs off"]:
                    del pro["proJs"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔════════════\n╠☛ Protection Alphat Js off\n╚════════════")

#---------------------------------------------------------
                elif msg.text in ["Procancel on"]:
                    pro["protectcancl"][msg.to]=True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔════════════\n╠☛ protect cancel on\n╚════════════")

                elif msg.text in ["Procancel off"]:
                    del pro["protectcancl"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔════════════\n╠☛ protect cancel off\n╚════════════")

#--------------------------------------------------------
                elif msg.text in ["Left on"]:
                    pro["bymsg"][msg.to] = True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to, "╔════════════\n╠☛ msg left on\n╚════════════")

                elif msg.text in ["Left off"]:
                    del pro["bymsg"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to, "╔════════════\n╠☛ msg left off\n╚════════════")

#---------------------------------------------------------
                elif msg.text in ["Welcome on"]:
                    pro["wellcome"][msg.to]=True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to, "╔════════════\n╠☛ Msg welcome on\n╚════════════")

                elif msg.text in ["Welcome off"]:
                    del pro["wellcome"][msg.to]
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to, "╔════════════\n╠☛ Msg welcome off\n╚════════════")

#---------------------------------------------------------
                elif msg.text in ["Read on"]:
                    wait["reader"] = True
                    cl.sendMessage(to,"on")

                elif msg.text in ["Read off"]:
                    wait["reader"] = False
                    cl.sendMessage(to,"off")
#--------------------------------------------------------
                elif msg.text in ["Prokick on"]:
                    pro["autokick"][msg.to]=True
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to, "╔════════════\n╠☛ kick on\n╚════════════")

                elif msg.text in ["Prokick off"]:
                    pro["autokick"][msg.to]=False
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to, "╔════════════\n╠☛ kick off\n╚════════════")

#--------------------------------------------------------
                elif msg.text in ["Respon on"]:
                        wait["tagg"]=True
                        cl.sendMessage(to, "╔════════════\n╠☛ auto tag on\n╚════════════")

                elif msg.text in ["Respon off"]:
                        wait["tagg"]=False
                        cl.sendMessage(to, "╔════════════\n╠☛ auto tag off\n╚════════════")

                elif msg.text in ["Notag on"]:
                        wait["Mentionkick"]=True
                        cl.sendMessage(to, "╔════════════\n╠☛ Kick Mention on\n╚════════════")

                elif msg.text in ["Notag off"]:
                        wait["Mentionkick"]=False
                        cl.sendMessage(to, "╔════════════\n╠☛ Kick Mention off\n╚════════════")

                elif msg.text in ["Allrefresh"]:
                    if msg.to in pro["protectgr"]:
                        try:
                            del pro["protectgr"][msg.to]
                        except:
                            pass
                    if msg.to in pro["protectcancl"]:
                        try:
                            del pro["protectcancl"][msg.to]
                        except:
                            pass
                    if msg.to in pro["proJs"]:
                        try:
                            del pro["proJs"][msg.to]
                        except:
                            pass
                    if msg.to in pro["protectinvite"]:
                        try:
                            del pro["protectinvite"][msg.to]
                        except:
                            pass
                    if msg.to in pro["autokick"]:
                        try:
                            del pro["autokick"][msg.to]
                        except:
                            pass
                    if msg.to in pro["intaPoint"]:
                        try:
                            del pro['intaPoint'][msg.to]
                        except:
                            pass
                    if msg.to in pro["bymsg"]:
                        try:
                            del wait["bymsg"][msg.to]
                        except:
                            pass
                    if msg.to in pro["wellcome"]:
                        try:
                            del wait['wellcome'][msg.to]
                        except:
                            pass
                    with open('pro.json', 'w') as fp:
                        json.dump(pro, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔════════════\n╠☛ reset done\n╚════════════")

                elif msg.text in ["Grup set"]:
                    md = ""
                    if msg.to in pro["intaPoint"]: md+="╠☛ Auto in : ✓\n"
                    else: md +="╠☛ Auto in :: ✘\n"

                    if msg.to in pro["protectgr"]: md+="╠☛ Progrup : ✓\n"
                    else: md +="╠☛ Progrup : ✘\n"

                    if msg.to in pro["protectcancl"]: md+="╠☛ Procancel : ✓\n"
                    else: md+="╠☛ Procancel : ✘\n"

                    if msg.to in pro["protectinvite"]: md+="╠☛ Proinvite : ✓\n"
                    else: md+= "╠☛ Proinvite : ✘\n"

                    if msg.to in pro["autokick"]: md+="╠☛ Auto kick : ✓\n"
                    else:md+="╠☛ Auto kick : ✘\n"

                    if msg.to in pro["proJs"]: md+="╠☛ ProJs : ✓\n"
                    else:md+="╠☛ ProJs : ✘\n"

                    if msg.to in pro["wellcome"]: md+="╠☛ Sambutan : ✓\n"
                    else:md+="╠☛ Sambutan : ✘\n"

                    if msg.to in pro["bymsg"]: md+="╠☛ Msg left : ✓\n"
                    else:md+="╠☛ Msg left : ✘\n"
                    cl.sendMessage(to,"╔══════════════\n╠☛❲ Sett Group ❳☚\n╠══════════════\n"+ md +"╚══════════════")

                elif msg.text in ["Add off"]:
                    wait["invi"]=False
                    wait["ainvite"]=False
                    wait["binvite"]=False
                    wait["cinvite"]=False
                    wait["dinvite"]=False
                    wait["atarget"]=False
                    wait["dtarget"]=False
                    wait["afriend"]=False
                    wait["dfriend"]=False
                    wait["atebz"]=False
                    wait["dtebz"]=False
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"☛ all add off")

                elif msg.text in ["Add status"]:
                    md = ""
                    if wait["invi"] == True: md+="╠☛ Invite : ✓\n"
                    else:md+="╠☛ Invite : ✘\n"
                    if wait["ainvite"] == True: md+="╠☛ A invite : ✓\n"
                    else:md+="╠☛ A invite : ✘\n"
                    if wait["binvite"] == True: md+="╠☛ B invite : ✓\n"
                    else:md+="╠☛ B invite : ✘\n"
                    if wait["cinvite"] == True: md+="╠☛ C invite : ✓\n"
                    else:md+="╠☛ C invite : ✘\n"
                    if wait["dinvite"] == True: md+="╠☛ D invite : ✓\n"
                    else:md+="╠☛ D invite : ✘\n"
                    if wait["atarget"] == True: md+="╠☛ save : ✓\n"
                    else:md+="╠☛ save : ✘\n"
                    if wait["dtarget"] == True: md+="╠☛ dsave : ✓\n"
                    else:md+="╠☛ dsave : ✘\n"
                    if wait["atebz"] == True: md+="╠☛ add tebz : ✓\n"
                    else:md+="╠☛ add tebz : ✘\n"
                    if wait["dtebz"] == True: md+="╠☛ del tebz : ✓\n"
                    else:md+="╠☛ del tebz : ✘\n"
                    if wait["afriend"] == True: md+="╠☛ add friend : ✓\n"
                    else:md+="╠☛ add friend : ✘\n"
                    if wait["dfriend"] == True: md+="╠☛ del friend : ✓\n"
                    else:md+="╠☛ del friend : ✘\n"
                    cl.sendMessage(to,"╔══════════════\n╠     ☛❲ Setatus add ❳☚\n╠══════════════\n"+ md +"╚══════════════")

                elif msg.text in ["Status"]:
                    md = ""
                    if wait["midct"] == True: md+="╠☛ midct : ✓\n"
                    else:md+="╠☛ midct : ✘\n"
                    if wait["autojoin"] == True: md+="╠☛ auto join : ✓\n"
                    else:md+="╠☛ auto join : ✘\n"
                    if wait["tagg"] == True: md+="╠☛ tagging : ✓\n"
                    else:md+="╠☛ tagging : ✘\n"
                    if wait["siri"] == True: md+="╠☛ siri : ✓\n"
                    else:md+="╠☛ siri : ✘\n"
                    if wait["spamr"] == True: md+="╠☛ spam contact : ✓\n"
                    else:md+="╠☛ spam contact : ✘\n"
                    if wait["invi"] == True: md+="╠☛ invi : ✓\n"
                    else:md+="╠☛ invi : ✘\n"
                    if wait["ainvite"] == True: md+="╠☛ ainv : ✓\n"
                    else:md+="╠☛ ainv : ✘\n"
                    if wait["binvite"] == True: md+="╠☛ binv : ✓\n"
                    else:md+="╠☛ binv : ✘\n"
                    if wait["cinvite"] == True: md+="╠☛ cinv : ✓\n"
                    else:md+="╠☛ cinv : ✘\n"
                    if wait["dinvite"] == True: md+="╠☛ dinv : ✓\n"
                    else:md+="╠☛ dinv : ✘\n"
                    if wait["likeOn"] == True: md+="╠☛ Like : ✓\n"
                    else:md+="╠☛ Like : ✘\n"
                    if wait["timeline"] == True: md+="╠☛ Get post : ✓\n"
                    else:md+="╠☛ Get post : ✘\n"
                    cl.sendMessage(to,"╔══════════════\n╠    ☛❲Self status ❳☚\n╠══════════════\n"+ md +"╚══════════════")
#=============================#
                elif "Unban @" in msg.text:
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                        names = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if mention['M'] in wait2["blacklist"]:
                                del wait2["blacklist"][mention['M']]
                                with open('wait2.json', 'w') as fp:
                                    json.dump(wait2, fp, sort_keys=True, indent=4)
                                cl.sendMessage(to,"done ..")
                            else:
                                cl.sendMessage(to,"Not found")

                elif msg.text in ["Clear ban"]:
                    wait2['blacklist'] = {}
                    with open('wait2.json', 'w') as fp:
                        json.dump(wait2, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔══════════════\n╠☛ done boss\n╚══════════════")

                elif msg.text in ["Kill ban"]:
                     if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait2["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendMessage(to,"╔══════════════\n╠☛ empty user BL\n╚══════════════")
                            return
                        for jj in matched_list:
                            try:
                                ka.kickoutFromGroup(msg.to,[jj])
                                kb.kickoutFromGroup(msg.to,[jj])
                                kc.kickoutFromGroup(msg.to,[jj])
                                kd.kickoutFromGroup(msg.to,[jj])
                            except:
                                print ("limit")
                        cl.sendMessage(to,"Done")

                elif msg.text in ["Add blacklist"]:
                        wait["ablacklist"]=True
                        cl.sendMessage(to, "╔══════════════\n╠☛ please sent contact\n╚══════════════")

                elif msg.text in ["Del blacklist"]:
                        wait["dblacklist"]=True
                        cl.sendMessage(to, "╔══════════════\n╠☛ please sent contact\n╚══════════════")

                elif msg.text in ["Banlist"]:
                    if wait2["blacklist"] == {}:
                        cl.sendMessage(to,"╔══════════════\n╠☛ empty list\n╚══════════════")
                    else:
                        mc = "╔══════════════\n╠☛ ❲ BanList ❳☚\n╠══════════════"
                        for mi_d in wait2["blacklist"]:
                            mc += "\n╠☛ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(msg.to,mc + "\n╚══════════════")

                elif msg.text in ["Add friend"]:
                        wait["afriend"]=True
                        cl.sendMessage(to, "╔══════════════\n╠☛ please sent contact\n╚══════════════")

                elif msg.text in ["Del friend"]:
                        wait["dfriend"]=True
                        cl.sendMessage(to,"╔══════════════\n╠☛ please sent contact\n╚══════════════")

                elif msg.text in ["List friend"]:
                    if org["friend"] == {}:
                        cl.sendMessage(to,"╔══════════════\n╠☛ empty list\n╚══════════════")
                    else:
                        mc = "╔══════════════\n╠☛ ❲ Friend List ❳☚\n╠══════════════"
                        for mi_d in org["friend"]:
                            mc += "\n╠☛ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(msg.to,mc + "\n╚══════════════")

                elif msg.text in ["Clear friend"]:
                    org['friend'] = {}
                    with open('org.json', 'w') as fp:
                        json.dump(org, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔══════════════\n╠☛ succses\n╚══════════════")

                elif msg.text in ["Awb"]:
                    wait["ablack"]=True
                    cl.sendMessage(to,"╔══════════════\n╠☛ send contact\n╚══════════════")

                elif msg.text in ["Like off"]:
                    wait["dblack"]=False
                    cl.sendMessage(to,"╔══════════════\n╠☛ send contact\n╚══════════════")

                elif msg.text in ["My grup"]:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = cl.getGroup(i).name
                            h += "╠☛ %s\n" % (gn)
                        cl.sendMessage(to,"╔══════════════\n╠☛⟦ My grup ⟧☚\n╠══════════════\n"+ h +"╚══════════════")

                elif msg.text in ["Z1 grup"]:
                        gid = ka.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = ka.getGroup(i).name
                            h += "╠☛ %s\n" % (gn)
                        ka.sendMessage(to,"╔══════════════\n╠☛⟦ My grup ⟧☚\n╠══════════════\n"+ h +"╚══════════════")

                elif msg.text in ["Z2 grup"]:
                        gid = kb.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = kb.getGroup(i).name
                            h += "╠☛ %s\n" % (gn)
                        kb.sendMessage(to,"╔══════════════\n╠☛⟦ My grup ⟧☚\n╠══════════════\n"+ h +"╚══════════════")
                elif msg.text in ["Z3 grup"]:
                        gid = kc.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = kc.getGroup(i).name
                            h += "╠☛ %s\n" % (gn)
                        kc.sendMessage(to,"╔══════════════\n╠☛⟦ My grup ⟧☚\n╠══════════════\n"+ h +"╚══════════════")
                elif msg.text in ["Z4 grup"]:
                        gid = kd.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = kd.getGroup(i).name
                            h += "╠☛ %s\n" % (gn)
                        kd.sendMessage(to,"╔══════════════\n╠☛⟦ My grup ⟧☚\n╠══════════════\n"+ h +"╚══════════════")

                elif msg.text in ["Z5 grup"]:
                        gid = ke.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            gn = ke.getGroup(i).name
                            h += "╠☛ %s\n" % (gn)
                        ke.sendMessage(to,"╔══════════════\n╠☛⟦ My grup ⟧☚\n╠══════════════\n"+ h +"╚══════════════")

                elif "tw1 inv me: " in msg.text:
                    ng = msg.text.replace("tw1 inv me: ","")
                    gid = ka.getGroupIdsJoined()
                    for i in gid:
                            h = ka.getGroup(i).name
                            if h == ng:
                                ka.inviteIntoGroup(i,[mid])
                                ka.sendMessage(to,"Success invite to ☛❲"+ h +"❳☚ group")
                            else:
                                pass
                elif "tw2 inv me: " in msg.text:
                    ng = msg.text.replace("tw2 inv me: ","")
                    gid = kb.getGroupIdsJoined()
                    for i in gid:
                            h = kb.getGroup(i).name
                            if h == ng:
                                kb.inviteIntoGroup(i,[mid])
                                kb.sendMessage(to,"Success invite to ☛❲"+ h +"❳☚ group")
                            else:
                                pass
                elif "tw3 inv me: " in msg.text:
                    ng = msg.text.replace("tw3 inv me: ","")
                    gid = kc.getGroupIdsJoined()
                    for i in gid:
                            h = kc.getGroup(i).name
                            if h == ng:
                                kc.inviteIntoGroup(i,[mid])
                                kc.sendMessage(to,"Success invite to ☛❲"+ h +"❳☚ group")
                            else:
                                pass
                elif "tw4 inv me: " in msg.text:
                    ng = msg.text.replace("tw4 inv me: ","")
                    gid = kd.getGroupIdsJoined()
                    for i in gid:
                            h = kd.getGroup(i).name
                            if h == ng:
                                kd.inviteIntoGroup(i,[mid])
                                kd.sendMessage(to,"Success invite to ☛❲"+ h +"❳☚group")
                            else:
                                pass

                elif "tw5 inv me: " in msg.text:
                    ng = msg.text.replace("tw5 inv me: ","")
                    gid = ke.getGroupIdsJoined()
                    for i in gid:
                            h = ke.getGroup(i).name
                            if h == ng:
                                ke.inviteIntoGroup(i,[mid])
                                ke.sendMessage(to,"Success invite to ☛❲"+ h +"❳☚group")
                            else:
                                pass

                elif "Cname: " in msg.text:
                    x = cl.getProfile()
                    x.displayName = msg.text.replace("Zname: ","")
                    cl.updateProfile(x)
                    cl.sendMessage(to, " ☛done")

                elif "tw1 cn: " in msg.text:
                    x = ka.getProfile()
                    x.displayName = msg.text.replace("tw1 cn: ","")
                    ka.updateProfile(x)
                    ka.sendMessage(to, " ☛done")
                elif "tw2 cn: " in msg.text:
                    x = kb.getProfile()
                    x.displayName = msg.text.replace("tw2 cn: ","")
                    kb.updateProfile(x)
                    kb.sendMessage(to, " ☛done")
                elif "tw3 cn: " in msg.text:
                    x = kc.getProfile()
                    x.displayName = msg.text.replace("tw3 cn: ","")
                    kc.updateProfile(x)
                    kc.sendMessage(to, " ☛done")
                elif "tw4 cn: " in msg.text:
                    x = kd.getProfile()
                    x.displayName = msg.text.replace("tw4 cn: ","")
                    kd.updateProfile(x)
                    kd.sendMessage(to, " ☛done")
                elif "tw5 cn: " in msg.text:
                    x = ke.getProfile()
                    x.displayName = msg.text.replace("tw5 cn: ","")
                    ke.updateProfile(x)
                    ke.sendMessage(to, " ☛done")

                elif "Kicker cn: " in msg.text:
                    x = k1.getProfile()
                    x.displayName = msg.text.replace("Kicker cn: ","")
                    k1.updateProfile(x)
                    k1.senMessage(to, " ☛done")

                elif "Leave grup: " in msg.text:
                    ng = msg.text.replace("Leave grup: ","")
                    gid = ka.getGroupIdsJoined()
                    for i in gid:
                            h = ka.getGroup(i).name
                            if h == ng:
                                ka.sendMessage(i,"╔══════════════\n╠☛ bot dipaksa pulang owner!\n╚══════════════")
                                kb.leaveGroup(i)
                                kc.leaveGroup(i)
                                kd.leaveGroup(i)
                                ke.leaveGroup(i)
                                ka.leaveGroup(i)
                                cl.sendMessage(to,"Success left ["+ h +"] group")
                            else:
                                pass

                elif msg.text in ["Leave all grup"]:
                    gid = ka.getGroupIdsJoined()
                    for i in gid:
                        ka.sendMessage(i,"╔══════════════\n╠☛ bot dipaksa pulang owner!\n╚══════════════")
                        kb.leaveGroup(i)
                        kc.leaveGroup(i)
                        kd.leaveGroup(i)
                        ke.leaveGroup(i)
                        ka.leaveGroup(i)
                    cl.sendMessage(to,"☛ Success left all group")

                elif msg.text in ["Autojoin on"]:
                    wait["autojoin"]=True
                    cl.sendMessage(to,"╔══════════════\n╠☛ autojoin on\n╚══════════════")

                elif msg.text in ["Autojoin off"]:
                    wait["autojoin"]=False
                    cl.sendMessage(to,"╔══════════════\n╠☛ autojoin off\n╚══════════════")

                elif msg.text in ["Autoadd on"]:
                    wait["message"]=True
                    cl.sendMessage(to,"╔══════════════\n╠☛ autoAdd on\n╚══════════════")

                elif msg.text in ["Autoadd off"]:
                    wait["message"]=False
                    cl.sendMessage(to,"╔══════════════\n╠☛ autoAdd off\n╚══════════════")

                elif msg.text in ["Kicker gift"]:
                    X = cl.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    k1.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = k1.getGroup(msg.to)
                    try:
                        k1.sendMessage(msg.to, None, contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                        k1.sendMessage(to,"◄═===============⟮✶⟯===============═►\n\n      ☛❲• ™⟮✶⟯SELF Bot Version™ •❳☚\n\n     •••✶ ready rent Self n Pro Botz ✶•••\n\n◄═===============⟮ ❢ ⟯===============═►")
                    except:
                        print ("gift error")
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                    Ticket = k1.reissueGroupTicket(msg.to)
                    k1.leaveGroup(msg.to)

                elif msg.text in ["creator"]:
                    X = cl.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    k1.acceptGroupInvitationByTicket(msg.to,Ti)
                    group = k1.getGroup(msg.to)
                    try:
                        me = k1.getContact(mid)
                        k1.sendContact(msg.to, mid)
                        k1.sendMessage(msg.to,"╔══════════════\n╠☛ " + me.displayName + "\n╚══════════════")
                    except:
                        k1.sendMessage(to,"limit")
                    G = k1.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(msg.to)
                    k1.leaveGroup(msg.to)

                elif msg.text in ["Kicker kickall"]:
                    X = cl.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    k1.acceptGroupInvitationByTicket(msg.to,Ti)
                    group = k1.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    for x in nama:
                        time.sleep(0.2)
                        if x not in Bots:
                            if x not in org["friend"]:
                                try:
                                    k1.kickoutFromGroup(msg.to,[x])
                                except:
                                    pass
                    G = k1.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(msg.to)
                    k1.leaveGroup(msg.to)

                elif msg.text in ["Kicker absen"]:
                    X = cl.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    k1.acceptGroupInvitationByTicket(msg.to,Ti)
                    k1.sendMessage(to,"yess hadir\n\nada yang bisa dibantu bosquh?")
                    G = k1.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    k1.updateGroup(G)
                    k1.sendMessage(to,"slalu stay diluar boss\n\npamit ya boss...")
                    k1.sendMessage(to,"papay bosquh")
                    Ticket = k1.reissueGroupTicket(msg.to)
                    k1.leaveGroup(msg.to)

                elif msg.text in ["Kicker on"]:
                        wait["siri"]=True
                        cl.sendMessage(to, "╔══════════════\n╠☛ Ghost mode on\n╚══════════════")

                elif msg.text in ["Kicker off"]:
                        wait["siri"]=False
                        cl.sendMessage(to, "╔══════════════\n╠☛ Ghos mode off\n╚══════════════")

                elif msg.text in ["joinlink on"]:
                        wait["autoJoinTicket"]=True
                        cl.sendMessage(to, "╔══════════════\n╠☛ autoJoin Link mode on\n╚══════════════")

                elif msg.text in ["joinlink off"]:
                        wait["autoJoinTicket"]=False
                        cl.sendMessage(to, "╔══════════════\n╠☛ autoJoin Link mode off\n╚══════════════")

                elif msg.text in ["Unsend on"]:
                        wait["unsendMessage"]=True
                        cl.sendMessage(to, "╔══════════════\n╠☛ UnsendMsg mode on\n╚══════════════")

                elif msg.text in ["Unsend off"]:
                        wait["unsendMessage"]=False
                        cl.sendMessage(to, "╔══════════════\n╠☛ unsendMsg mode off\n╚══════════════")

#--------------------------------------------------------
                elif msg.text in ["Inta"]:
                        now2 = datetime.now()
                        pro['intaPoint'][msg.to] = True
                        pro['intaTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                        with open('pro.json', 'w') as fp:
                            json.dump(pro, fp, sort_keys=True, indent=4)
                        cl.sendMessage(to, "yess")

                elif msg.text in ["Clear inta"]:
                        now2 = datetime.now()
                        del pro['intaPoint'][msg.to]
                        del pro['intaTime'][msg.to]
                        with open('pro.json', 'w') as fp:
                            json.dump(pro, fp, sort_keys=True, indent=4)
                        cl.sendMessage(to, "╔══════════════\n╠☛ succses clear\n╚══════════════")
#--------------------------------------------------------
                elif msg.text in ["Mention","Tag all"]:
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                    if jml <= 100:
                        summon(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, len(nama)-1):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                    if jml > 200  and jml < 500:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, 199):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range(200, 299):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                        for l in range(300, 399):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for m in range(400, len(nama)-1):
                            nm5 += [nama[m]]
                        summon(msg.to, nm5)

                elif msg.text in ["Lurk on"]:
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         wait2['readPoint'][msg.to] = msg_id
                         wait2['readMember'][msg.to] = {}
                         cl.sendMessage(msg.to, "Lurking mode on\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                elif msg.text in ["Lurk off"]:
                         tz = pytz.timezone("Asia/Jakarta")
                         timeNow = datetime.now(tz=tz)
                         del wait2['readPoint'][msg.to]
                         del wait2['readMember'][msg.to]
                         cl.sendMessage(msg.to, "Lurking mode off\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                elif msg.text in ["Lurkers"]:
                       if msg.to in wait2['readPoint']:
                           if wait2['readMember'][msg.to] != {}:
                               aa = []
                               for x in wait2['readMember'][msg.to]:
                                   aa.append(x)
                               try:
                                   arrData = ""
                                   textx = "  [ Result Sider Member ]    \n\n  [ Lurking ]\n1. ".format(str(len(aa)))
                                   arr = []
                                   no = 1
                                   b = 1
                                   for i in aa:
                                       b = b + 1
                                       end = "\n"
                                       mention = "@x\n"
                                       slen = str(len(textx))
                                       elen = str(len(textx) + len(mention) - 1)
                                       arrData = {'S':slen, 'E':elen, 'M':i}
                                       arr.append(arrData)
                                       tz = pytz.timezone("Asia/Jakarta")
                                       timeNow = datetime.now(tz=tz)
                                       textx += mention
                                       if no < len(aa):
                                           no += 1
                                           textx += str(b) + ". "
                                       else:
                                           try:
                                               no = " {} ".format(str(cl.getGroup(msg.to).name))
                                           except:
                                               no = "  "
                                   msg.to = msg.to
                                   msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                   msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                   msg.contentType = 0
                                   cl.sendMessage1(msg)
                               except:
                                   pass
                               try:
                                   del wait2['readPoint'][msg.to]
                                   del wait2['readMember'][msg.to]
                               except:
                                   pass
                               wait2['readPoint'][msg.to] = msg.id
                               wait2['readMember'][msg.to] = {}
                           else:
                               cl.sendMessage(msg.to, "°no sider•••")
                       else:
                           cl.sendMessage(msg.to, "please create lurk on")

                elif msg.text in ["Sider on"]:
                      try:
                          tz = pytz.timezone("Asia/Jakarta")
                          timeNow = datetime.now(tz=tz)
                          cl.sendMessage(msg.to, "╔══════════════\n╠☛ starting cek sider\n╚══════════════\n\n╔══════════════\n╠☛ date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠☛ hour "+ datetime.strftime(timeNow,'%H:%M:%S')+"\n╚══════════════")
                          del ciduk['ceadPoint'][msg.to]
                          del ciduk['ceadMember'][msg.to]
                          del ciduk['cyduk'][msg.to]
                      except:
                          pass
                      ciduk['ceadPoint'][msg.to] = msg.id
                      ciduk['ceadMember'][msg.to] = ""
                      ciduk['cyduk'][msg.to]=True
                      print ("Sider room")
                elif msg.text in ["Sider off"]:
                       if msg.to in ciduk['ceadPoint']:
                           tz = pytz.timezone("Asia/Jakarta")
                           timeNow = datetime.now(tz=tz)
                           ciduk['cyduk'][msg.to]=False
                           cl.sendMessage(msg.to, "╔══════════════\n╠☛ sider off mode\n╚══════════════")
                       else:
                           cl.sendMessage(msg.to, "done off°")

                elif msg.text in ["Rechat","Bersihin"]:
                    try:
                        ka.removeAllMessages(op.param2)
                        ka.sendMessage(to,"done")
                        kb.removeAllMessages(op.param2)
                        kb.sendMessage(to,"done")
                        kc.removeAllMessages(op.param2)
                        kc.sendMessage(to,"done")
                        kd.removeAllMessages(op.param2)
                        kd.sendMessage(to,"done")
                        ke.removeAllMessages(op.param2)
                        ke.sendMessage(to,"done")
                        ka.sendMessage(to,"done bosqu")
                    except:
                        ka.removeAllMessages(op.param2)
                        ka.sendMessage(to,"done")
                        kb.removeAllMessages(op.param2)
                        kb.sendMessage(to,"done")
                        kc.removeAllMessages(op.param2)
                        kc.sendMessage(to,"done")
                        kd.removeAllMessages(op.param2)
                        kd.sendMessage(to,"done")
                        ke.removeAllMessages(op.param2)
                        ke.sendMessage(to,"done")
                        k1.removeAllMessages(op.param2)
                        k1.sendMessage(to,"done")
                        ka.sendMessage(to,"done bosqu")
#--------------------------------------------------------
                elif msg.text in ["Cancel","Cancel all"]:
                    group = cl.getGroup(msg.to)
                    if group.invitee is None:
                        cl.sendMessage(op.message.to, "╔══════════════\n╠☛ no one is inviting\n╚══════════════")
                    else:
                        nama = [contact.mid for contact in group.invitee]
                        for x in nama:
                            cl.cancelGroupInvitation(msg.to, [x])
                            time.sleep(0.3)
                        cl.sendMessage(to, "done.")
                        print ("done cancell")

                elif msg.text in ["Bot cancel"]:
                    group = ka.getGroup(msg.to)
                    if group.invitee is None:
                        ka.sendMessage(op.message.to, "╔══════════════\n╠☛ no one is inviting\n╚══════════════")
                    else:
                        nama = [contact.mid for contact in group.invitee]
                        for x in nama:
                            random.choice(K2C).cancelGroupInvitation(msg.to, [x])
                            time.sleep(0.3)
                        ka.sendMessage(to, "done.")
                        print ("done cancell")

                elif msg.text in ["tw1 cancel"]:
                    group = kb.getGroup(msg.to)
                    if group.invitee is None:
                        kb.sendMessage(op.message.to, "╔══════════════\n╠☛ no one is inviting\n╚══════════════")
                    else:
                        nama = [contact.mid for contact in group.invitee]
                        for x in nama:
                            kb.cancelGroupInvitation(msg.to, [x])
                            time.sleep(0.3)
                        kb.sendMessage(to, "done.")
                        print ("done cancell")

                elif msg.text in ["tw2 cancel"]:
                    group = kc.getGroup(msg.to)
                    if group.invitee is None:
                        kc.sendMessage(op.message.to, "╔══════════════\n╠☛ no one is inviting\n╚══════════════")
                    else:
                        nama = [contact.mid for contact in group.invitee]
                        for x in nama:
                            kc.cancelGroupInvitation(msg.to, [x])
                            time.sleep(0.3)
                        kc.sendMessage(to, "done.")
                        print ("done cancell")

                elif msg.text in ["tw3 cancel"]:
                    group = kd.getGroup(msg.to)
                    if group.invitee is None:
                        kd.sendMessage(op.message.to, "╔══════════════\n╠☛ no one is inviting\n╚══════════════")
                    else:
                        nama = [contact.mid for contact in group.invitee]
                        for x in nama:
                            kd.cancelGroupInvitation(msg.to, [x])
                            time.sleep(0.3)
                        kd.sendMessage(to, "done.")
                        print ("done cancell")

                elif msg.text in ["tw4 cancel"]:
                    group = ka.getGroup(msg.to)
                    if group.invitee is None:
                        ka.sendMessage(op.message.to, "╔══════════════\n╠☛ no one is inviting\n╚══════════════")
                    else:
                        nama = [contact.mid for contact in group.invitee]
                        for x in nama:
                            ka.cancelGroupInvitation(msg.to, [x])
                            time.sleep(0.3)
                        ka.sendMessage(to, "done.")
                        print ("done cancell")

                elif msg.text in ["tw5 cancel"]:
                    group = ke.getGroup(msg.to)
                    if group.invitee is None:
                        ke.sendMessage(op.message.to, "╔══════════════\n╠☛ no one is inviting\n╚══════════════")
                    else:
                        nama = [contact.mid for contact in group.invitee]
                        for x in nama:
                            ke.cancelGroupInvitation(msg.to, [x])
                            time.sleep(0.3)
                        ke.sendMessage(to, "done.")
                        print ("done cancell")

                elif msg.text in ["Kicker cancel"]:
                    group = k1.getGroup(msg.to)
                    if group.invitee is None:
                        k1.sendMessage(op.message.to, "╔══════════════\n╠☛ no one is inviting\n╚══════════════")
                    else:
                        nama = [contact.mid for contact in group.invitee]
                        for x in nama:
                            k1.cancelGroupInvitation(msg.to, [x])
                            time.sleep(0.4)
                        k1.sendMessage(to, "done.")
                        print ("done cancell")
#--------------------------------------------------------
#--------------------------------------------------------
                elif msg.text in ["...."]:
                        G = cl.getGroup(msg.to)
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                elif msg.text in ["All join","Masuk"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                elif msg.text in [".inv"]:
                        cl.inviteIntoGroup(msg.to,[Amid,Bmid,Cmid,Dmid,Emid])
                        ka.acceptGroupInvitation(msg.to)
                        kb.acceptGroupInvitation(msg.to)
                        kc.acceptGroupInvitation(msg.to)
                        kd.acceptGroupInvitation(msg.to)
                        ke.acceptGroupInvitation(msg.to)
                elif msg.text in ["Kicker stay"]:
                    try:
                        znf = [Smid]
                        ka.inviteIntoGroup(msg.to, znf)
                    except:
                        pass
                elif msg.text in ["ZNF stay"]:
                    try:
                        znf = [Smid]
                        cl.inviteIntoGroup(msg.to, znf)
                    except:
                        pass
                elif msg.text in ["tw1 join"]:
                        x = cl.getGroup(msg.to)
                        x.preventedJoinByTicket = False
                        cl.updateGroup(x)
                        invsend = 0
                        Ti = cl.reissueGroupTicket(msg.to)
                        ka.acceptGroupInvitationByTicket(msg.to,Ti)
                        G = cl.getGroup(msg.to)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                elif msg.text in ["tw2 join"]:
                      x = cl.getGroup(msg.to)
                      x.preventedJoinByTicket = False
                      cl.updateGroup(x)
                      invsend = 0
                      Ti = cl.reissueGroupTicket(msg.to)
                      kb.acceptGroupInvitationByTicket(msg.to,Ti)
                      G = cl.getGroup(msg.to)
                      G.preventedJoinByTicket = True
                      cl.updateGroup(G)
                      Ticket = cl.reissueGroupTicket(msg.to)
                elif msg.text in ["tw3 join"]:
                      x = cl.getGroup(msg.to)
                      x.preventedJoinByTicket = False
                      cl.updateGroup(x)
                      invsend = 0
                      Ti = cl.reissueGroupTicket(msg.to)
                      kc.acceptGroupInvitationByTicket(msg.to,Ti)
                      G = cl.getGroup(msg.to)
                      G.preventedJoinByTicket = True
                      cl.updateGroup(G)
                      Ticket = cl.reissueGroupTicket(msg.to)
                elif msg.text in ["tw4 join"]:
                      X = cl.getGroup(msg.to)
                      X.preventedJoinByTicket = False
                      cl.updateGroup(X)
                      invsend = 0
                      Ti = cl.reissueGroupTicket(msg.to)
                      kd.acceptGroupInvitationByTicket(msg.to,Ti)
                      G = cl.getGroup(msg.to)
                      G.preventedJoinByTicket = True
                      cl.updateGroup(G)
                      Ticket = cl.reissueGroupTicket(msg.to)
                elif msg.text in ["tw5 join"]:
                      X = cl.getGroup(msg.to)
                      X.preventedJoinByTicket = False
                      cl.updateGroup(X)
                      invsend = 0
                      Ti = cl.reissueGroupTicket(msg.to)
                      ke.acceptGroupInvitationByTicket(msg.to,Ti)
                      G = cl.getGroup(msg.to)
                      G.preventedJoinByTicket = True
                      cl.updateGroup(G)
                      Ticket = cl.reissueGroupTicket(msg.to)

                elif msg.text in ["Kicker join"]:
                    X = cl.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    cl.updateGroup(X)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    k1.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = cl.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(msg.to)

#===========Hiburan============#
                elif "Sholat: " in msg.text:
                     sep = text.split(" ")
                     location = text.replace(sep[0] + " ","")
                     with requests.session() as web:
                          web.headers["user-agent"] = random.choice(wait["userAgent"])
                          r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                          data = r.text
                          data = json.loads(data)
                          tz = pytz.timezone("Asia/Jakarta")
                          timeNow = datetime.now(tz=tz)
                          if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                 ret_ = "     「Jadwal Sholat」"
                                 ret_ += "\n☛Lokasi : " + data[0]
                                 ret_ += "\n⌬ " + data[1]
                                 ret_ += "\n⌬ " + data[2]
                                 ret_ += "\n⌬ " + data[3]
                                 ret_ += "\n⌬ " + data[4]
                                 ret_ += "\n⌬ " + data[5]
                                 ret_ += "\n\n☛Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                 ret_ += "\n☛Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                          cl.sendMessage(msg.to, str(ret_))

                elif "Cuaca: " in msg.text:
                    separate = text.split(" ")
                    location = text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["user-agent"] = random.choice(wait["userAgent"])
                        r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                        data = r.text
                        data = json.loads(data)
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        if "result" not in data:
                            ret_ = "「Status Cuaca」"
                            ret_ += "\n☛ Lokasi : " + data[0].replace("Temperatur di kota ","")
                            ret_ += "\n☛ Suhu : " + data[1].replace("Suhu : ","") + " C"
                            ret_ += "\n☛ Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                            ret_ += "\n☛ Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                            ret_ += "\n☛ Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                            ret_ += "\n\n☛ Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                            ret_ += "\n☛ Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                        cl.sendMessage(msg.to, str(ret_))

                elif "Lokasi: " in msg.text:
                    separate = msg.text.split(" ")
                    location = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["user-agent"] = random.choice(wait["userAgent"])
                        r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                        data = r.text
                        data = json.loads(data)
                        if data[0] != "" and data[1] != "" and data[2] != "":
                            link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                            ret_ = " 「Info Lokasi」"
                            ret_ += "\n☛ Location : " + data[0]
                            ret_ += "\n☛ Google Maps : " + link
                        else:
                            ret_ = "Details Location Error : Location not found"
                        cl.sendMessage(msg.to,str(ret_))

                elif "ID line: " in msg.text:
                      msgs = msg.text.replace("ID line: ","")
                      conn = cl.findContactsByUserid(msgs)
                      if True:
                          cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                          cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

                elif "Max: " in msg.text:
                        proses = text.split(":")
                        strnum = text.replace(proses[0] + ":","")
                        num =  int(strnum)
                        wait2["Maxlimit"] = num
                        cl.sendMessage(msg.to,"Succes Sett Limit to " +strnum)

                elif "Spamcall: " in msg.text:
                        proses = text.split(":")
                        strnum = text.replace(proses[0] + ":","")
                        num =  int(strnum)
                        wait["limit"] = num
                        cl.sendText(msg.to,"Succes Sett Spamcall to " +strnum)

                elif "Spamtag " in msg.text:
                        if 'MENTION' in msg.contentMetadata.keys()!=None:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            zx = ""
                            zxc = " "
                            zx2 = []
                            pesan2 = "@a"" "
                            xlen = str(len(zxc))
                            xlen2 = str(len(zxc)+len(pesan2)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':key1}
                            zx2.append(zx)
                            zxc += pesan2
                            msg.contentType = 0
                            msg.text = zxc
                            lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                            msg.contentMetadata = lol
                            jmlh = int(wait2["Maxlimit"])
                            if jmlh <= 1000:
                                for x in range(jmlh):
                                    try:
                                        cl.sendMessage1(msg)
                                    except Exception as e:
                                        cl.sendMessage(msg.to,str(e))
                            else:
                                cl.sendMessage(msg.to,"Eror Out off Range")

                elif msg.text in ["Spamcall"]:
                     if msg.toType == 2:
                        group = cl.getGroup(to)
                        members = [mem.mid for mem in group.members]
                        jmlh = int(wait["limit"])
                        cl.sendMessage(msg.to, "Spam Call Grup {} Done ".format(str(wait["limit"])))
                        if jmlh <= 1000:
                          for x in range(jmlh):
                             try:
                                call.acquireGroupCallRoute(to)
                                call.inviteIntoGroupCall(to, contactIds=members)
                             except Exception as e:
                                cl.sendMessage(msg.to,str(e))
                        else:
                            cl.sendMessage(msg.to,"Error out off range")
#--------------------------------------------------------
                elif msg.text in ["Invite on"]:
                        wait["invi"] = True
                        cl.sendMessage(to,"╔══════════════\n╠☛ please sent contact\n╚══════════════")
                        print ("iiiiNv ")
                elif msg.text in ["tw1 invite"]:
                        wait["ainvite"] = True
                        ka.sendMessage(to,"╔══════════════\n╠☛ please sent contact\n╚══════════════")
                        print ("inv a")
                elif msg.text in ["tw2 invite"]:
                        wait["binvite"] = True
                        kb.sendMessage(to,"╔══════════════\n╠☛ please sent contact\n╚══════════════")
                        print ("inv b")
                elif msg.text in ["tw3 invite"]:
                        wait["cinvite"] = True
                        kc.sendMessage(to,"╔══════════════\n╠☛ please sent contact\n╚══════════════")
                        print ("inv c")
                elif msg.text in ["tw4 invite"]:
                        wait["dinvite"] = True
                        kd.sendMessage(to,"╔══════════════\n╠☛ please sent contact\n╚══════════════")
                        print ("inv d")
                elif msg.text in ["tw5 invite"]:
                        wait["einvite"] = True
                        ke.sendMessage(to,"╔══════════════\n╠☛ please sent contact\n╚══════════════")
                        print ("inv d")

#--------------------------------------------------------
                elif msg.text in ["Bye all","Pulang"]:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            ka.leaveGroup(msg.to)
                            kb.leaveGroup(msg.to)
                            kc.leaveGroup(msg.to)
                            kd.leaveGroup(msg.to)
                            ke.leaveGroup(msg.to)
                        except:
                            ka.leaveGroup(msg.to)
                            kb.leaveGroup(msg.to)
                            kc.leaveGroup(msg.to)
                            kd.leaveGroup(msg.to)
                            ke.leaveGroup(msg.to)
                            k1.leaveGroup(msg.to)
                elif msg.text in ["tw1 bye"]:
                    if msg.toType == 2:
                        ginfo = ka.getGroup(msg.to)
                        try:
                            ka.leaveGroup(msg.to)
                            print ("a bye")
                        except:
                            pass
                elif msg.text in ["tw2 bye"]:
                    if msg.toType == 2:
                        ginfo = kb.getGroup(msg.to)
                        try:
                            kb.leaveGroup(msg.to)
                            print ("b bye")
                        except:
                            pass
                elif msg.text in ["tw3 bye"]:
                    if msg.toType == 2:
                        ginfo = kc.getGroup(msg.to)
                        try:
                            kc.leaveGroup(msg.to)
                            print ("c bye")
                        except:
                            pass
                elif msg.text in ["tw4 bye"]:
                    if msg.toType == 2:
                        ginfo = kd.getGroup(msg.to)
                        try:
                            kd.leaveGroup(msg.to)
                            print ("d bye")
                        except:
                            pass
                elif msg.text in ["tw5 bye"]:
                    if msg.toType == 2:
                        ginfo = ke.getGroup(msg.to)
                        try:
                            ke.leaveGroup(msg.to)
                            print ("d bye")
                        except:
                            pass
                elif msg.text in ["/bye"]:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)
                            print ("cl bye")
                        except:
                            pass
                elif msg.text in ["Kicker bye"]:
                    if msg.toType == 2:
                        ginfo = k1.getGroup(msg.to)
                        try:
                            k1.leaveGroup(msg.to)
                            print ("ghost bye")
                        except:
                            pass
#--------------------------------------------------------
                elif msg.text in ["List member"]:
                    kontak = cl.getGroup(msg.to)
                    group = kontak.members
                    msgs="╔══════════════\n╠☛❲ Member List ❳☚\n╠══════════════"
                    for ids in group:
                        msgs+="\n╠☛ %s" % (ids.displayName)
                    msgs+="\n╠══════════════\n╠☛❲ Total Members : %i ❳☚\n" % len(group)+"╚══════════════"
                    cl.sendMessage(to, msgs)
#--------------------------------------------------------
                elif msg.text in ["Gift"]:
                    cl.sendMessage(to, "👇👇.For U°°°°")
                    cl.sendMessage(to, None, contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                    print ("gift")
#--------------------------------------------------------
                elif "tr-en" in msg.text:
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif "tr-id" in msg.text:
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
#================================#
                elif "Coment: " in msg.text:
                    wait["comment"] = msg.text.replace("Coment: ","")
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendText(msg.to,"╔══════════════\n╠☛ succses\n╚══════════════")
#=================================#
                elif "Sider: " in msg.text:
                    wait["cctvteks"] = msg.text.replace("Sider: ","")
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔══════════════\n╠☛ succses\n╚══════════════")
#====================#
                elif "Tag: " in msg.text:
                    wait["teksp"] = msg.text.replace("Tag: ","")
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔══════════════\n╠☛ succses\n╚══════════════")
#===================#
                elif "Left: " in msg.text:
                    wait["leftmsg"] = msg.text.replace("Left: ","")
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔══════════════\n╠☛ succses\n╚══════════════")
#=================#
                elif "Welcome: " in msg.text:
                    wait["welmsg"] = msg.text.replace("Welcome: ","")
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔══════════════\n╠☛ succses\n╚══════════════")
                elif msg.text in ["Like "]:
                    try:
                        typel = [1001,1002,1003,1004,1005,1006]
                        key = eval(msg.contentMetadata["MENTION"])
                        u = key["MENTIONEES"][0]["M"]
                        a = cl.getContact(u).mid
                        s = cl.getContact(u).displayName
                        hasil = channel.getHomeProfile(mid=a)
                        st = hasil['result']['feeds']
                        for i in range(len(st)):
                            test = st[i]
                            result = test['post']['postInfo']['postId']
                            channel.like(str(sender), str(result), likeType=random.choice(typel))
                            channel.comment(str(sender), str(result), wait['comment'])
                        cl.sendMessage(msg.to, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
#=================#
                elif "Add: " in msg.text:
                    wait["message"] = msg.text.replace("Add: ","")
                    with open('setting.json', 'w') as fp:
                        json.dump(wait, fp, sort_keys=True, indent=4)
                    cl.sendMessage(to,"╔══════════════\n╠☛ succses\n╚══════════════")
                elif msg.text in ["Check all msg"]:
                    cl.sendMessage(to,"msg sider: \n══════════════\n" + wait["cctvteks"] + "\n══════════════")
                    cl.sendMessage(to,"msg comment: \n══════════════\n" + wait["comment"] + "\n══════════════")
                    cl.sendMessage(to,"msg tag: \n══════════════\n" + wait["teksp"] + "\n══════════════")
                    cl.sendMessage(to,"Msg leave: \n══════════════\n" + wait["leftmsg"] + "\n══════════════")
                    cl.sendMessage(to,"msg welcome: \n══════════════\n" + wait["welmsg"] + "\n══════════════")
                    cl.sendMessage(to,"msg add: \n══════════════\n" + wait["message"] + "\n══════════════")
                else:
                    pass
#==========================#
            elif msg.contentType == 13:
                if wait["atarget"]==True:
                    if msg.contentMetadata["mid"] in org["target"]:
                        cl.sendMessage(msg.to, "╔══════════════\n╠ ☛ sudah di save boss\n╚══════════════")
                        wait["atarget"]=False
                        print ("sudah di save")
                    else:
                        org["target"][msg.contentMetadata["mid"]] = True
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        cl.sendMessage(msg.to, "╔══════════════\n╠ ☛ done save\n╚══════════════")
                        wait["atarget"]=False
                        print ("save succes")
                if wait["dtarget"]==True:
                    if msg.contentMetadata["mid"] in org["target"]:
                        del org["target"][msg.contentMetadata["mid"]]
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        wait["dtarget"]=False
                        cl.sendMessage(msg.to,"╔══════════════\n╠ ☛ done removed\n╚══════════════")
                    else:
                        cl.sendMessage(msg.to,"╔══════════════\n╠ ☛ target not found\n╚══════════════")

#====================#
                if wait["afriend"]==True:
                    if msg.contentMetadata["mid"] in org["friend"]:
                        cl.sendMessage(to, "╔══════════════\n╠ ☛ sudah jadi teman\n╚══════════════")
                        wait["afriend"]=False
                        print ("was f")
                    else:
                        org["friend"][msg.contentMetadata["mid"]] = True
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        cl.sendMessage(to, "╔══════════════\n╠ ☛ done add boss\n╚══════════════")
                        wait["afriend"]=False
                        print ("succes F")
#===============#
                if wait["dfriend"]==True:
                    if msg.contentMetadata["mid"] in org["friend"]:
                        del org["friend"][msg.contentMetadata["mid"]]
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        cl.sendMessage(to,"╔══════════════\n╠ ☛ sorry diremove\n╚══════════════")
                        wait["dfriend"]=False
                        print ("succes deleted")
                    else:
                        cl.sendMessage(to,"╔══════════════\n╠ ☛ target not found\n╚══════════════")
                        wait["dfriend"]=False
                        print ("not found del")
#====================#
                if wait["ablacklist"]==True:
                    if msg.contentMetadata["mid"] in wait2["blacklist"]:
                        cl.sendMessage(to, "╔══════════════\n╠ ☛ Was BL boss\n╚══════════════")
                        wait["ablacklist"]=False
                        print ("was f")
                    else:
                        wait2["blacklist"][msg.contentMetadata["mid"]] = True
                        with open('wait2.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.sendMessage(to, "╔══════════════\n╠ ☛ Blacklist Saved\n╚══════════════")
                        wait["ablacklist"]=False
                        print ("succes F")
#===============#
                if wait["dblacklist"]==True:
                    if msg.contentMetadata["mid"] in wait2["blacklist"]:
                        del wait2["blacklist"][msg.contentMetadata["mid"]]
                        with open('wait2.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.sendMessage(to, "╔══════════════\n╠ ☛ Blacklist Removed\n╚══════════════")
                        wait["dblacklist"]=False
                        print ("succes delete BL")
                    else:
                        cl.sendMessage(to,"╔══════════════\n╠ ☛ target not found\n╚══════════════")
                        wait["dblacklist"]=False
                        print ("not found del")
#=============#
                if wait["ainvite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = ka.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            ka.sendMessage(to,"dia ☛❲ " + _name + "❳☚ sudah didalam group boss")
                            wait["ainvite"] = False
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            ka.findAndAddContactsByMid(target)
                            ka.inviteIntoGroup(msg.to,[target])
                            ka.sendMessage(to,"succses invite : \n╔══════════════\n╠ ☛❲" + _name + "❳☚\n╚══════════════\nsemoga dia betah")
                            wait["ainvite"] = False
                            print ("ok")
                            break
#=================#
                if wait["invi"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            cl.sendMessage(to,"dia ☛❲ " + _name + " ❳☚ sudah didalam group boss")
                            wait["invi"] = False
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            cl.findAndAddContactsByMid(target)
                            cl.inviteIntoGroup(msg.to,[target])
                            cl.sendMessage(to,"succses Invite : \n╔══════════════\n╠ ☛❲" + _name + "❳☚\n╚══════════════\nsemoga dia betah")
                            wait["invi"] = False
                            print ("ok")
                            break
#===============#
                if wait["binvite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = kb.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            kb.sendMessage(to,"dia ☛❲ " + _name + " ❳☚ sudah didalam boss")
                            wait["binvite"] = False
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            kb.findAndAddContactsByMid(target)
                            kb.inviteIntoGroup(msg.to,[target])
                            kb.sendMessage(to,"succses Invite : \n╔══════════════\n╠ ☛❲" + _name + "❳☚\n╚══════════════\nsemoga dia betah")
                            wait["binvite"] = False
                            print ("ok")
                            break
#=================#
                if wait["cinvite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = kc.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            kc.sendMessage(to,"dia ☛❲" + _name + "❳☚ sudah didalam boss")
                            wait["cinvite"] = False
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            kc.findAndAddContactsByMid(target)
                            kc.inviteIntoGroup(msg.to,[target])
                            kc.sendMessage(to,"succses Invite : \n╔══════════════\n╠ ☛❲" + _name + "❳☚\n╚══════════════\nsemoga dia betah")
                            wait["cinvite"] = False
                            print ("ok")
                            break
#=================#
                if wait["dinvite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = kd.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            kd.sendMessage(to,"dia ☛❲" + _name + " ❳☚ dia sudah didalam boss")
                            wait["dinvite"] = False
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            kd.findAndAddContactsByMid(target)
                            kd.inviteIntoGroup(msg.to,[target])
                            kd.sendMessage(to,"succses Invite : \n╔══════════════\n╠ ☛❲" + _name + "❳☚\n╚══════════════\nsemoga dia betah")
                            wait["dinvite"] = False
                            print ("ok")
                            break
                if wait["einvite"] == True:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = ke.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            ke.sendMessage(to,"dia ☛❲" + _name + " ❳☚ dia sudah didalam boss")
                            wait["einvite"] = False
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            ke.findAndAddContactsByMid(target)
                            ke.inviteIntoGroup(msg.to,[target])
                            ke.sendMessage(to,"succses Invite : \n╔══════════════\n╠ ☛❲" + _name + "❳☚\n╚══════════════\nsemoga dia betah")
                            wait["einvite"] = False
                            print ("ok")
                            break

            if msg.contentType == 7:
                if wait["sticker"] == True:
                  msg.contentType = 0
                  cl.sendMessage(msg.to,"╔══════════════\n╠☛❲Check Sticker❳\n╠☛ STKID : " + msg.contentMetadata["STKID"] +"\n╠☛ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n╠☛ STKVER : " + msg.contentMetadata["STKVER"] + "\n╠☛ " + "line://shop/detail/" + msg.contentMetadata["STKPKGID"] +"\n╚══════════════")
                else:
                   pass
            if msg.contentType == 13:
                if wait["ablack"] == True:
                    if msg.contentMetadata["mid"] in wait2["commentBlack"]:
                        with open('wait2.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.sendMessage(to, "╔══════════════\n╠ ☛ in cblacklist\n╚══════════════")
                        wait["ablack"] = False
                    else:
                        wait2["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["ablack"] = False
                        cl.sendMessage(msg.to,"no comment")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait2["commentBlack"]:
                        del wait2["commentBlack"][msg.contentMetadata["mid"]]
                        with open('wait2.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.sendMessage(to, "╔══════════════\n╠ ☛ cblackist removed\n╚══════════════")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendMessage(msg.to,"not in Blacklist")
#=================-#
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if wait["reader"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in wait2["readPoint"]:
                    if sender not in wait2["ROM"][msg.to]:
                        wait2["ROM"][msg.to][sender] = True
                if wait["unsendMessage"] == True:
                    try:
                        msg = op.message
                        if msg.toType == 0:
                            cl.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                        else:
                            cl.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                            msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    except Exception as error:
                        logError(error)
                if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    if text is None:
                        return
                    elif text.lower() == 'token mac':
                        data = {
                            'nama': '{}'.format(msg._from),
                            'submit4': ''

                        }
                        post_response = requests.post(url = 'https://lazybot.us/snipz/', data = data)
                        qr = post_response.text
                        cl.sendMessage(msg.to, '{}'.format(qr))
                    elif text.lower() == 'token win10':
                        data = {
                            'nama': '{}'.format(msg._from),
                            'submit3': ''

                        }
                        post_response = requests.post(url = 'https://lazybot.us/snipz/', data = data)
                        qr = post_response.text
                        cl.sendMessage(msg.to, '{}'.format(qr))
                    elif text.lower() == 'token ios':
                        data = {
                            'nama': '{}'.format(msg._from),
                            'submit2': ''

                        }
                        post_response = requests.post(url = 'https://lazybot.us/snipz/', data = data)
                        qr = post_response.text
                        cl.sendMessage(msg.to, '{}'.format(qr))
                    elif text.lower() == 'token chrome':
                        data = {
                            'nama': '{}'.format(msg._from),
                            'submit1': ''

                        }
                        post_response = requests.post(url = 'https://lazybot.us/snipz/', data = data)
                        qr = post_response.text
                        cl.sendMessage(msg.to, '{}'.format(qr))
                    elif text.lower() == 'token done':
                        data = {
                            'nama': '{}'.format(msg._from),
                            'submit5': ''

                        }
                        post_response = requests.post(url = 'https://lazybot.us/snipz/', data = data)
                        qr = post_response.text
                        cl.sendMessage(msg.to, '{}'.format(qr))
                    elif msg.text in ["/ti/g/"]:
                        if wait["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = cl.findGroupByTicket(ticket_id)
                                cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                cl.sendMessage(to, "succes join to: %s" % str(group.name))
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mid in mention['M']:
                                if wait["tagg"] == True:
                                    ca = cl.getContact(sender)
                                    cl.sendMessage(to, "halo...☛❲ " + ca.displayName + "❳☚")
                                    cl.sendMessage(to, wait["teksp"])
                                    cl.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}" .format(str(ca.pictureStatus)))
                                else:
                                    pass
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mid in mention['M']:
                                if wait["tags"] == True:
                                    ca = cl.getContact(sender)
                                    cl.sendMessage(to, "halo...☛❲ " + ca.displayName + "❳☚")
                                    cl.sendMessage(to, wait["teksp"])
                                    cl.sendMessage(msg.to, None, contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                else:
                                    pass
                    if 'MENTION' in msg.contentMetadata.keys() != None:
                      if wait["Mentionkick"] == True:
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                             if mention ['M'] in mid:
                                cl.mentiontag(msg.to,[msg._from])
                                cl.sendMessage(msg.to, "Jangan Tag gw ...")
                                cl.kickoutFromGroup(msg.to, [msg._from])
                                break
                if msg.contentType == 7:
                    if wait["sticker"] == True:
                      msg.contentType = 0
                      cl.sendMessage(msg.to,"╔══════════════\n╠☛❲Check Sticker❳\n╠☛ STKID : " + msg.contentMetadata["STKID"] +"\n╠☛ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n╠☛ STKVER : " + msg.contentMetadata["STKVER"] + "\n╠☛ " + "line://shop/detail/" + msg.contentMetadata["STKPKGID"] +"\n╚══════════════")
                    else:
                        pass
                if msg.contentType == 16:
                    url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                    cl.like(url[25:58], url[66:], likeType=1001)
                    ka.like(url[25:58], url[66:], likeType=1001)
                    kb.like(url[25:58], url[66:], likeType=1001)
                    kc.like(url[25:58], url[66:], likeType=1001)
                    kd.like(url[25:58], url[66:], likeType=1001)
                    ke.like(url[25:58], url[66:], likeType=1001)
                if msg.contentType == 16:
                    try:
                       for posts in cl.activity(1)["result"]["posts"]:
                         if posts["postInfo"]["liked"] is False:
                            if wait["likeOn"] == True:
                               cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                               ka.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                               kb.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                               kc.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                               kd.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                               ke.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                               k1.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                               print ("Like")
                               if wait["commentOn"] == True:
                                  if posts["userInfo"]["writerMid"] in wait2["commentBlack"]:
                                     pass
                                  else:
                                      cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                                      ka.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                                      kb.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                                      kc.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                                      kd.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                                      k1.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                               else:
                                   pass
                    except:
                        pass
                if msg.contentType == 16:
                    if wait["Timeline"] == True:
                        try:
                            ret_ = "╔═══════[ Details Post ]"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(sender)
                                auth = "\n╠☛ Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\n╠☛ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                            purl = "\n╠☛URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                            ret_ += auth
                            ret_ += purl
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n╠☛ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n╠☛ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n╠☛ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n╠☛ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n╠☛ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n╠☛ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n╠☛ Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "text" in msg.contentMetadata:
                                text = "\n╠☛ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                ret_ += text
                            ret_ += "\n╚══════[ Finish ]"
                            cl.sendMessage(to, str(ret_))
                        except:
                            cl.sendMessage(to, "Post tidak valid")
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if wait["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "╔═══[ Detect Unsend Message ]═══\n╠☛ Sender :  "
                                ret_ = "╠☛ Group Name : {}".format(str(ginfo.name))
                                ret_ += "\n╠☛ Send at : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n╠☛ Message : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n╚══════════════════════"
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                del msg_dict[msg_id]
                    else:
                        cl.sendMessage(at,"SentMessage cancelled!!")
                except Exception as e:
                    print(e)
#================================#
        if op.type == 55:
            try:
                if op.param1 in wait2["readPoint"]:
                   if op.param2 in wait2["readMember"][op.param1]:
                       pass
                   else:
                       wait2["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if ciduk['cyduk'][op.param1]==True:
                if op.param1 in ciduk['ceadPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in ciduk['ceadMember'][op.param1]:
                        pass
                    else:
                        ciduk['ceadMember'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])

            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
                ka.like(url[25:58], url[66:], likeType=1001)
                kb.like(url[25:58], url[66:], likeType=1001)
                kc.like(url[25:58], url[66:], likeType=1001)
                kd.like(url[25:58], url[66:], likeType=1001)
#==============================================================================#
    except Exception as error:
        print (error)

while True:
    try:
        ops=oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        print(e)

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)
