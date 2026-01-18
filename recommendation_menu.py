import streamlit as st
import random
import time
import datetime

today = datetime.datetime.now().strftime("%Y-%m-%d")
st.set_page_config(page_title=f"{today} 점메추", layout="wide", page_icon="🍚")

# 1. 10,000원
stores_10k = {
    "샤브로21": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250228_225%2F1740709796246qckvp_JPEG%2F1000022478.jpg",
        "cat": "샤브샤브",
        "url": "https://map.naver.com/p/search/%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%EC%83%A4%EB%B8%8C%EB%A1%9C21/place/1587597181?placePath=/home?bk_query=%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%EC%83%A4%EB%B8%8C%EB%A1%9C21&entry=pll&from=map&fromNxList=true&fromPanelNum=2&timestamp=202601180219&locale=ko&svcName=map_pcv5&searchText=%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%EC%83%A4%EB%B8%8C%EB%A1%9C21&searchType=place",
    },
    "손으로피자": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20220720_157%2F1658301156950VwVce_JPEG%2F%25BF%25A5%25BA%25ED%25B7%25B31.jpg",
        "cat": "피자",
        "url": "https://map.naver.com/p/entry/place/1430940357?lng=126.9499143&lat=37.4812754&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "홍시원": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200101_48%2F1577885236820qbPuX_JPEG%2FxHoo5ClP0CPGx0tPSaMHnMWA.jpg",
        "cat": "중식",
        "url": "https://map.naver.com/p/entry/place/1675322701?lng=126.9475864&lat=37.4812817&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601180254&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "군산아구찜": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240716_49%2F1721117412213I2YBR_JPEG%2FKakaoTalk_Photo_2024-07-12-15-37-45-4.jpeg",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/1480500276?lng=126.9473161&lat=37.4811015&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601180255&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "석양식당": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250531_225%2F1748679755103MaUWw_JPEG%2FIMG_5968.jpeg",
        "cat": "돈가스",
        "url": "https://map.naver.com/p/entry/place/1636441630?lng=126.9473797&lat=37.481223&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601180257&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "청진동감자탕순대국": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230120_160%2F1674144243838ovIUa_JPEG%2F997CD13F-3B2C-490A-9A38-9F44F1D5AA63.jpeg", # 가게 사진
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/1926841969?lng=126.9477377&lat=37.4812644&placePath=%2Fhome&searchType=place&c=15.00,0,0,0,dh",
    },
    "카도야라멘": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250717_162%2F1752755896043roH88_JPEG%2FIMG_2660.jpeg",
        "cat": "라멘",
        "url": "https://map.naver.com/p/entry/place/38276362?lng=126.9513001&lat=37.4816764&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "정자네": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230917_198%2F1694938900052AqT7B_JPEG%2F1694938877942.jpg",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/1559560115?lng=126.9470224&lat=37.481153&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601180303&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "오니": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250629_298%2F17511661557134mwco_JPEG%2FIMG_2784.jpeg",
        "cat": "오니기리",
        "url": "https://map.naver.com/p/entry/place/1784547468?lng=126.9509012&lat=37.4804168&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601180305&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "뜸들이다": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200926_173%2F1601073979588ER769_JPEG%2FakuH1ku0-lrZrk0Vh4XUZwve.jpeg.jpg",
        "cat": "덮밥",
        "url": "https://map.naver.com/p/entry/place/1221670362?lng=126.9512359&lat=37.4802634&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601180306&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "충칭마라훠궈": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20241220_221%2F1734692184018clwKk_JPEG%2Fimage.jpg",
        "cat": "중식",
        "url": "https://map.naver.com/p/entry/place/1025641913?lng=126.9551296&lat=37.4796145&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601180313&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "그릴하우스": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250929_196%2F1759126747669cs7Ws_JPEG%2F%25BD%25A1%25BA%25D2%25BE%25E7%25B3%25E4%25B1%25B8%25C0%25CC2.jpg",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/1928441811?lng=126.9561448&lat=37.4783792&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601180330&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "파앤피파스타하우스": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240327_4%2F1711518534588BHtXe_JPEG%2FKakaoTalk_20240327_144016285_02.jpg",
        "cat": "양식",
        "url": "https://map.naver.com/p/entry/place/1303035400?lng=126.9569967&lat=37.4785972&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "누들하우스": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200119_95%2F1579417367409P19TR_JPEG%2FyMTfS96JgOQr306KCpOzFpMu.jpg",
        "cat": "라멘",
        "url": "https://map.naver.com/p/entry/place/1805570237?lng=126.9573891&lat=37.4778213&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "밥한끼": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200622_27%2F1592825501669vngWY_JPEG%2FebpTj_qE7AohLIFQGp_oeFzk.jpg",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/1816360299?lng=126.9530669&lat=37.4780739&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181739&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "하이보": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200613_29%2F1592009911606yufd2_JPEG%2FU8lZRW6VfB8HiZVEkkVve6Wi.jpg",
        "cat": "중식",
        "url": "https://map.naver.com/p/entry/place/1333550573?lng=126.9526884&lat=37.4772346&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181740&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "왓더버거": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20260114_194%2F1768377305946jX4nL_JPEG%2Fm1.jpg",
        "cat": "햄버거",
        "url": "http://map.naver.com/p/entry/place/2012144622?lng=126.9528667&lat=37.4782031&placePath=%2Fhome&entry=plt&searchType=place",
    },
    "하노이별": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250818_58%2F1755508047196EXtbn_JPEG%2FKakaoTalk_20250818_174945530_13.jpg",
        "cat": "베트남음식",
        "url": "https://map.naver.com/p/search/%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%ED%95%98%EB%85%B8%EC%9D%B4%EB%B3%84/place/1354356843?placePath=?bk_query=%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%ED%95%98%EB%85%B8%EC%9D%B4%EB%B3%84&entry=pll&from=nx&fromNxList=true&searchType=place&c=15.00,0,0,0,dh",
    },
    "밀밀밀 포케&샐러드": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250207_265%2F1738933632982Ugrer_JPEG%2F1000037671.jpg",
        "cat": "샐러드",
        "url": "https://map.naver.com/p/entry/place/1716210969?lng=126.9526798&lat=37.4825041&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181743&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "일미순대국": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fpup-review-phinf.pstatic.net%2FMjAyNTEyMTFfMSAg%2FMDAxNzY1NDI1MzgxMDA2.FBJJFmbig_TlYfLcCGLdcLREx9C4eaYb52f0fKr7Nbwg.cuFiqXKcmvSTylKpSF27ubaVpmYT29n8ZEQkTJe0OY8g.JPEG%2F20251210_193520.jpg.jpg%3Ftype%3Dw1500_60_sharpen", # 사진 변경 필요
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/1664031628?c=15.00,0,0,0,dh&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181746&locale=ko&svcName=map_pcv5",
    },
    "모락미반": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230325_270%2F1679740132588RHjY9_JPEG%2FIMG_6111.JPG",
        "cat": "한식",
        "url": "http://map.naver.com/p/entry/place/1644141060?lng=126.9544558&lat=37.4839579&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "채우동": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250828_298%2F1756365464811JwClb_JPEG%2F%25C7%25C3%25B7%25B9%25C0%25CC%25BD%25BA016.jpg",
        "cat": "우동",
        "url": "http://map.naver.com/p/entry/place/1897575493?lng=126.9539197&lat=37.4798717&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "정숙성": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250222_124%2F17401886270212a7fT_JPEG%2F%25B3%25D7%25C0%25CC%25B9%25F65_%25C1%25A1%25BD%25C9_%25BE%25DF%25B5%25E9_%25C1%25A6%25C0%25B0%25BA%25BA%25C0%25BD.jpg",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/1959742624?lng=126.9538301&lat=37.4791772&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181751&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "찰솥밥소담쌈밥&추어탕": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240812_30%2F17234446935191um1q_JPEG%2F1723444608937.jpg", # 가게 사진
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/1593423527?lng=126.9568372&lat=37.4802476&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181753&locale=ko&svcName=map_pcv5&searchType=place&c=15.00,0,0,0,dh",
    },
}

