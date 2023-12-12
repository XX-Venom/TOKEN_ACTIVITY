import aiohttp
import cloudscraper
import random
import json
import time
import sys
import asyncio
import os
import string
import httpx,os,threading
import requests
import re
import gmailnator
from time import gmtime, strftime
from bs4 import BeautifulSoup
from src.getuseragent import User_Agent
from colorama import Fore, init
from datetime import datetime
from onest_captcha import OneStCaptchaClient
data_ora_curenta = datetime.now()
format_data_ora = data_ora_curenta.strftime("%H:%M:%Y")

init()
class Client:
    def __init__(self, use_proxy, auth_token):
        self.datas = strftime("%H:%M:%S", gmtime())
        self.use_proxy = use_proxy
        self.session = aiohttp.ClientSession()
        self.csrf_token = ''
        self.user_agent_ = User_Agent.make_random_user_agent()
        self.auth_token = auth_token
        self.timeouts = 30
        self.token_capcha_site_key = '0152B4EB-D2DC-460A-89A1-629838B529C9'
        self.home_data = []
        self.cookies = {
            'auth_token': self.auth_token,
        }
        self.headers = {
            'authority': 'twitter.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://twitter.com/',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Opera";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0',
        }
    async def get_proxy(self):
        self.proxy = None
        if self.use_proxy == True:
            try:
                with open('src/proxies.txt', 'r', encoding='utf-8') as file:
                    data = file.read().split()
                    self.proxy = random.choice(data)
                    self.proxy = 'http://' + self.proxy
                    # print(f'> [{self.username}:{self.password}] -- The current USER')
                    # response = await self.session.get('https://api.ipify.org?format=json', proxy=self.proxy, timeout=5)
                    # response = await response.json()
                    # print(f'> [{self.username}:{self.password}] -- The current proxy is : {response["ip"]}')
            except Exception as e:
                print('Please wait to change proxy...  ' + str(e))
                await self.get_proxy()
                
       
       
    async def set_list_comment(self):
        lines = []
        with open('src/comments.txt', 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(line.rstrip())
        r = random.choice(lines)
        
        if '><' in str(r):
            message = r.replace('><', '\n')
        else:
            message = r
        
        return message
    
    
    async def set_list_reply(self):
        lines = []
        with open('src/reply.txt', 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(line.rstrip())
        r = random.choice(lines)
        
        if '><' in str(r):
            message = r.replace('><', '\n')
        else:
            message = r
        
        return message   
      
      
    async def number_succes(self):
        try:
            nume_fisier = 'succes_activity.txt'
            with open(nume_fisier, 'r', encoding="utf-8") as f:
                numar_linii = sum(1 for line in f) 
            return numar_linii
        except:
            return 0
      
      
                
    async def get_ct0(self):
        cookies = self.cookies.copy()
        headers = self.headers.copy()   
        async with aiohttp.ClientSession() as session:
            async with session.get('https://twitter.com/i/api/1.1/account/update_profile.json', cookies=self.cookies, headers=self.headers, proxy=self.proxy,timeout=self.timeouts) as response:
                cookie_jar = response.cookies
                ct0 = cookie_jar.get('ct0')
                cookies['ct0'] = str(ct0.value)
                headers['x-csrf-token'] = str(ct0.value)
                self.xcsrftoken = str(ct0.value)
                self.cookies = cookies
                self.headers = headers
    
    
    
    
    async def get_feed_info(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Referer': 'https://twitter.com/home',
            'x-csrf-token': self.xcsrftoken,
            'x-twitter-client-language': 'en',
            'x-twitter-active-user': 'yes',
            'Origin': 'https://twitter.com',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'Connection': 'keep-alive',
        }
        json_data = {
            'variables': {
                'count': 20,
                'includePromotedContent': True,
                'latestControlAvailable': True,
                'requestContext': 'launch',
                'withCommunity': True,
            },
            'features': {
                'responsive_web_graphql_exclude_directive_enabled': True,
                'verified_phone_label_enabled': False,
                'responsive_web_home_pinned_timelines_enabled': True,
                'creator_subscriptions_tweet_preview_api_enabled': True,
                'responsive_web_graphql_timeline_navigation_enabled': True,
                'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
                'c9s_tweet_anatomy_moderator_badge_enabled': True,
                'tweetypie_unmention_optimization_enabled': True,
                'responsive_web_edit_tweet_api_enabled': True,
                'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
                'view_counts_everywhere_api_enabled': True,
                'longform_notetweets_consumption_enabled': True,
                'responsive_web_twitter_article_tweet_consumption_enabled': False,
                'tweet_awards_web_tipping_enabled': False,
                'freedom_of_speech_not_reach_fetch_enabled': True,
                'standardized_nudges_misinfo': True,
                'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': True,
                'longform_notetweets_rich_text_read_enabled': True,
                'longform_notetweets_inline_media_enabled': True,
                'responsive_web_media_download_video_enabled': False,
                'responsive_web_enhance_cards_enabled': False,
            },
            'queryId': '5iHgyPJ0aB3NzaQYPa9-og',
        }
        # json_data = json.dumps(json_data)
        response  =  await self.session.post('https://twitter.com/i/api/graphql/5iHgyPJ0aB3NzaQYPa9-og/HomeTimeline',json=json_data, cookies=self.cookies, headers=headers, proxy=self.proxy,timeout=self.timeouts)      
        json_data = await response.json()
        entries = json_data["data"]["home"]["home_timeline_urt"]["instructions"][0]["entries"]
        for data in entries:
            try:
                tweet_rest_id = data["content"]["itemContent"]["tweet_results"]["result"]["rest_id"]
                user_rest_id = data["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]["rest_id"]
                if user_rest_id not in str(self.home_data):
                    self.home_data.append({"user_id": user_rest_id, "tweet_id": tweet_rest_id})
            except:
                pass
                
    async def send_fallow(self, user_id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-csrf-token': self.xcsrftoken,
            'x-twitter-client-language': 'en',
            'x-twitter-active-user': 'yes',
            'Origin': 'https://twitter.com',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'Connection': 'keep-alive',
        }
        
        data = {
                'include_profile_interstitial_type': '1',
                'include_blocking': '1',
                'include_blocked_by': '1',
                'include_followed_by': '1',
                'include_want_retweets': '1',
                'include_mute_edge': '1',
                'include_can_dm': '1',
                'include_can_media_tag': '1',
                'include_ext_has_nft_avatar': '1',
                'include_ext_is_blue_verified': '1',
                'include_ext_verified_type': '1',
                'include_ext_profile_image_shape': '1',
                'skip_status': '1',
                'user_id': user_id,
            }
        response  =  await self.session.post('https://twitter.com/i/api/1.1/friendships/create.json',data=data, cookies=self.cookies, headers=headers, proxy=self.proxy,timeout=self.timeouts)  
        if response.status == 200:
            json_data = await response.json()
            return json_data['screen_name']
        else:
            return False
            
    async def like(self, post_id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json',
            'Referer': 'https://twitter.com/home',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-csrf-token': self.xcsrftoken,
            'x-twitter-client-language': 'en',
            'x-twitter-active-user': 'yes',
            'Origin': 'https://twitter.com',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'Connection': 'keep-alive',
        }
        json_data = {
            'variables': {
                'tweet_id': post_id,
            },
            'queryId': 'lI07N6Otwv1PhnEgXILM7A',
        }
        response  =  await self.session.post('https://twitter.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet',json=json_data, cookies=self.cookies, headers=headers, proxy=self.proxy,timeout=self.timeouts)  
        if response.status == 200:
           json_data = await response.json()
           if 'Done' in str(json_data):
               return True
        else:
            return False
     
     
     
    async def tweet(self):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Content-Type': 'application/json',
                'Referer': 'https://twitter.com/compose/tweet',
                'x-twitter-auth-type': 'OAuth2Session',
                'x-csrf-token':self.xcsrftoken,
                'x-twitter-client-language': 'en',
                'x-twitter-active-user': 'yes',
                'Origin': 'https://twitter.com',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                'Connection': 'keep-alive',
               
            }
        json_data = {
            'variables': {
                'tweet_text': await self.set_list_comment(),
                'dark_request': False,
                'media': {
                    'media_entities': [],
                    'possibly_sensitive': False,
                },
                'semantic_annotation_ids': [],
            },
            'features': {
                'c9s_tweet_anatomy_moderator_badge_enabled': True,
                'tweetypie_unmention_optimization_enabled': True,
                'responsive_web_edit_tweet_api_enabled': True,
                'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
                'view_counts_everywhere_api_enabled': True,
                'longform_notetweets_consumption_enabled': True,
                'responsive_web_twitter_article_tweet_consumption_enabled': False,
                'tweet_awards_web_tipping_enabled': False,
                'responsive_web_home_pinned_timelines_enabled': True,
                'longform_notetweets_rich_text_read_enabled': True,
                'longform_notetweets_inline_media_enabled': True,
                'responsive_web_graphql_exclude_directive_enabled': True,
                'verified_phone_label_enabled': False,
                'freedom_of_speech_not_reach_fetch_enabled': True,
                'standardized_nudges_misinfo': True,
                'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': True,
                'responsive_web_media_download_video_enabled': False,
                'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
                'responsive_web_graphql_timeline_navigation_enabled': True,
                'responsive_web_enhance_cards_enabled': False,
            },
            'queryId': 'I_J3_LvnnihD0Gjbq5pD2g',
        }
        
        response  =  await self.session.post('https://twitter.com/i/api/graphql/I_J3_LvnnihD0Gjbq5pD2g/CreateTweet',json=json_data, cookies=self.cookies, headers=headers, proxy=self.proxy,timeout=self.timeouts) 
        if response.status == 200:
            response_json = await response.json()
            if 'errors' in str(response_json):
                msj = response_json['errors'][0]['message']
                return {'status':False, "message": msj}
            else:
                msj = response_json['data']['create_tweet']['tweet_results']['result']['legacy']['conversation_id_str'] 
                return {'status':True, "message": msj}
        else:
            return False
       
     
    async def send_retweet(self, tweet_id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'content-type': 'application/json',
            'X-Client-UUID': 'f67fcc08-3807-4f68-b5a1-57b04ea7750e',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-csrf-token': self.xcsrftoken,
            'x-twitter-client-language': 'en',
            'x-twitter-active-user': 'yes',
            'x-client-transaction-id': '4Se4CWOhsOf8WlvcSfKAyLwVHaGgsIr3B5AGV5kMVvEa9CqukRYJsAlUgIXC2Rl+Z5PPyOCbxMznnbM3W7LSTU8vBlzU4A',
            'Origin': 'https://twitter.com',
            'Connection': 'keep-alive',
            'Referer': 'https://twitter.com/home',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
           
        }
        json_data = {
            'variables': {
                'tweet_id':tweet_id,
                'dark_request': False,
            },
            'queryId': 'ojPdsZsimiJrUGLR1sjUtA',
        }
        response  =  await self.session.post('https://twitter.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet',json=json_data, cookies=self.cookies, headers=headers, proxy=self.proxy,timeout=self.timeouts) 
        if response.status == 200:
            response_json = await response.json()
            if 'errors' in str(response_json):
                msj = response_json['errors'][0]['message']
                return {'status':False, "message": msj}
            else:
                msj = response_json['data']['create_retweet']['retweet_results']['result']['rest_id'] 
                return {'status':True, "message": msj}

        
     
    async def send_reply(self,in_reply_to_tweet_id):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Content-Type': 'application/json',
                'Referer': 'https://twitter.com/compose/tweet',
                'X-Client-UUID': '64f1bb1c-e5a0-4497-8372-6332a32ad0d1',
                'x-twitter-auth-type': 'OAuth2Session',
                'x-csrf-token': self.xcsrftoken,
                'x-twitter-client-language': 'en',
                'x-twitter-active-user': 'yes',
                'x-client-transaction-id': 'I3jpWYa+5PiBf9VI7TFNtjtgKODJ1hYJ1qubUEYaCOKYLjJvDbJRmR8+w+VQ20ybREMXCiIoH+VtZfY9evZWbHdiBX4QIg',
                'Origin': 'https://twitter.com',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
                'Connection': 'keep-alive',
               
            }
     
        json_data = {
            'variables': {
                'tweet_text': await self.set_list_reply(),
                'reply': {
                    'in_reply_to_tweet_id': in_reply_to_tweet_id,
                    'exclude_reply_user_ids': [],
                },
                'dark_request': False,
                'media': {
                    'media_entities': [],
                    'possibly_sensitive': False,
                },
                'semantic_annotation_ids': [],
            },
            'features': {
                'c9s_tweet_anatomy_moderator_badge_enabled': True,
                'tweetypie_unmention_optimization_enabled': True,
                'responsive_web_edit_tweet_api_enabled': True,
                'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
                'view_counts_everywhere_api_enabled': True,
                'longform_notetweets_consumption_enabled': True,
                'responsive_web_twitter_article_tweet_consumption_enabled': False,
                'tweet_awards_web_tipping_enabled': False,
                'responsive_web_home_pinned_timelines_enabled': True,
                'longform_notetweets_rich_text_read_enabled': True,
                'longform_notetweets_inline_media_enabled': True,
                'responsive_web_graphql_exclude_directive_enabled': True,
                'verified_phone_label_enabled': False,
                'freedom_of_speech_not_reach_fetch_enabled': True,
                'standardized_nudges_misinfo': True,
                'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': True,
                'responsive_web_media_download_video_enabled': False,
                'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
                'responsive_web_graphql_timeline_navigation_enabled': True,
                'responsive_web_enhance_cards_enabled': False,
            },
            'queryId': 'I_J3_LvnnihD0Gjbq5pD2g',
        }

        response  =  await self.session.post('https://twitter.com/i/api/graphql/I_J3_LvnnihD0Gjbq5pD2g/CreateTweet',json=json_data, cookies=self.cookies, headers=headers, proxy=self.proxy,timeout=self.timeouts) 
        if response.status == 200:
            response_json = await response.json()
            if 'errors' in str(response_json):
                msj = response_json['errors'][0]['message']
                return {'status':False, "message": msj}
            else:
                msj = response_json['data']['create_tweet']['tweet_results']['result']['rest_id'] 
                return {'status':True, "message": msj}

    async def login(self):
        try:
            response = await self.get_ct0()
            tweet = await self.tweet()
            msg = tweet['message']
            if tweet['status']:
                print(f'{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE} {await self.number_succes()} {Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX}{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE}{self.datas}{Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX} [ {Fore.GREEN}SUCCES{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}AUTH: {self.auth_token[:10]}{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX} TWEET {Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}{msg}{Fore.LIGHTYELLOW_EX} ] ')
            else:
                print(f'{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE} {await self.number_succes()} {Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX}{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE}{self.datas}{Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX} [ {Fore.RED}ERROR{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}AUTH: {self.auth_token[:10]}{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX} TWEET {Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}{msg}{Fore.LIGHTYELLOW_EX} ] ')
            response = await self.get_feed_info()
            count = 0
            if len(self.home_data) > 0:
                for line in self.home_data[:10]:
                    count+=1
                    user_id = line['user_id']
                    tweet_id = line['tweet_id']
                    response = await self.send_fallow(user_id)
                    if response:
                        print(f'{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE} {await self.number_succes()} {Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX}{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE}{self.datas}{Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX} [ {Fore.GREEN}SUCCES{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}{count}{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}AUTH: {self.auth_token[:10]}{Fore.LIGHTYELLOW_EX} ] [ {Fore.MAGENTA} FALLOW {Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}SCREEN NAME: {Fore.YELLOW }{response}{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}USER ID: {user_id}{Fore.LIGHTYELLOW_EX} ]')
                    response = await self.like(tweet_id)
                    if response:
                        print(f'{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE} {await self.number_succes()} {Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX}{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE}{self.datas}{Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX} [ {Fore.GREEN}SUCCES{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}{count}{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}AUTH: {self.auth_token[:10]}{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTMAGENTA_EX} -LIKE- {Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}USER ID: {user_id}{Fore.LIGHTYELLOW_EX} ]')
                    re_tweet = await self.send_retweet(tweet_id)
                    msg = re_tweet['message']
                    if re_tweet['status']:
                        print(f'{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE} {await self.number_succes()} {Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX}{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE}{self.datas}{Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX} [ {Fore.GREEN}SUCCES{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}AUTH: {self.auth_token[:10]}{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX} RE_TWEET {Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}{msg}{Fore.LIGHTYELLOW_EX} ] ')
                    else:
                        print(f'{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE} {await self.number_succes()} {Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX}{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE}{self.datas}{Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX} [ {Fore.RED}ERROR{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}AUTH: {self.auth_token[:10]}{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX} RE TWEET {Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}{msg}{Fore.LIGHTYELLOW_EX} ] ')
                    create_tweet = await self.send_reply(tweet_id)
                    msg = create_tweet['message']
                    if create_tweet['status']:
                        print(f'{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE} {await self.number_succes()} {Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX}{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE}{self.datas}{Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX} [ {Fore.GREEN}SUCCES{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}AUTH: {self.auth_token[:10]}{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX} REPLY {Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}{msg}{Fore.LIGHTYELLOW_EX} ] ')
                    else:
                        print(f'{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE} {await self.number_succes()} {Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX}{Fore.LIGHTYELLOW_EX} [ {Fore.BLUE}{self.datas}{Fore.LIGHTYELLOW_EX} ]{Fore.LIGHTYELLOW_EX} [ {Fore.RED}ERROR{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}AUTH: {self.auth_token[:10]}{Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX} REPLY {Fore.LIGHTYELLOW_EX} ] [ {Fore.LIGHTCYAN_EX}{msg}{Fore.LIGHTYELLOW_EX} ] ')
                    await asyncio.sleep(1)
                self.home_data = []        
                count = 0
            self.home_data = []   

            with open('succes_activity.txt', 'a', encoding="utf-8") as f:
                f.write(f'{self.auth_token}\n')                
        
        
        except Exception as e:
            print(f'{Fore.RED} ERROR:  {e} {Fore.RESET}')
            pass
    async def close(self):
        if self.session:
            if not self.session.closed:
                await self.session.close()
            