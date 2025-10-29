import streamlit as st
st.title('이정윤의 첫번째 앱!')
st.subheader('오늘 저녁 뭐먹지?')
st.write('하하하! 오늘 석식 고구마튀김...')
st.write('https://naver.com')
st.link_button("네이버 바로가기",'https://naver.com')

name = st.text_input('이름을 입력해주세요!:')
if st.button('환영인사'):
    st.write(name+'님 안녕하세요!')
    st.balloons()
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGoPzMpnTdvXwnxeuv5cHUrxR2SRYbrji5921if6pBgaX3sM2jA_4-zCuRaHaevAuSHwu1zVegwKZA9ZjeIg8DP3yPc3wrOq0klJ2KkAU')

st.success('성공!')
st.warning('경고!')
st.error('오류!')
st.info('안내문')