# 20,000원
stores_20k = {
    "킷사서울": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20251210_197%2F1765300963671YhdX4_JPEG%2FIMG_4232.jpeg",
        "cat": "일식",
        "url": "https://map.naver.com/p/entry/place/1218049409?lng=126.9537873&lat=37.4792338&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601180219&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "텐동요츠야": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20251218_236%2F1766022349578edBBr_JPEG%2F1000016379.jpg",
        "cat": "일식",
        "url": "https://map.naver.com/p/entry/place/38460514?lng=126.9565657&lat=37.4784518&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "외래향": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20191202_287%2F1575267243159QEHT0_JPEG%2FkFkFdVXXbFhJWHAM7uVAFtoF.jpg",
        "cat": "중식",
        "url": "https://map.naver.com/p/entry/place/37770452?lng=126.9504933&lat=37.4817454&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601180220&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "빼누카츠": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240721_153%2F1721514251815EY9nn_JPEG%2FIMG_4180.jpeg",
        "cat": "돈가스",
        "url": "https://map.naver.com/p/entry/place/1202495197?lng=126.9459889&lat=37.4808849&placePath=%2Fhome&entry=plt&searchType=place",
    },
    "춘원쌈밥": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190704_91%2F1562240166016GQLot_JPEG%2FcCtoM9loQNHXA6hCdWRC84HM.jpg",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/913189557?lng=126.9552125&lat=37.483625&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601180303&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "샤로샤브": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20241008_41%2F1728368315433iUHYh_JPEG%2FIMG_0507.jpeg",
        "cat": "샤브샤브",
        "url": "https://map.naver.com/p/entry/place/1950347193?lng=126.9503323&lat=37.4787974&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "스아게": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240422_104%2F17137581463630J3lh_JPEG%2FIMG_20240418_154215_043.jpg",
        "cat": "카레",
        "url": "https://map.naver.com/p/entry/place/1919416084?lng=126.9535184&lat=37.4792547&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "브런치빈": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250523_78%2F1747995027255L9FPl_JPEG%2F%25BA%25EA%25B7%25B1%25C4%25A1%25BA%25F3_%25BF%25A9%25B8%25A7%25B8%25DE%25B4%25BA%25C6%25C7-01.jpg",
        "cat": "브런치",
        "url": "https://map.naver.com/p/entry/place/1122579123?lng=126.9541688&lat=37.4803934&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601180309&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "등촌샤브칼국수": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20241206_274%2F1733468985227xUcKW_JPEG%2F1000026567.jpg",
        "cat": "샤브샤브",
        "url": "https://map.naver.com/p/search/%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%EB%93%B1%EC%B4%8C%EC%83%A4%EB%B8%8C%EC%B9%BC%EA%B5%AD%EC%88%98/place/1034986125?placePath=/home?bk_query=%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%EB%93%B1%EC%B4%8C%EC%83%A4%EB%B8%8C%EC%B9%BC%EA%B5%AD%EC%88%98&entry=pll&from=map&fromNxList=true&fromPanelNum=2&timestamp=202601180310&locale=ko&svcName=map_pcv5&searchText=%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%EB%93%B1%EC%B4%8C%EC%83%A4%EB%B8%8C%EC%B9%BC%EA%B5%AD%EC%88%98&searchType=place&c=15.00,0,0,0,dh",
    },
    "스미비": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20220518_132%2F165286930299400ihz_JPEG%2F7.JPG",
        "cat": "함박스테이크",
        "url": "https://map.naver.com/p/search/%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%EC%8A%A4%EB%AF%B8%EB%B9%84/place/1256354786?placePath=/home?bk_query=%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%EC%8A%A4%EB%AF%B8%EB%B9%84&entry=pll&from=nx&fromNxList=true&from=map&fromPanelNum=2&timestamp=202601180319&locale=ko&svcName=map_pcv5&searchText=%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%EC%8A%A4%EB%AF%B8%EB%B9%84&placeSearchOption=bk_query%3D%25EC%2584%259C%25EC%259A%25B8%25EB%258C%2580%25EC%259E%2585%25EA%25B5%25AC%2520%25EC%258A%25A4%25EB%25AF%25B8%25EB%25B9%2584%26entry%3Dpll%26fromNxList%3Dtrue%26x%3D126.891732%26y%3D37.476909&searchType=place",
    },
    "키요이 스키야키": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20220219_180%2F16451971873645uLCP_JPEG%2FD2919B54-5649-4EEF-8026-63AB790B6C78.jpeg",
        "cat": "일식",
        "url": "https://map.naver.com/p/entry/place/1775764629?lng=126.9570831&lat=37.478509&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "앤미": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20231111_139%2F1699632473331ivc85_JPEG%2FIMG_5311.jpeg",
        "cat": "일식",
        "url": "https://map.naver.com/p/entry/place/1419822172?lng=126.9550304&lat=37.4778448&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181736&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "후안타이": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250122_143%2F1737519659515gV6RS_JPEG%2FKakaoTalk_20250105_110435512_09.jpg",
        "cat": "태국음식",
        "url": "https://map.naver.com/p/entry/place/37929791?lng=126.951503&lat=37.4825157&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181744&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
}

