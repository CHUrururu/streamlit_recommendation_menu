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
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200926_173%2F1601073979588ER769_JPEG%2FakuH1ku0-lrZrk0Vh4XUZwve.jpeg.jpg", # 가게 사진
        "cat": "덮밥",
        "url": "https://map.naver.com/p/entry/place/1221670362?lng=126.9512359&lat=37.4802634&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601180306&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "충칭마라훠궈": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20241220_221%2F1734692184018clwKk_JPEG%2Fimage.jpg", # 메뉴 사진
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
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200622_27%2F1592825501669vngWY_JPEG%2FebpTj_qE7AohLIFQGp_oeFzk.jpg", # 가게 사진
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
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250207_265%2F1738933632982Ugrer_JPEG%2F1000037671.jpg", # 메뉴 사진
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
    "유미타코": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20251211_47%2F1765432661069e6VHb_JPEG%2F%25C0%25AF%25B9%25CC%25C5%25B8%25C4%25DA_-308.jpg",
        "cat": "타코",
        "url": "http://map.naver.com/p/entry/place/2081662207?lng=126.9553579&lat=37.4782695&placePath=%2Fhome&entry=plt&searchType=place",
    },
    "복희": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20241028_238%2F1730062643311ud40b_JPEG%2F3_%25BB%25F3%25C2%25F7%25B8%25B2_%25288%2529.JPG",
        "cat": "분식",
        "url": "https://map.naver.com/p/entry/place/1490746293?lng=126.9576552&lat=37.477928&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181758&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "줄포집": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240415_210%2F1713161750001IeP2u_JPEG%2F%25B4%25D9%25BF%25EE%25B7%25CE%25B5%25E5_%25287%2529.jpeg",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/1400713333?lng=126.9493425&lat=37.4822992&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "라이라이켄": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20180510_261%2F1525936420890s1PiU_JPEG%2FSD0Qbzg7vHaiXHG_FUa89-z9.jpg",
        "cat": "라멘",
        "url": "http://map.naver.com/p/entry/place/1158830420?lng=126.9540185&lat=37.4821416&placePath=%2Fhome&entry=plt&searchType=place",
    },
    "칠리향도삭면": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230829_226%2F16932889069546RSCH_JPEG%2FKakaoTalk_20230829_145429863_02.jpg",
        "cat": "중식",
        "url": "https://map.naver.com/p/entry/place/1119381344?lng=126.9529214&lat=37.4806567&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181802&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "어부사시가": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190827_233%2F1566877550770bS2af_JPEG%2Fyye_95qZkmqAYBf6_CK96hVs.jpeg.jpg", # 가게 사진
        "cat": "한식",
        "url": "http://map.naver.com/p/entry/place/1039016287?lng=126.9542973&lat=37.479001&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181803&locale=ko&svcName=map_pcv5&entry=plt&searchType=place",
    },
    "봉이돈가스": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200803_255%2F1596459500399IRJPa_JPEG%2FgQ19_FJ4ogr8u80HUkUln2LM.jpeg.jpg", # 가게 사진
        "cat": "돈가스",
        "url": "https://map.naver.com/p/entry/place/38232858?lng=126.9449262&lat=37.4817826&placePath=/home?entry=ple&fromPanelNum=1&additionalHeight=76&timestamp=202601181804&locale=ko&svcName=map_pcv5&searchType=place&c=15.00,0,0,0,dh",
    },
    "완산정": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20151104_50%2F1446623427279IzDes_JPEG%2F167054568045740_0.jpg",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/11680002?lng=126.953644&lat=37.481683&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181808&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "춘리마라탕": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230917_16%2F1694920086493KG5sP_JPEG%2FIMG_2258.jpeg",
        "cat": "마라탕",
        "url": "https://map.naver.com/p/search/%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%EC%B6%98%EB%A6%AC%EB%A7%88%EB%9D%BC%ED%83%95/place/1616772251?placePath=/home?bk_query=%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%EC%B6%98%EB%A6%AC%EB%A7%88%EB%9D%BC%ED%83%95&entry=pll&from=map&fromNxList=true&fromPanelNum=2&timestamp=202601181810&locale=ko&svcName=map_pcv5&searchText=%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%EC%B6%98%EB%A6%AC%EB%A7%88%EB%9D%BC%ED%83%95&searchType=place&c=15.00,0,0,0,dh",
    },
    "나눔국수국수": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20201217_227%2F1608171192338yPEB4_JPEG%2FgH7cyTpiiNxz4vD1MVqB1tCp.jpg",
        "cat": "국수",
        "url": "https://map.naver.com/p/entry/place/33284165?lng=126.951145&lat=37.478925&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181811&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "신의주찹쌀순대": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240613_95%2F1718242820870RholV_PNG%2F%25BD%25BA%25B8%25B6%25C6%25AE%25C7%25C3%25B7%25B9%25C0%25CC%25BD%25BA_%25BE%25F7%25C3%25BC%25C0%25CC%25B9%25CC%25C1%25F61.png",
        "cat": "한식",
        "url": "https://map.naver.com/p/search/%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%EC%8B%A0%EC%9D%98%EC%A3%BC%EC%B0%B9%EC%8C%80%EC%88%9C%EB%8C%80/place/33431474?placePath=?bk_query=%EC%84%9C%EC%9A%B8%EB%8C%80%EC%9E%85%EA%B5%AC%20%EC%8B%A0%EC%9D%98%EC%A3%BC%EC%B0%B9%EC%8C%80%EC%88%9C%EB%8C%80&entry=pll&from=nx&fromNxList=true&searchType=place&c=15.00,0,0,0,dh",
    },
    "요리요리": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20210527_50%2F1622098087896MLIFs_JPEG%2FdUSatkgzYCLCsEmR4aNadTdX.jpg", # 메뉴 사진
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/32873135?lng=126.9528141&lat=37.4784385&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181814&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "황토방": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250827_159%2F17562638365200h6TT_JPEG%2F20250827_120116.jpg", # 메뉴 사진
        "cat": "한식",
        "url": "http://map.naver.com/p/entry/place/31936395?lng=126.9528238&lat=37.4781333&placePath=%2Fhome&entry=plt&searchType=place",
    },
    "제주국수임당": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250912_280%2F1757652481745moj8K_JPEG%2FIMG_2276.jpeg",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/1477861012?lng=126.9527774&lat=37.4782557&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181818&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "엄마손칼국수": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190618_284%2F1560866427930K4CO5_JPEG%2FWzZqP2D22TJUbG1bNoJq5kgE.jpg", # 가게 사진
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/20856322?lng=126.9583017&lat=37.4778663&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "기절초풍왕순대": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200706_118%2F1594040337018Uus9B_JPEG%2FsbG7KFyUxl5r5KYESO2hkY9D.jpg", # 가게 사진
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/18709584?lng=126.9584629&lat=37.4781103&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181824&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "달떡볶이": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20201014_240%2F1602650925868FUVLK_JPEG%2Fp8v4q_CMXxtUS2gQtdP6QF2z.jpg",
        "cat": "분식",
        "url": "https://map.naver.com/p/entry/place/1817435234?lng=126.9547323&lat=37.4802623&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181825&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "클랩피자": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250227_166%2F1740645313100Us464_JPEG%2F%25BF%25C3%25B9%25CC%25C6%25AE_%25B1%25EE%25B8%25A3%25BA%25B8%25B3%25AA%25B6%25F3_%25BF%25AC%25C3%25E2%25C4%25C6_hand%2528%25C0%25FA%25BF%25EB%25B7%25AE%2529.jpg",
        "cat": "피자",
        "url": "https://map.naver.com/p/entry/place/1577383966?lng=126.9573881&lat=37.4775191&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "육해장": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250911_25%2F1757590172038QKrlC_JPEG%2F1201.jpg",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/2022542924?lng=126.9598999&lat=37.4787521&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "부림": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20200101_36%2F1577886345286vrixv_JPEG%2FqCj3jtR-YiOF4Y9UfwIYaAxJ.jpg", # 가게 사진
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/19877530?lng=126.9464721&lat=37.4813404&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181837&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "화우륵": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250618_144%2F17502471277362OuYA_JPEG%2F%25BB%25E7%25C1%25F87.jpeg",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/1907798176?placePath=%252Fhome%253Fentry%253Dplt&searchType=place&lng=126.9543072&lat=37.4823469&c=15.00,0,0,0,dh",
    },
    "늘콩": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20211114_105%2F1636889026973mhzbH_JPEG%2F20211114_202113.jpg",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/1591908912?placePath=%252Fhome%253Fentry%253Dplt&searchType=place&lng=126.9536312&lat=37.4830320&c=15.00,0,0,0,dh",
    },
    "멘지": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250626_190%2F1750909128281LGWVc_JPEG%2F8.jpg",
        "cat": "라멘",
        "url": "https://map.naver.com/p/entry/place/1545899272?lng=126.9559642&lat=37.4784345&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "도원경": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240809_145%2F17232011507912TkXF_JPEG%2F4.JPG",
        "cat": "중식",
        "url": "https://map.naver.com/p/entry/place/1010496761?placePath=/home?entry=plt&from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181906&locale=ko&svcName=map_pcv5&searchType=place&lng=126.9448298&lat=37.4831908&c=15.00,0,0,0,dh",
    },
    "낙원샌드위치": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230602_226%2F1685637977235iF3P0_JPEG%2F5.jpg",
        "cat": "샌드위치\n포장·배달",
        "url": "https://map.naver.com/p/entry/place/1131210397?lng=126.9523419&lat=37.4826681&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181910&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "올리스테이블": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250117_43%2F1737101581236NO16z_JPEG%2F1736325140461.jpg", # 로고 사진
        "cat": "샌드위치\n포장·배달",
        "url": "https://map.naver.com/p/entry/place/1339681998?lng=126.9530456&lat=37.4826855&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181911&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
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
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20191202_287%2F1575267243159QEHT0_JPEG%2FkFkFdVXXbFhJWHAM7uVAFtoF.jpg", # 가게 사진
        "cat": "중식",
        "url": "https://map.naver.com/p/entry/place/37770452?lng=126.9504933&lat=37.4817454&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601180220&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "빼누카츠": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240721_153%2F1721514251815EY9nn_JPEG%2FIMG_4180.jpeg",
        "cat": "돈가스",
        "url": "https://map.naver.com/p/entry/place/1202495197?lng=126.9459889&lat=37.4808849&placePath=%2Fhome&entry=plt&searchType=place",
    },
    "춘원쌈밥": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20190704_91%2F1562240166016GQLot_JPEG%2FcCtoM9loQNHXA6hCdWRC84HM.jpg", # 가게 사진
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
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20241206_274%2F1733468985227xUcKW_JPEG%2F1000026567.jpg", # 메뉴 사진
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
    "나인온스버거": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20151104_123%2F1446623089057duSbk_JPEG%2F167054567467570_0.jpg",
        "cat": "햄버거",
        "url": "https://map.naver.com/p/entry/place/33315286?lng=126.9584021&lat=37.4772272&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181806&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "정가네 낙지마당": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230218_215%2F1676689201871IhElW_JPEG%2F%25B3%25AB%25C1%25F6%25BE%25C6%25B1%25B8%25C2%25F2.jpg",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/20059579?lng=126.9527559&lat=37.477551&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "레몬그라스타이": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240327_148%2F1711521427054rbyRu_JPEG%2F1000009062.jpg", # 가게 사진
        "cat": "태국음식",
        "url": "https://map.naver.com/p/entry/place/1842750579?lng=126.9590196&lat=37.4782925&placePath=%2Fhome&searchType=place&c=15.00,0,0,0,dh",
    },
    "순보보": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250422_191%2F1745301061461rFwYK_JPEG%2F1000011655.jpg", # 메뉴 사진
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/20729782?lng=126.9587594&lat=37.4774374&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181821&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "몬스터포": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240626_243%2F17193792249890llX3_JPEG%2FKakaoTalk_20240322_125458357.jpg",
        "cat": "베트남음식",
        "url": "https://map.naver.com/p/entry/place/1030657713?placePath=%252Fhome%253Fentry%253Dplt&searchType=place&lng=126.9566161&lat=37.4805475&c=15.00,0,0,0,dh",
    },
    "동경산책": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20251204_85%2F1764775138153w4MN3_JPEG%2F1000019274.jpg",
        "cat": "일식",
        "url": "http://map.naver.com/p/entry/place/1588568877?lng=126.9542&lat=37.4789029&placePath=%2Fhome&entry=plt&searchType=place",
    },
    "스테이크하우스 로아": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250210_263%2F1739184331858mjgon_PNG%2F%25B4%25DC%25C3%25BC%25BC%25A6_%25B3%25D7%25C0%25CC%25B9%25F6.png",
        "cat": "양식",
        "url": "https://map.naver.com/p/entry/place/36084392?placePath=/home?entry=plt&from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181830&locale=ko&svcName=map_pcv5&searchType=place&lng=126.9589582&lat=37.4776631&c=15.00,0,0,0,dh",
    },
    "꼬꼬숯불닭갈비": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240625_284%2F1719281819505RYywk_JPEG%2FIMG_7146.JPG",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/1292300657?lng=126.9548011&lat=37.4801632&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "채선당": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20211228_117%2F1640672035109D7lqS_JPEG%2FERT.jpg",
        "cat": "샤브샤브",
        "url": "https://map.naver.com/p/entry/place/18146831?lng=126.9540451&lat=37.4805072&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181843&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "보끔당": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230804_255%2F1691118198247lRahb_JPEG%2FIMG_E4130.JPG",
        "cat": "한식",
        "url": "https://map.naver.com/p/entry/place/1710111971?lng=126.9544994&lat=37.4789447&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181848&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "카츠쇼신": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20241015_72%2F1728957033097Y7FAE_JPEG%2FIMG_9764.jpeg",
        "cat": "돈가스",
        "url": "https://map.naver.com/p/entry/place/1217588172?lng=126.9532949&lat=37.4797117&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181854&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "삼백돈 돈가츠": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20250604_148%2F1749025615766t9cdF_JPEG%2F%25B4%25EB%25C7%25A5%25C0%25CC%25B9%25CC%25C1%25F6_%25B3%25D7%25C0%25CC%25B9%25F6%25C7%25C3%25B7%25B9%25C0%25CC%25BD%25BA_%25BE%25C8%25BD%25C9.jpg",
        "cat": "돈가스",
        "url": "https://map.naver.com/p/entry/place/2028991155?lng=126.9552883&lat=37.478012&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "스시공방": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20201115_226%2F1605452329325Lm0xK_JPEG%2FnLC6Q_6KyHGcLLEQpDDUwhzc.jpg",
        "cat": "초밥",
        "url": "https://map.naver.com/p/entry/place/1077343690?lng=126.9567514&lat=37.4803783&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181857&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "후추스시": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20241128_53%2F1732763137953CqyDe_JPEG%2FIMG_2642.jpeg",
        "cat": "초밥",
        "url": "https://map.naver.com/p/entry/place/1070317367?lng=126.9573162&lat=37.4781977&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181858&locale=ko&svcName=map_pcv5&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "아란": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20241107_48%2F173098923274011YO8_JPEG%2F1000005372.jpg",
        "cat": "양식",
        "url": "https://map.naver.com/p/entry/place/1708386763?lng=126.9446773&lat=37.4832019&placePath=%2Fhome&entry=plt&searchType=place&c=15.00,0,0,0,dh",
    },
    "이상범스시": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20170730_1%2F1501344439601fpxxn_JPEG%2F186680413739072_4.jpeg",
        "cat": "초밥",
        "url": "https://map.naver.com/p/entry/place/875574854?lng=126.9453267&lat=37.4831312&placePath=/home?from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181904&locale=ko&svcName=map_pcv5&searchType=place&c=15.00,0,0,0,dh",
    },
    "도원경": {
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240809_145%2F17232011507912TkXF_JPEG%2F4.JPG",
        "cat": "중식",
        "url": "https://map.naver.com/p/entry/place/1010496761?placePath=/home?entry=plt&from=map&fromPanelNum=1&additionalHeight=76&timestamp=202601181906&locale=ko&svcName=map_pcv5&searchType=place&lng=126.9448298&lat=37.4831908&c=15.00,0,0,0,dh",
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
