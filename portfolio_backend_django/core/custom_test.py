# -*- coding: utf-8 -*-

# no need to check values in the middle of running codes and after running codes as the unit-test way,
# I wrote automatically running test codes not in the way.



import os
import sys
import threading
import time

from pathlib import Path

import redis

import django
from django.conf import settings
from django.test import RequestFactory

from pymongo import MongoClient



BASE_DIR = Path(__file__).resolve().parent.parent 
sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_backend.settings")
django.setup()

from core.views import *
from core.util import *



msg_prettifier = MessagePrettifier("util")



def initialize_setting():
    mongo_client = MongoClient(settings.MONGODB_HOST)
    personality_db = mongo_client["personality"] 
    character_a_personality_collection = personality_db["character_a"] 
    character_a_personality_collection.drop()

    redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)


    # automatically applying an atmoic transaction to rollback if something goes wrong.
    #
    # no need to explicitly write with sess.start_transaction():, 
    # sess.start_transaction() ~ sess.commit_transaction() ~ sess.end_transaction(),
    # because the code does not need a multi-document transaction, 
    # processing things together within the above statements.
    character_a_personality_collection.insert_one({
        '_id': 'LrYMUPsjtRw', 
        'subtitle': "3:28:01\n않을까요? 짠. 아 사장님 한 자치하셔만 열고자\n3:28:08\n짠 파이팅 짠 저희는 공겜이 좋아서 보러온게 아니고\n3:28:13\n공겜을 하는 희나님을 보러 온 거라 괜찮아요. 짠 히나님 저 배경 화면이 바뀌었네요.\n3:28:20\n방 리모델링 했나요? 짠. 아무래도 답답한 분들 T입니다. 게임 스토리는\n3:28:26\n다른 데서 보시고 여기서는 그냥 지국을 즐기시면 됩니다. 감사합니다. 짠. 아\n3:28:33\n히나이야 나는데 저녁도 하고 있을 것 같다. 눈 딱\n3:28:39\n까먹고 나가서 약 먹으면 되는데 왜 그게 힘들까 이렇게 배경 퀄리티\n3:28:44\n지린다. 같이 공포 게임 같은데. 짠. 저\n3:28:50\n약은 문명신 거야. 스나야\n3:28:56\n잠시 눈고 있을게. 히나가 알아서 비명으로 깨워줄 테니.\n3:29:03\n짠. 신나야 작년에 입대 안에 오늘 저녁한데 축하해 줘라.\n3:29:11\n짠. 이방 안 나가면 나랑 결혼하는 거다.\n3:29:16\n짠. 50년 계약 하는 법. 50년 동안 방송왕 뜨기.\n3:29:22\n짠. 도네가 예전에 지정등만큼 터지고 있어요. 크크크.\n3:29:28\n짠. 희나 사기생 나올 때도 이방에서 보고\n3:29:33\n있을듯. 크크크. 짠. 세상에서 제일 긴 1분.\n3:29:41\n저체 주제가 마구마구 생각나는 신나면 개추 크나\n3:29:48\n오늘 먹은 수박이 참 맛있어 170 넘지 않았으므로 비겁한 변명입니다. 히 병장님 돌격하십시오. 짠\n3:29:56\n신나야 어느새 대선배가 됐구나 벌써까지\n3:30:02\n나왔다니 대비했을 때가 엊그제 같은데 대신경\n3:30:08\n짠 대신 1분 지났어요 쫄보님 짠 절대 나가지 말아 줘 신야 나랑 평생\n3:30:16\n여기서 같이 있자 너무 행복해 짠\n3:30:22\n민 짠 아니야 신나야 좀만 더 있어줘 짠\n3:30:28\n희나의 공포 게임은 후회와 두려움이 반이다. 아 진짜 사장님이 같이 해주면 안 무서울 듯 진짜 사장님이\n3:30:35\n같이 안 무서울 사장님이 같이었으면 괜찮았을 듯. 내 사장님이 나 혼자\n3:30:42\n무서 문 열어라. 이응 이응. 오케이 알았어. 진짜 열개이 공김을 오래오래 볼 수 있다니 너무\n3:30:47\n좋구나. 짠 안녕 기나 데이7년에\n3:30:53\n진짜 몸 풀고 나갈게요. 이거 진짜 불안고 진짜 불러.이 이 진짜이 진짜 이제 더 이상 취면 안 되겠까? 아까\n3:31:00\n이제짠 미안하다. 나야 반응 진짜 개 맛있다. 하\n3:31:07\n짠 얘는 존쫄보의 급이 다르네이 정도면 신기한 수준인데.\n3:31:13\n잠깐만요.이 정도면 밖에 좀비복. 제일 못해요. 난 진행도 못해요.\n3:31:19\n티나님 이겜 첫날에 입대한다던 친구들 오늘 저녁해서 방송 보러 왔대요.\n3:31:27\n포디 대비 축하해요. 벌써대 30년이라니 축하해요.\n3:31:34\n짠 신박수 체크기가 없는게 너무 아쉬워요. 다음 공겜 what's\n3:31:39\n때. 아 신박수 체크 어떻해? 나 진짜 이거 이게 조속 5cm 나는 영화인가요?\n3:31:46\n짠. 아 일단 문 좀 풀고 나야 나 강지다. 짠 이건 무조건 이상 영상이거든요. 일단\n3:31:52\n녹소리도 사라졌고 TV가 켜져 있는데 제가 역시 계속 딜러 했는데 TV가 안 꺼져요 이거는\n3:32:00\n무조건 30초 뒤에 나갈게요. 1분 뒤에 진짜 나갈게요. 몸 풀고 진짜\n3:32:07\n나갈게요. 아 진짜 몸 다 풀었어. 거의 다 풀고 있어. 사장님은 이미이 상황이 즐겁다.\n3:32:13\n짠. 아니 안 즐거울까? 네. 여기 다 할까?\n3:32:18\n짠. 지금 같이 옆에 두고 싶은 사람 있어?\n3:32:23\n옆에 한번 확인해 봐. 있을 거야. 짠. 아무도 없잖아. 오케이. 이제 어깨 풀게요.\n3:32:30\n짠. 정보 희나는 TV가 켜져 있으면 방을 못 나간다. 짠.\n3:32:36\n희나야 나 강지는 아닌데 지금 너무 즐겁다. 화이팅해라.\n3:32:44\n짠. 일단 허리 여기가 그 바터스톤 현실판인가요? 오케이 여러분 허리 피세요.\n3:32:51\n배트 사장님은 보고 있지도 않다. 와 나 그러면 나 진짜 슬플 듯.\n3:32:57\n사장님이 오늘 전화해서 희나님 그럼 하기로 한 거죠? 자 오늘 사장님 후주에다도 보고\n3:33:05\n싶어요. 기게요. 이러 이래놓고 안 보고 있으면 진짜 상처일듯.이 이 난 이렇게 고통받고\n3:33:12\n있는데 나는 진짜 구글 TV 꺼져 짠 난 이렇게 고통 받고 있는데\n3:33:20\n오늘 하루를 아무것도 안 난지 너무 상다 디 안녕하세요 희나님 희나님은 할 수\n3:33:28\n있어요 파이팅입니다. 짠. 와, 내가 귀신이면 문앞에 캠프\n3:33:35\n설치하고 언제 나오는지 대기하고 있겠다. 역대급.\n3:33:40\n근데 여러분 그거 아세요? 이미 나가려면 초반에 나갔어야 됐어. 기나야 내가 보고 있잖아.\n3:33:45\n여기서 10분 뻥이니까 도았어. 고생 많았어. 문 열기가\n3:33:52\n꿈나라에서 꿀잠실듯. 나 나이 배워 하면 보지 마세요. 눈 마주칠 수도\n3:33:59\n있어요.지 갈게. 현실 도피하지만 쫄고 같아 보인다고\n3:34:05\n진짜\n3:34:15\n이거 빼면 안 되니까 한쪽만 뛸게. 짠. 누가 보면 방 안에서 안 나가는\n3:34:20\n히키코모리인 줄 알겠어요. 짠. 야, 쫄보.\n3:34:32\n제 갈게. 짠. 신나야.이 정도면 나 저 목 없는\n3:34:39\n애랑 친해진 것 같아. 짠. 신나야. 나 눈 감고 있다. 가고\n3:34:47\n있지. 짠. 위대한 적걸음. 짠.\n3:34:53\n히나문열 때까지 숨참음 흡이라고 써 있습니다. 짠.\n3:34:58\n이게 뭐라고? 이기생 DS. 짠.\n3:35:03\n비킹 연습 들어가자. 아니 약으로 치킹해야 돼.\n3:35:17\n짠. 미션 시간이 10분밖에 안 남았다는게 놀랍다.\n3:35:24\n짠. 그냥 빨리 나가 됐지야.\n3:35:31\n오케이. 진짜 갈게요. 아이씨 농담 안 하고 이제 갈 때 됐어. 이제 더\n3:35:37\n이상 더 이상 안 돼. 진짜 더 이상 안 돼. 문두드리다가 손가락 닦아졌겠다.\n3:35:43\n그 실제로 꼬개하셨어. 지금 소리가 안 나약 까먹었을까 봐 말하는 건데 약은 화장실 안에 있다.\n3:35:49\n웃기고 있네. 이씨 형가 있는 거 다 알거든. 자 환각이 사라지거나 원래대로\n3:35:55\n돌아오면 오케 데이 3 1시간으로 오케이 갈게 한각이 살지 않아야\n3:36:01\n근데 기절하는 거 조심하고 17번째 날조는 사라지지 않게요\n3:36:08\n오케고 그다음에 황장 시라유키 할머니님 벌써 1500개월째\n3:36:14\n구독이네요 항상 감사합니다. 짠 히나님 신박수 측정 올려 놓고\n3:36:20\n갈까요? 짠. 여기 아늑한데 좀만 더 있다가죠. 근데 그 기계 있어야 되는 거\n3:36:26\n아닌가? 모판 밖으로 꺼지라고. 짠. 신나야 나갈 때 꼭 섬광탄 까고\n3:36:34\n나가라. 짠. 신나 혼자서 평균 플레이 타임을\n3:36:40\n늘리고 있어. 아니 진짜 나올 거야. 잘 부탁.\n3:36:46\n근데이 방송은 대기방인가요? 감사합니다. 왜 계속 화면이 부록될까요?\n3:36:53\n비난하지 마. 짠. 조금만 히나야 고맙다. 무사히 대다리 왔다.\n3:36:58\n진 진짜 먹고 있을 테니 잘 다녀와. 짠 히나야 이러다가 스텔라이브\n3:37:04\n인도네시아도 나오겠다. 짠 이제 좀 나가자. 크크크. 몇\n3:37:10\n군요? 알았어. 아마. 와 신나야. 5,600원\n3:37:16\n갖고 얼마나 게임을 즐기는 거야? 부러워.\n3:37:23\n할 수 있다. 정인하고 가장 나가고 싶은 건 나야.\n3:37:28\n짠. 히나가 총만 들어서도 다 이기는데 아쉽네. 맨손이라. 크크크크크크크.\n3:37:35\n짠. 오케. 히나야 도시락 챙겼어. 가방에 빠뜨린 건 없고. 짠.\n3:37:41\n달리가 없어.이 문앞에 캠핑 중인데 진짜 나가. 짠.\n3:37:47\n캠핑 중이라고. 기다리면 갑자기 누가 문 열고 들어오지 않을까요?\n3:37:52\n짠. 히나야 잠깐만 혹시 우리 가습을 안 끈 거 아닐까? 짠.\n3:37:59\n여기는 하늘소 퇴근하고 싶소. 짠.\n3:38:04\n헤이리도 신나처럼 겁 먹을 때 아구몬이 용기네라고 응원해줬어.\n3:38:11\n우리가 아구몬을 대신해 줄게. 짠.\n3:38:17\n환불나기 챌린지입니다. 짠. 히나님 호재에 떠워 운영자님이 이제\n3:38:24\n30년 발 게임 섭종하게 해달라고\n3:38:29\n소개자하고 뛰는데 어떻게 할까요? 짠 오케이 진짜 갈게요. 오케이 진짜\n3:38:37\n갈게요. 오케이 진짜 갈게요. 오케이 진짜 갈게요. 하지만 뭐라\n3:38:43\n하지 마 뭐라 하지 마. 짠. 진짜 나갈게요. 20분 정도 더\n3:38:49\n하다가 밖에서 40분 동안 내가 진짜 나 왜 이렇게 태어났을까?\n3:38:56\n조금 귀신 친화정이게 타났으면 안 을까? 나갈게요. 오케이. 몸만 풀고 나갈게요. 오케이. 이제 진자\n3:39:02\n나갈게요. 오케이. 짠. 내 뱃속에 있는 아이가 벌써 이렇게\n3:39:10\n어여하게 컸어요. 대대손 응원할 테니 힘내세요.\n3:39:21\n짠 앙모띠 짠 나 여기서 뭐 뭐이 몇 분 있었어\n3:39:27\n바로 앞에 귀신 있다 야 진짜 그러면 하지 마 이거 다큐 3일 키고모리 편인가요\n3:39:34\n40분 이러고 있었다고요 30분 비난님 방안에서 심지어 47년이\n3:39:40\n지났네요 저희 아들이 이번에 딸을 낳았어요 축하해 주세요\n3:39:45\n짠 3라는게 혹시 리얼타임 3일인가\n3:39:50\n인가요? 짠.이 게임 플레이타임 30분데이\n3:39:56\n뜻이 없구나. 진짜 30분 안 내가요? 야, 참 미안해. 아무도 뭐라니\n3:40:01\n마음에 준비나 하시라고. 크크크. 짠.\n3:40:07\n히나의 짜장면 시켜줄까? 짜장면으로 다 죽여버리자.\n3:40:13\n짠. 신나야, 나 알리올리오 면삼고 있는데 10분만 더 기다려 줄 수 있을까?\n3:40:19\n짠. 난 너무 환영이 나 이제 나가도 된다. 귀신들 다 늙어 죽었다. 크\n3:40:24\n알았어 알았어. 어 대기 없네. 계속 여기 있자. 짠 정보 게임에서 나온 거 아무것도\n3:40:32\n없다는 거 아니 나왔어. 고맙습니다. 말이야. 그리고 이상한 사람들 다\n3:40:40\n발급까지 받았습니다. 대희 짠. 나간다 나간다 하고 제자리인 거 너무\n3:40:46\n귀엽다. 아 진짜 나갈 거야. 진짜 진심먹어 먹어진짜 약 먹을게 다시 약 먹게 아\n3:40:54\n나 진짜 나 그거 청심만 좀 먹고 할 거야 먹고 양모 먹어 양모 양 먹어 양 먹어\n3:41:00\n짠 30분이요 짠 오케이진짜 갈게요 게이진짜 갈게요\n3:41:07\n게이진 짜 갈게요 짜 귀신들 캐치 테이블로 예약하고 실어\n3:41:14\n갔다네요 짠 그래 이제 진짜 나올게 이렇게 가만히 있는 알크 알았어 알았어 진짜\n3:41:21\n심각수 대충 메모장으로 200 써서 쌀 먹게도 태안날 때 자\n3:41:28\n님 치킨 먹으면서 꼬려고 지금 달걀 부하기에 넣었습니다. 천천히 하세요.\n3:41:35\n잠깐 알았어. 나 진짜 이것만 하고. 즐기는구나. 신나야.\n3:41:40\n짠 오케이 짠. 신나야 방 나가면 살거나 죽거나인데\n3:41:47\n방은 안 좋네. 짠. 덕분에 치킨 도착해서 잘 먹고\n3:41:53\n있다. 짠. 네이 3 미션이 30분 시작이었다.\n3:41:59\n짠. 아니야, 너랑 나랑 언어 사전이 다른 거냐 나간다는게 내가 알고 있는 건\n3:42:07\n문을 열고 이동하는 건데. 대체 뭐지? 짠.\n3:42:13\n저 잠깐 졸다 왔는데 다행히 1분밖에 안 지났네요.\n3:42:18\n짠. 보고누나 밖에서 40분째 문두드리는 중후.\n3:42:23\n짠. 세계 최초 리버스 스피드론 1위 축하드립니다. 기나님\n3:42:30\n짠. 막간을 이용해 히나님 심장 소리도 들어보고 싶어요.\n3:42:36\n짠. 히나가 공개을 한시간 동안 플레이했대. 장하다 우리나.\n3:42:44\n짠. 나 한 시간이나 했어요. 아니 잠깐 이거 이거밖에 안 했는데 한 시간밖에 안 했어. 방에서 마음에\n3:42:50\n준비 중인 거니? 손호공이 드래곤볼 모으는 시간이 더 빠르겠다. 요즘에 시간이 진짜 빨리 가는 거\n3:42:56\n같아요. 난님 게임 최장 플레이네스 비로. 세우신 기념 소감이 어떠신가요?\n3:43:03\n짠. 히나야 분노를 채워서 용기를 얻자. 두 손으로 가슴으로 마구 두드리고\n3:43:11\n바닥 두번 황팡. 그건 고릴라잖아요. 우 고유함자.\n3:43:16\n짠. 히나야 진지하게 하기 싫으면 그냥 끄지. 짠.\n3:43:22\n히나야 오늘 지ád만도 배달았다. 짠. 이것은 한 명의 인간에게는 작은\n3:43:29\n발걸음이지만 인류에게는 위대한 도약이다. 짠.\n3:43:34\n알았다. 진짜 갈게. 아사라비아 콜롬비아. 아사라비아 콜롬비아. 아사라비아\n3:43:40\n콜롬비아. 아사라비아 콜롬비아. 상사라비아. 아사라비아 콜롬비아. 아사라비아\n3:43:47\n콜롬비아. 짠. 겨우 3년 겨우 그 나 약먹으러 간다.\n3:43:52\n짠. 지금 귀신도 희나 언제 나올까? 긴장 중임 선방치면 이일 때\n3:44:00\n짠 히나야 고맙다 너 게임 시작하고 치킨 시켰는데 방송 보면서 먹으라고\n3:44:06\n기다려줬구나 짠 셀프디주를 30분째 하시는 거 보고\n3:44:12\n있으니 안락한 기분이 드네요. 이것도 못 하면\n3:44:17\n희나의 전생인 시바연이라는 이야기가 있다. 나는 그 이야기를 좋아한다.\n3:44:23\n짠. 제가 딱 대비하기 전에 이익스프레스 타러 왔을 때 너무 무서웠지만 딱\n3:44:29\n이마인드로 했거든요. 이것도 못하면 이것도 무서워하면 데뷔는 어떻게 하려고?\n3:44:39\n그래서 이번에도 이것도 못하네.면 안전한데 굳이 학교로 나가야 할까?\n3:44:44\n짠. 히나 사장님 여기 전집 전이 너무 맛있어요. 단골 손님이 될 것\n3:44:50\n같아요. 짠. 진짜 도저히 혼자서는 진행 못 하겠다 싶으면 누구라도 불러볼까? 정\n3:44:57\n힘들면. 짠. 지금 치킨 시켜도 문 열기 전에 배다겠죠?\n3:45:02\n아니 누굴 부르면 분명히 일부 공개 이부인 줄 알았는데\n3:45:07\n끝까지 시킬 것 같아서 그냥 이게 나은 거 같아요. 귀신들도 빨리 끝내고 휴가 가야 된다고.\n3:45:13\n알았어. 짠. 알어 알았어. 알았어. 이상 현상 궁금한데. 조금만 보다가 약 먹어 볼까요?\n3:45:18\n짠. 어 미션 시간이 짠. 아 죄송합니다.\n3:45:25\n나 이제부터 런닝 뛰느라 30분은 화면 못 볼 텐데 나 빼고 이상 현상\n3:45:33\n구경하지 말아다워. 아지 진짜 배경이 신기하네요. 새로 뽑으신\n3:45:41\n거가요? [음악] 짠.\n3:45:48\n히나님 금만두만 15년 드시는 중인가요? 짠. 여기가 혹시 시간과 정신의 방인가요?\n3:45:56\n짠. 히나야 배달. 아 근데이 미지의 것이라 너무 무서운 거 같아. 진짜 미지라서\n3:46:04\n이게 인간의 공포는 뭐든지 미지에서 오거든요. 미지에 가서 오거든요. 혹시 방송을 갖춰서 하고 계신 걸\n3:46:11\n지금 방에서 한 발자국도 안 나가는 게임플레이로 표현하고 계신 건가요? 아니 진짜이 미지의 것이라서 진짜 더\n3:46:17\n훨씬 무서운 거야. 아니 이게 진짜 내가 아는 거면은 갈 텐데. 근데이\n3:46:24\n정말 미지의 공포가 이렇게 무서워요. 짠. 히나님 사기생 데뷔 방송 보셨나요?\n3:46:31\n진짜 대박이더라고요. 어 아직 보셨다고요? 야 역시 사장님의 보석함\n3:46:37\n공고 게임 한시간 버티기 성공하셨으니까 이제 다른 공포 게임 하셔도\n3:46:43\n되겠어요. 짠 나이겜 보면서 뭔 똥개인가 했는데\n3:46:50\n오늘 보니 각기다 크크크 진짜 재밌다. 아니 아무것도 안 했는데 어떻게\n3:46:56\n재밌어요? 나도 재 나도 재밌게 하고 싶은데 못 나가겠면서\n3:47:02\n[음악] 시간 들고 있는 거지 [음악]\n3:47:08\n어느새 2026년 1월 1일이 이내 피나야 새해복 많이 받아\n3:47:14\n짠 정이나 화이팅 정이나 화이팅 정이나\n3:47:19\n화이팅 정이나 화이팅 정이나 화이팅 정이나 화이팅 정이나 화이팅\n3:47:27\n정이나 화이팅 정이나 화이팅 정이나 화이팅 정이나 화이팅\n3:47:34\n짠 나도 지내가고 싶어 내가 지금 지내가고 싶어\n3:47:39\n아 알겠다 히나가 귀신이라 대기하고 있는 거지 짠 사장님 보고 계시죠 진짜 갑니다.\n3:47:47\n짠. 진짜 겨우 한시간 그에 비해 와놓으니 백성들이 감내해야 했던 고통은\n3:47:54\n짠 나 벌써 치킨 다 쳐먹어 버렸다.\n3:48:00\n너무 슬퍼. 아 지할게. 지하겠다고 알았다고 지정하겠다.\n3:48:07\n아직도 하루가 지났네. 역시 이래서 원한 18세구나.\n3:48:14\n짠 아까 혼자 돌아다니기 위험하단다.이\n3:48:20\n치고리타 치고리타 치고리타 중 하나를 데려가렴. 짠.\n3:48:26\n희나야 나 존만 잘게 나갈 때 깨워줘. 짠. 아 다들 뭐라 하지 말고\n3:48:32\n리을리은 크크 만치라고 리을리은 키읔키읔 짠 안녕하세요\n3:48:38\n호날두입니다. 희나님의 공개물 응원합니다. 수수\n3:48:44\n짠 시즌 65호 진짜 갈게요. 짠.이\n3:48:50\n게임이 클리어되지 않고 노방종으로 함께하는게 더 좋은 결과 같기도\n3:48:56\n난이 정도인지 몰랐는데 지금 귀신들이 플레이어가 방에서 안 나온다고 이상하다며 약을 먹고\n3:49:04\n있다네요. 짠 좀 짠 봐봐 봐봐 지금 나한테 눈치 주잖아\n3:49:11\n지금 이거 미안하네 이지는 또 언년이야 짠\n3:49:17\n오늘 이렇게 8시간은 다만 있을 예정인가요 짠 갑자기 철학적인 토론이 당기나요\n3:49:25\n갈게 가겠다고 가겠다고 나가면 되잖아 알았어 나갈게 모습 1년에 진짜 몇\n3:49:32\n번 못 보는거다 천천히 많이 즐겨라. 짠. 방송 보면서 치킨 먹으려고 이제\n3:49:39\n병어리 부화시켰는데 안 늦겠죠? 유유. 짠. 신나야 계속 보다 보니 지금 방이\n3:49:48\n안늑해 보인다. 짠. 넌 미지의 것이지 우린 미치는\n3:49:53\n것이다. 짠. 와 해둥이들 진짜 너무 하네. 지금\n3:49:58\n히나가 SOS 신호 보내는 중이잖아. 아 왜 이렇게 문을 여는이 그냥\n3:50:05\n이하면 왜 이렇게 어렵지? 열릴 거 같아서 진짜 개무서워진다.\n3:50:12\n진짜 아까 50분 전에 2일차였던 거 보고 다시 왔는데 아직 그때인가요?\n3:50:19\n짠. 갑자기 이체로 학성에서 세상과 싸우기\n3:50:24\n시작하는 정인. 짠. 오케이. 히나야 여기서 창면 그게 더\n3:50:29\n공포다. 정신 차리고 눈딱 감고 용기해 내야 돼. 바로 버튼 눌러. 파이팅.\n3:50:34\n오케이. 올드보이 안 보셨다더니 울드보이 사전 체험 중이신가요?\n3:50:40\n짠. 오늘 저시랑 해경 바꾸고 저 단거할\n3:50:46\n착각죠? 오라. 짠. 나가라고 나가라고 나가라고 나가라고\n3:50:53\n나가라고 나가라 나가라고 나가라고 알았어\n3:50:58\n알았다고 아 감사합니다. 고맙습니다. 얘들아. 회동해가\n3:51:06\n구독건 좋다. 짠. 한시간 밥만 더 있으면 데이트로 넘어가여 버티샘.\n3:51:12\n짠. 어 뭐 했다고 벌써 2,100년이야? 근데 여기는 아직도 이렇고 있네.\n3:51:19\n크. 짠. 크크크. 진짜 공포 영화 보는 거\n3:51:24\n같네. 서 갈게. 아 너무 밖을 안 봤어.\n3:51:29\n무조건 나가는 거 본다. 짠. 히나야. 한국 통일했대. 지금\n3:51:35\n사람들이 밖에 나가서 통일 만세 부르고 있는데. 아, 갈 거야. 아니, 무릎하지 마.\n3:51:40\n무릎하지 마. 무릎하지 마. 무릎하지 마. 갈 거야. 갈 거야. 잠깐. 너\n3:51:45\n저응시킨 거야. 너 너무 안 열어서 너시킨 거라고. 이\n3:51:51\n방송 모니터링 중이었으면 죽겠다. 아니, 눈만 시킨 거예요. 나갈\n3:51:56\n거예요. 다 희나요? 짠. 채팅 창만 보고 계시는데 공포이\n3:52:03\n아니라 저 채탄다 생각하면 되지 않을까요? [음악]\n3:52:10\n감사합니다. 감사합니다. 감사합니다.\n3:52:17\n짠. 아 진짜이 정도면 올라와서 민심한 정이라도\n3:52:22\n시키셔. 오케이. 짠. 나야 귀신 알바는 알바생이 기다리다가\n3:52:29\n지쳐서 집에 갔대. 컨트롤 확인. 직진 확인. 진짜 갈게.\n3:52:35\n빨리 달리는 거 확인. 빨리 달리는 거 안 되. 진짜 갈게. 어 시프트 누르면 좀 빨라지는 거 같은데.\n3:52:40\n알았어 진짜 갈게. 알았어 진짜 갈 아니 빨리 달리는 거 없다고 한 사람 누구야? 프 누르 빨리\n3:52:46\n달리잖아. 히나님이 갇치신 동안 기생이 보고\n3:52:52\n싶어요. 님짠. 뭐 문 밖으로 첫 거지라고\n3:52:59\n진짜 갈게. 짠 빨라 이게 보면서 먹으려고 시킨 KFC 치킨\n3:53:05\n여덟 조각 다 먹었는데 아직도 여기구나 이응이응. 근데 달리기가 있다는 거\n3:53:11\n자고 내일 다시 보기로 볼게요. 짠 오케이 얼마나 긴장했으면 자막에 오타했네.\n3:53:18\n크크크. 짠. 학나. 콧물 소리 나는 거 보니 진짜 무섭나 보네. 콧물 소리 나서 있죠.\n3:53:25\n짠. 안녕하세요. 궁개뮤입니다. 안녕하세요.\n3:53:31\n밖에 귀신들이 들을까 봐 속삭귀는 거임. 짠.\n3:53:36\n그냥 행복 버튼 누르고 이부 가는게 모두가 행복해지는 길 아닐까요?\n3:53:43\n나도 그렇게 생각해. 아이고 고맙습니다. 전설의 오빠님\n3:53:49\n너무 감사합니다 시뮬레이터였던 거 감사합니다. 짠 한평생이 지난 후 짠\n3:53:58\n내가 안 나가면 믿할 수 있는데 짠\n3:54:04\n진짜 나갈게요. 아 진짜 이건 진짜 이대로는 진짜 안 되겠다. 이거는 너무하다. 이거 진짜 짜증나고 나\n3:54:12\n진짜 나한테 실망해도 어쩔 수 없어. 그래서 내가 진짜\n3:54:19\n짠 나 갈게. 짠 진짜 갈게. 사랑하는 사람 이름 외지면서 모아\n3:54:26\n일단 구조 좀 익혀 뭐라 하면 그거 뭐라 한다고 안 나간다. 그냥 기다려라 이응이 이응.\n3:54:32\n짠. 수금 달달한데 그냥 방에 있죠.\n3:54:38\n짠. 히나야 나갈지 말지 채집 비티한테 물어보자.\n3:54:44\n짠. 앞으로 저 책 배경하면은 여기 방으로 하는게 어떤가요?\n3:54:49\n짠. 치즈 밀린 거라. 짠. 신나야 노래 부르면서 갈까?\n3:54:58\n짠. 노래 부르면서 가. 야 기다려줘서 고맙다. 알리올리오면 이 아 진짜 거예요. 아 진짜 눈\n3:55:04\n적응시키는 거야. 히나는 지금 간속하는 중인 답답해.\n3:55:10\n안될까? 나도 너무 미안하고 신경쓰는데\n3:55:15\n이렇게 답답해하면 나도 너무 슬치신태오카시모스\n3:55:23\n짠 치지직 아 여기는 답답지 그래 나도 이해 나도 때리고\n3:55:30\n싶었을 것 같아 시작했습니까 태둥이 형사 이제 시작했습니까 짠\n3:55:37\n안 무섭게 개많은 법 알려준다 방불 끄고 뱀소리 좀 키우면 된다. 희나야\n3:55:45\n감사 인사. 나 지금 불편하는데도이 모양인데 네가 그 말하면 어떡해? 다들이 위대한 한 걸음을 기억해라.\n3:55:52\n이응이 아이씨 신나야 하나도 안 답답하니까\n3:55:58\n네가 원하는 대로 해. 다른 사람들 말다위 신경 쓰지 마.\n3:56:04\n알았어. 죄송한데 알았으니 도배하지 말아주세요.\n3:56:10\n제가 쓰레기입니다. 그래요. 제가 쓰레기에요. 잠\n3:56:16\n열어드렸습니다. 갈테니까 이제 또 한시간 있다가 열게요. 짠.\n3:56:22\n그래도 문여는 거 성공했다. 한자네. 짠. 내가\n3:56:28\n뭐라하지 마. 뭐라하지 마. 몰라하지 마. 뭐라하지 마. 뭐라하지 마. 몰라하지 마. 짠.\n3:56:33\n사랑해 나야. 짠 내가 아 이방의 에어컨 컴퓨터폰만 있었어도\n3:56:40\n평생 있을 만 사이가 좋았다면 짠 공기 꿋꿋했는데 환기 좋았다.\n3:56:48\n짠 이것은 방구석 페인이 방에서 나가는 이야기다.\n3:56:55\n힘내 힘내 오케이 다들 나들 화이팅 한 마디만\n3:57:01\n해줘 나야 너 책상 아래에 누구 있는데 그럼 짠 그런 거 하지 말라고 냥 게임 켜놓고 아무것도 안 해도 돈\n3:57:07\n복사 되는데 뭐 하러 나감 냥 있는게 이득인데 나한테 화이팅하고 위로해 주면 나\n3:57:14\n진짜 연기 내볼게 안녕하세요 기난 저는 오후 10시\n3:57:21\n22분에 해둥이에요.이 이 도네가 나올 때쯤 희나님은 문여시는 걸\n3:57:27\n성공했을까요? 미래의 신에게 응원을 짠\n3:57:32\n신 화이팅 짠 희나야 슬슬 이나야 슬슬 이나야 슬슬\n3:57:40\n나야 슬 이런 거 말고 화이팅해 달라고 나 화이팅 짠\n3:57:46\n그럼 시프트 누르고 빨리 나가 짠 오케이 정인나 화이팅\n3:57:51\n짠 나 눈감마도을 열었다 닫았다 물치듯이 저게\n3:57:58\n짠. 하나. 배도 알 때 이렇게 피킹했으면 다 잡겠네.\n3:58:03\n둘. 짠. 근데 방 안에서만 있을 건데 의미 있니?\n3:58:09\n짠. 그래도 하루를 깨보자. 후 옆집 보고 공문 무공이 기까지\n3:58:15\n해관는 거구나. 이게 다 한국의 분들이 문제다. 짠.\n3:58:20\n둘. 짠. 파이팅.\n3:58:25\n짠. 집주인데요. 월세 밀렸으니까 나가 주세요.\n3:58:31\n오케이. 피나야 동료 부르면서 하면 좀 나아진데. 아기상어 또로 부르면서 앞으로 가보자.\n3:58:40\n갈게. 파이팅 해줬어. 팅. 얘들아 나가자\n3:58:45\n얘들아. 미안하고 히나는 여기서 사람이도 여기서 살게. 흐\n3:58:52\n밖으로 빨리 나가. 내가 나 죽어도 진짜 갈게. 나 죽으면 양지 바른 곳에 묻어줘.\n3:59:00\n심장 계약 연장해주세요. 짠.\n3:59:06\n본인이 45분 기다렸는데 한 눈판 순간 지나갈까 봐 딴짓 못하게. 각이 왔어. 나 필이 왔어.\n3:59:13\n짠. 그래서 이나야 사랑해. 이나야 사랑해 이나야 사랑해.이야 사랑해이 나야\n3:59:20\n사랑해. 짠. 그리고 공포는 상상일의 파이팅.\n3:59:26\n내가 많이 못 해줘서 미안한다. 만하면녀가 돼버리네.\n3:59:31\n짠. 한숨 자고 올테니까 문 나가면 비명\n3:59:36\n한번 질러서 깨워 줘요. 짠. 제가 한시간 전에 와서 잘 몰라서\n3:59:42\n그런데 지금 하고 있는게 방탈출 게임인가요? 아니요. 후즈.\n3:59:47\n나야. 나 빨래 개고 왔는데 아직 여기라 안심했다. 고맙다. 짠.\n3:59:53\n답답해 하지 말아 주세요. 저희는 이렇게 보는 것만으로도 행복합니다. 마음 단디 먹고 출발하세요.",
        'video_personality': '겁이 많고 쉽게 긴장하는 성격\n* 반복적으로 *“오케이 진짜 갈게요”*라고 말하면서도 실제로 나가지 못하고 주저하는 모습이 드러남.\n* 예: 3:38:293:39:02, 3:40:463:41:14, 3:52:29~3:52:46 구간 등에서 여러 번 “진짜 갈게”를 선언하지만 행동으로 옮기지 못함.\n* 공포를 “미지의 것이라 더 무섭다”라고 직접 설명(3:46:04~3:46:24)하는 부분에서도 낯선 것에 대한 두려움이 강하게 나타남.\n자신을 자책하는 성향\n* 게임 속에서 주저하는 자신을 두고 “제가 쓰레기입니다” (3:56:10~3:56:16)라고 표현.\n* 또한 “나한테 실망해도 어쩔 수 없어” (3:54:07~3:54:12)라고 말하며 자기비하적으로 상황을 받아들이는 모습이 보임.\n유머러스하고 자기과장적인 성격\n* 긴장된 상황을 우스꽝스럽게 풀어내려 함. 예: *“아사라비아 콜롬비아”*를 반복하며 분위기를 희화화(3:43:34~3:43:47).\n* *“세계 최초 리버스 스피드런 1위 축하드립니다”*라는 시청자 도네이션에 맞장구치는 듯 반응(3:42:23~3:42:30).\n* 3:52:17~3:52:29에서 “귀신 알바는 기다리다가 지쳐서 집에 갔다”라는 농담으로 긴장을 풀려는 모습.\n시청자와의 상호작용을 중요시하는 성격\n* 반복적으로 시청자의 도네이션과 채팅에 반응하며 웃거나 인정함.\n* 예: 3:40:32~3:40:40 “고맙습니다. 말이야. 그리고 이상한 사람들 다 발급까지 받았습니다”라며 도네이션에 맞춰 반응.\n* 3:57:01~3:57:14에서는 “나한테 화이팅하고 위로해 주면 나 진짜 연기 내볼게”라며 시청자의 응원에 크게 의지함.\n쉽게 미안함을 표현하는 성격\n* “아, 참 미안해” (3:39:563:40:01), “알았어, 죄송한데 알았으니 도배하지 말아주세요” (3:56:043:56:10) 등에서 보이듯 시청자에게 자주 사과함.\n* 자신이 행동을 미루는 것에 대해 “미안하고 신경쓰는데” (3:55:10~3:55:15)라고 해명하기도 함.\n집요하고 끈질긴 성격\n* 비록 겁을 먹고 망설이지만, 끝내는 “그래도 문 여는 거 성공했다” (3:56:22~3:56:28)라고 말하며 결국 시도해냄.\n* 오랜 시간 같은 장면에서 버티며 시청자와 함께 긴 시간을 견디는 모습 자체가 끈기를 보여줌 (3:38:29 ~ 3:59:53 전반에 걸쳐 반복).'
    })


    doc = character_a_personality_collection.find_one({'_id': 'LrYMUPsjtRw'})
    
    if doc == None:
        raise Exception('the doc is not found; check if the insertion worked well.')
    else:
        print(f'inserted:\n{msg_prettifier.prettify_json(doc)}')


    redis_client.delete('LrYMUPsjtRw')
    mongo_client.close()
    redis_client.close()