# UI
st.title(f"{today} 점메추🍚")
st.write("뽑기 버튼을 눌러주세요")

tab1, tab2 = st.tabs(["🤍 10,000원 데이", "💙 20,000원 데이"])

def show_recommendation(store_dict, title):
    if st.button("뽑기", key=title, type="primary"):
        with st.spinner("메뉴 고르는 중..."):
            time.sleep(1)
            
        # 3곳 랜덤 추출
        picks = random.sample(list(store_dict.keys()), min(3, len(store_dict)))
        st.balloons()
        
        st.subheader(f"오늘의 추천 메뉴 TOP 3")
        cols = st.columns(3)
        
        for i, name in enumerate(picks):
            with cols[i]:
                st.info(f"**{i+1}: {name}**")
                st.write(f"{store_dict[name]['cat']}")
                st.image(store_dict[name]['img'], use_column_width=True)
                
                target_url = store_dict[name]['url']
                button_html = f"""
                <a href="{target_url}" target="_blank" style="text-decoration: none;">
                    <div style="
                        display: inline-block;
                        width: 100%;
                        padding: 12px 0;
                        margin: 10px 0;
                        color: white;
                        background-color: #e84520;
                        text-align: center;
                        border-radius: 8px;
                        font-weight: bold;
                        font-size: 18px;
                    ">
                        📍 {name} 정보 보기
                    </div>
                </a>
                """
                st.markdown(button_html, unsafe_allow_html=True)
                
with tab1:
    show_recommendation(stores_10k, "만원")
with tab2:
    show_recommendation(stores_20k, "이만원")
