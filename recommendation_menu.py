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
        "img": "https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20230120_160%2F1674144243838ovIUa_JPEG%2F997CD13F-3B2C-490A-9A38-9F44F1D5AA63.jpeg",
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
                st.write(f"분류: {store_dict[name]['cat']}")
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