def test_request_to_django_with_not_cached_redis():
    initialize_setting()

    rf = RequestFactory()
    req = rf.get('/LrYMUPsjtRw')

    # check logs to see if this works well too.
    print(f'returned:\n{VideoPersonalityFetchViewWithRedisConnectionpool.as_view()(req, "LrYMUPsjtRw").content.decode("utf-8")}')  

    mongo_client.close()
    redis_client.close()



def test_request_to_django_with_cached_redis():
    initialize_setting()


    # a test for not cached redis.
    rf = RequestFactory()
    req = rf.get('/LrYMUPsjtRw')

    # check logs to see if this works well too.
    print(f'returned:\n{VideoPersonalityFetchViewWithRedisConnectionpool.as_view()(req, "LrYMUPsjtRw").content.decode("utf-8")}')  

    # wait for redis to cache the data.
    time.sleep(1)

    # a test for cached redis.
    rf = RequestFactory()
    req = rf.get('/LrYMUPsjtRw')

    # check logs to see if this works well too.
    print(f'returned:\n{VideoPersonalityFetchViewWithRedisConnectionpool.as_view()(req, "LrYMUPsjtRw").content.decode("utf-8")}')  

    mongo_client.close()
    redis_client.close()



def test_redis_optimistic_write_lock():
    def request_to_django_with_not_cached_redis():
        rf = RequestFactory()
        req = rf.get('/LrYMUPsjtRw') 

        prettifed_json = VideoPersonalityFetchViewWithRedisConnectionpool.as_view()(req, 'LrYMUPsjtRw').content.decode('utf-8')

        # check logs to see if this works well too.
        print(f'returned:\n{prettifed_json}')  
        
    initialize_setting()
    threads = [threading.Thread(target=request_to_django_with_not_cached_redis) for _ in range(2)]
    [t.start() for t in threads]
    [t.join() for t in threads]

    mongo_client.close()
    redis_client.close()



