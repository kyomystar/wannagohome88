# # import streamlit as st

# # st.title("🎈 삶은감자")
# # st.info(
# #     "안녕하세요. 반갑습니다. 저는 말하는 감자입니다."
# # )
# # # st.markdown(): 마크다운 문법 지원 (굵게, 기울임, 목록 등)
# # st.markdown("**구황작물**, *드실래요?*")
# # st.markdown("""- 감자
# # - 고구마
# # - 옥수수""")
# # # 정보성 메시지 박스
# # st.warning("⚠️ 감자 많이 먹어라!")

# # st.image("https://i.namu.wiki/i/WmrhCVIzvV_lyGMUZiMz8ltnq7qierpQ2kTanyF1FlPZxDECWVnxnfpd799mZavVY-qFpc-V8ptU23RDVXUdgw.webp")
# # st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWdvdnRsOWdxb2hhdmJkaWVucDl3OHcxdWoyamsyaGY0Y2M0ZGhvbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OjmrBW4ZQbWjkq6RkC/giphy.gif")

# # st.code("""
# # import streamlit as st
# # st.title('Hello World')
# # """, language="python")

# # st.link_button("연결할 url을 이 다음 변수에 써주세요!", 'https://docs.streamlit.io/develop/quick-reference/cheat-sheet')

# # # st.columns(n): 화면을 n개의 수직 열로 나눕니다
# # col1, col2 = st.columns(2)  # 2개의 열 생성

# # with col1:
# #     st.write("야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! 야호! ")  # 첫 번째 열에 내용 작성
# # with col2:
# #     st.write("인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생! 인생!")  # 두 번째 열에 내용 작성

# #     # st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
# # tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

# # with tab1:
# #     st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
# #     name = st.text_area("할 말이 있으신가요?")

# # with tab2:
# #     st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용

# #     name = st.text_input("배우자 이름을 입력해주세요:")
# #     st.balloons()
# #     st.error(name+"님과 꼭 결혼하시길 바랍니다!")



# # # 카메라로 사진 촬영
# # image_data = st.camera_input("사진을 찍어보세요")
# # if image_data:
# #     st.image(image_data)


# # import openai

# # user_api_key = st.text_input("키를 입력해주세요.")

# # if user_api_key: 


# #     from openai import OpenAI

# #     client = OpenAI(api_key = user_api_key)
# #     prompt = st.text_input("프롬프트를 입력해주세요.")

# #     completion = client.chat.completions.create(
# #         model="gpt-3.5-turbo",
# #         messages=[{"role": "user", "content": prompt}]
# #     )
# #     st.markdown("### 💡 GPT의 답변:")
# #     st.write(completion.choices[0].message.content)


# import streamlit as st
# import openai

# # 🎈 제목 & 인트로
# st.title("🎈 삶은감자")
# st.info("안녕하세요. 반갑습니다. 저는 말하는 감자입니다.")

# # 마크다운 문법 예시
# st.markdown("**구황작물**, *드실래요?*")
# st.markdown("""
# - 감자  
# - 고구마  
# - 옥수수  
# """)

# # 정보성 메시지
# st.warning("⚠️ 감자 많이 먹어라!")

# # 이미지 출력
# st.image("https://i.namu.wiki/i/WmrhCVIzvV_lyGMUZiMz8ltnq7qierpQ2kTanyF1FlPZxDECWVnxnfpd799mZavVY-qFpc-V8ptU23RDVXUdgw.webp")
# st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWdvdnRsOWdxb2hhdmJkaWVucDl3OHcxdWoyamsyaGY0Y2M0ZGhvbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OjmrBW4ZQbWjkq6RkC/giphy.gif")

# # 코드 블럭 예시
# st.code("""
# import streamlit as st
# st.title('Hello World')
# """, language="python")

# # 링크 버튼
# st.link_button("연결할 url을 이 다음 변수에 써주세요!", 'https://docs.streamlit.io/develop/quick-reference/cheat-sheet')

# # 📌 두 개의 열(column) 레이아웃
# col1, col2 = st.columns(2)

# with col1:
#     st.write("야호! " * 25)

