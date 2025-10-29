# app.py
import streamlit as st

# 🌈 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천", page_icon="🧭", layout="wide")

# 🎨 스타일 (Streamlit Cloud 호환)
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #fef6e4, #e3f6f5, #f3e8ff);
    background-attachment: fixed;
}
h1, h2, h3 { text-align: center; }
.job-card {
    background-color: rgba(255, 255, 255, 0.75);
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
.job-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
    margin-top: 10px;
}
.tag {
    background-color: #dbeafe;
    border-radius: 20px;
    padding: 3px 10px;
    font-size: 0.85rem;
}
</style>
""", unsafe_allow_html=True)

# 🧭 MBTI별 직업 데이터
jobs = {
    "INTJ": [
        ("📊 데이터 사이언티스트", "전략적이고 논리적인 사고를 통해 복잡한 문제를 해결해요.", ["분석", "연구", "AI"]),
        ("🧠 전략 컨설턴트", "큰 그림을 보고 방향을 제시하는 데 강점을 보여요.", ["비즈니스", "리더십", "기획"])
    ],
    "INFP": [
        ("🖋️ 에디터/작가", "감정과 메시지를 글로 표현하는 데 능숙해요.", ["창의", "콘텐츠", "감성"]),
        ("🌱 사회복지사", "타인의 감정을 잘 이해하고 공감할 수 있어요.", ["사회영향", "교육", "서비스"])
    ],
    "ENFP": [
        ("🎬 콘텐츠 크리에이터", "아이디어와 에너지가 넘치는 창의형 인재!", ["창의", "콘텐츠", "소통"]),
        ("💬 브랜드 마케터", "감각적 스토리텔링으로 사람들의 마음을 사로잡아요.", ["비즈니스", "커뮤니케이션", "기획"])
    ],
    "ISTJ": [
        ("📋 회계/재무 전문가", "체계적이고 정확한 데이터 관리에 능숙해요.", ["정확성", "분석", "비즈니스"]),
        ("🏛️ 공공행정직", "책임감과 안정감을 바탕으로 사회에 기여해요.", ["정확성", "공공", "서비스"])
    ],
    "ESFP": [
        ("🎉 이벤트 플래너", "에너지 넘치고 현장을 즐기는 사람!", ["창의", "서비스", "커뮤니케이션"]),
        ("📺 인플루언서", "자신만의 매력으로 사람들과 소통해요.", ["콘텐츠", "감성", "소통"])
    ],
    "INFJ": [
        ("🎨 UX 디자이너", "사람의 감정을 이해하고 아름답게 풀어내요.", ["디자인", "공감", "연구"]),
        ("📚 교육 기획자", "지식과 가치를 전하는 데 열정을 가져요.", ["교육", "기획", "사회영향"])
    ],
}

# 💬 사이드바
st.sidebar.title("🧭 MBTI 직업 추천기")
user_mbti = st.sidebar.selectbox("당신의 MBTI를 선택하세요", list(jobs.keys()))
st.sidebar.write("🌟 선택된 유형:", f"**{user_mbti}**")

# 🌟 메인 화면
st.markdown("<h1>✨ MBTI 기반 직업 추천 ✨</h1>", unsafe_allow_html=True)
st.write("당신의 성향에 어울리는 직업을 소개합니다!")

# 🗂️ 추천 결과 출력
if user_mbti:
    st.markdown(f"<h2>💡 {user_mbti} 유형 추천 직업</h2>", unsafe_allow_html=True)
    for title, desc, tags in jobs[user_mbti]:
        st.markdown(f"""
        <div class='job-card'>
            <h4>{title}</h4>
            <p>{desc}</p>
            <div class='job-tags'>
                {''.join(f"<span class='tag'>#{t}</span>" for t in tags)}
            </div>
        </div>
        """, unsafe_allow_html=True)

# 🎯 하단 문구
st.markdown("---")
st.markdown("📎 *Streamlit Cloud에서 바로 실행 가능!*  \n💡 MBTI별 추천 결과를 저장하거나 친구들과 공유해보세요!")