def test_application_performance_after_optimization():
    # to focus speed performance improvement done by database optimization, 
    # the code calls view functions and goes to databases,
    # which does not care network latency and etc.

    # to check if the values of e-s are too affected by overhead or not,
    # check if the speed of printing the values to the console is normal.
    # I have seen it normal so far.
   
    # the average of the values of e-s can vary.
    # it is recommended to measure the average many times.

    def request_to_django_with_default_mongodb():
        rf = RequestFactory()
        req = rf.get('/LrYMUPsjtRw')

        s = time.time()
        VideoPersonalityFetchViewWithDefaultMongoDB.as_view()(req, "LrYMUPsjtRw").content.decode("utf-8")
        e = time.time()

        print(e-s)
        elapsed_time_list.append(e-s)

    def request_to_django_with_connection_pool_mongodb():
        rf = RequestFactory()
        req = rf.get('/LrYMUPsjtRw')

        s = time.time()
        VideoPersonalityFetchViewWithMongoDBConnectionpool.as_view()(req, "LrYMUPsjtRw").content.decode("utf-8")
        e = time.time()

        print(e-s)
        elapsed_time_list.append(e-s)

    def request_to_django_with_connection_pool_mongodb_and_redis():
        rf = RequestFactory()
        req = rf.get('/LrYMUPsjtRw')

        s = time.time()
        VideoPersonalityFetchViewWithRedisConnectionpool.as_view()(req, "LrYMUPsjtRw").content.decode("utf-8")
        e = time.time()

        print(e-s)
        elapsed_time_list.append(e-s)


    NUM_OF_REQUESTS = 8000
    
    def test_default_mongodb_performance():
        threads = [threading.Thread(target=request_to_django_with_default_mongodb) for _ in range(NUM_OF_REQUESTS)]
        [t.start() for t in threads]
        [t.join() for t in threads]

        print('==========')
        print(f'sum of elapsed_time_list: {sum(elapsed_time_list)}')
        print(f'num of elapsed_time_list(excluding error requests due to running out of ephemeral ports): {len(elapsed_time_list)}')
        print(f'avg of elapsed_time_list: {sum(elapsed_time_list)/len(elapsed_time_list)}')
        elapsed_time_list.clear()

    def test_mongodb_with_connection_pool_performance():
        threads = [threading.Thread(target=request_to_django_with_connection_pool_mongodb) for _ in range(NUM_OF_REQUESTS)]
        [t.start() for t in threads]
        [t.join() for t in threads]

        print('==========')
        print(f'sum of elapsed_time_list: {sum(elapsed_time_list)}')
        print(f'num of elapsed_time_list(excluding error requests due to running out of ephemeral ports): {len(elapsed_time_list)}')
        print(f'avg of elapsed_time_list: {sum(elapsed_time_list)/len(elapsed_time_list)}')
        elapsed_time_list.clear()

    def test_redis_with_connection_pool_performance():
        # this is warm-up to make enough connections to make a proper connection pool.
        threads = [threading.Thread(target=request_to_django_with_connection_pool_mongodb_and_redis) for _ in range(NUM_OF_REQUESTS)]
        [t.start() for t in threads]
        [t.join() for t in threads]
        elapsed_time_list.clear()

        # this uses the connection pool now.
        threads = [threading.Thread(target=request_to_django_with_connection_pool_mongodb_and_redis) for _ in range(NUM_OF_REQUESTS)]
        [t.start() for t in threads]
        [t.join() for t in threads]

        print('==========')
        print(f'sum of elapsed_time_list: {sum(elapsed_time_list)}')
        print(f'num of elapsed_time_list(excluding error requests due to running out of ephemeral ports): {len(elapsed_time_list)}')
        print(f'avg of elapsed_time_list: {sum(elapsed_time_list)/len(elapsed_time_list)}')
        elapsed_time_list.clear()


    initialize_setting()
    elapsed_time_list = []

    # to check if initialize_setting() prints well.
    time.sleep(1) 

    # the degree of optimization goes stronger from above to below.
    # uncomment each function to test each function one at a time; each test is independent on each other.
    # test_default_mongodb_performance()
    # test_mongodb_with_connection_pool_performance()

    # mongodb already uses its connection pool and redis uses its own now.
    # the performance betters when on bare-metal rather than virtual machine, due to hypervisor overhead.
    test_redis_with_connection_pool_performance() 

    mongo_client.close()
    redis_client.close()



# uncomment each function to test each function one at a time; each test is independent on each other.

# test the function separately, 
# or you can use it to initialize before running server through manage.py.
# initialize_setting()

# test_request_to_django_with_not_cached_redis()
# test_request_to_django_with_cached_redis()

# keep trying until the lock happens.
# test_redis_optimistic_write_lock()

test_application_performance_after_optimization()



# because implementing below test cases do not bring advantages, the code does not implement:
# a case of an invalidated cache after its expire time in redis,
# a case of requesting other urls except for '/LrYMUPsjtRw'
# 
# because it is hard to implement below test cases, the code does not implement:
# each thread requests each django request for the same url, but gets each different data returned from django,
# because the requests are being done in the middle of updating the same document/record in mongodb.