# with col2:
#     st.write("인생! " * 24)

# # 📌 탭 구성
# tab1, tab2 = st.tabs(["탭 1", "탭 2"])

# with tab1:
#     st.write("탭 1에 해당하는 내용입니다.")
#     name = st.text_area("할 말이 있으신가요?")

# with tab2:
#     st.write("탭 2에 해당하는 내용입니다.")
#     name = st.text_input("배우자 이름을 입력해주세요:")
#     st.balloons()
#     st.error(f"{name}님과 꼭 결혼하시길 바랍니다!")

# # 📷 카메라 입력
# image_data = st.camera_input("사진을 찍어보세요")
# if image_data:
#     st.image(image_data)

# # 🔐 OpenAI 연동
# user_api_key = st.text_input("키를 입력해주세요.")
# with tabs[5]
# if user_api_key:
#     from openai import OpenAI
#     client = OpenAI(api_key=user_api_key)

#     prompt = st.text_input("프롬프트를 입력해주세요.")

#     if prompt:
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}]
#         )

#         st.markdown("### 💡 GPT의 답변:")
#         st.write(completion.choices[0].message.content)

import streamlit as st
import openai

# 전체 앱을 탭으로 나누기
tabs = st.tabs(["🥔 감자소개", "📄 감자코드", "🎉 감자놀이", "📷 감자촬영", "🤖 GPT 감자"])

# --- 🥔 감자소개 탭 ---
with tabs[0]:
    st.title("🎈 삶은감자")
    st.info("안녕하세요. 반갑습니다. 저는 말하는 감자입니다.")

    st.markdown("**구황작물**, *드실래요?*")
    st.markdown("""
    - 감자  
    - 고구마  
    - 옥수수  
    """)

    st.warning("⚠️ 감자 많이 먹어라!")

    st.image("https://i.namu.wiki/i/WmrhCVIzvV_lyGMUZiMz8ltnq7qierpQ2kTanyF1FlPZxDECWVnxnfpd799mZavVY-qFpc-V8ptU23RDVXUdgw.webp")
    st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWdvdnRsOWdxb2hhdmJkaWVucDl3OHcxdWoyamsyaGY0Y2M0ZGhvbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OjmrBW4ZQbWjkq6RkC/giphy.gif")

# --- 📄 감자코드 탭 ---
with tabs[1]:
    st.markdown("### 📄 코드 예시")
    st.code("""
import streamlit as st
st.title('Hello World')
""", language="python")

    st.link_button("Streamlit 치트시트로 이동", 'https://docs.streamlit.io/develop/quick-reference/cheat-sheet')

# --- 🎉 감자놀이 탭 ---
with tabs[2]:
    st.markdown("## 🎊 감자 놀이터")

    col1, col2 = st.columns(2)
    with col1:
        st.write("야호! " * 25)
    with col2:
        st.write("인생! " * 24)

    inner_tabs = st.tabs(["💬 탭 1", "💘 탭 2"])
    with inner_tabs[0]:
        st.write("탭 1에 해당하는 내용입니다.")
        st.text_area("할 말이 있으신가요?")
    with inner_tabs[1]:
        st.write("탭 2에 해당하는 내용입니다.")
        name = st.text_input("배우자 이름을 입력해주세요:")
        if name:
            st.balloons()
            st.error(f"{name}님과 꼭 결혼하시길 바랍니다!")

# --- 📷 감자촬영 탭 ---
with tabs[3]:
    st.markdown("## 📷 사진 촬영")
    image_data = st.camera_input("사진을 찍어보세요")
    if image_data:
        st.image(image_data)

# --- 🤖 GPT 감자 탭 ---
with tabs[4]:
    st.markdown("## 🤖 GPT와 대화하기")
    user_api_key = st.text_input("OpenAI API 키를 입력해주세요:", type="password")

    if user_api_key:
        from openai import OpenAI
        client = OpenAI(api_key=user_api_key)

        prompt = st.text_input("프롬프트를 입력해주세요:")
        if prompt:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown("### 💡 GPT의 답변:")
            st.write(completion.choices[0].message.content)
