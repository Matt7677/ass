import getpass

import amino

from uuid import uuid4

import requests

import threading

from threading import Thread

import json

from os import path

import os

 

ear=[]

t = open('email.txt','r')

for m in t.read().splitlines():

    temp=m

    # for fx in range(0,len(temp)):

    #     temp=temp[:len(temp)-1]

    ear.append(str(temp))

t.close

ep = input("email >> ")

senha = input("senha >>")

 

#client = amino.Client("2260C506B9DC4DCBC141EB0CD99441FAB4541721551866B5672D2FF4AE2616E7CABAE89FCFEED52E65")

headers={

        "cookies":"__cfduid=d0c98f07df2594b5f4aad802942cae1f01619569096",

        "authorization":"Basic NWJiNTM0OWUxYzlkNDQwMDA2NzUwNjgwOmM0ZDJmYmIxLTVlYjItNDM5MC05MDk3LTkxZjlmMjQ5NDI4OA=="

    }

 

def extra(fo:str):

    data = {

        "reward":{"ad_unit_id":"t00_tapjoy_android_master_checkinwallet_rewardedvideo_322","credentials_type":"publisher","custom_json":{"hashed_user_id":f"{fo}"},"demand_type":"sdk_bidding","event_id":None,"network":"facebook","placement_tag":"default","reward_name":"Amino Coin","reward_valid":"true","reward_value":2,"shared_id":"dc042f0c-0c80-4dfd-9fde-87a5979d0d2f","version_id":"1569147951493","waterfall_id":"dc042f0c-0c80-4dfd-9fde-87a5979d0d2f"},

        "app":{"bundle_id":"com.narvii.amino.master","current_orientation":"portrait","release_version":"3.4.33567","user_agent":"Dalvik\/2.1.0 (Linux; U; Android 10; G8231 Build\/41.2.A.0.219; com.narvii.amino.master\/3.4.33567)"},"date_created":1620295485,"session_id":"49374c2c-1aa3-4094-b603-1cf2720dca67","device_user":{"country":"US","device":{"architecture":"aarch64","carrier":{"country_code":602,"name":"Vodafone","network_code":0},"is_phone":"true","model":"GT-S5360","model_type":"Samsung","operating_system":"android","operating_system_version":"29","screen_size":{"height":2260,"resolution":2.55,"width":1080}},"do_not_track":"false","idfa":"7495ec00-0490-4d53-8b9a-b5cc31ba885b","ip_address":"","locale":"en","timezone":{"location":"Asia\/Seoul","offset":"GMT+09:00"},"volume_enabled":"true"}

        }

    event=uuid4()

    data["reward"]["event_id"]=f"{event}"

    try:

        requests.post("https://ads.tapdaq.com/v4/analytics/reward",json=data, headers=headers)

    except:

    	pass 

 c = 1

 

password= input("Password: ")

for n in c:

    try:

    	client=amino.Client()

    	client.login(email=e,password=senha)

    	#fo=client.userId

    	coins = client.get_wallet_info().totalCoins

    	#print(f"Coins Before the ad: {coins}")

    	fo=client.userId

    	for _ in range(150):

    	       try:

    	       	threading.Thread(target=extra,args=(fo,)).start()

    	       except:

    	       	pass

    	coins = client.get_wallet_info().totalCoins

    	print(f"Coins After ad {coins}")

    except Exception as e:

    	print(e)

    	pass
