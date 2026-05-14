import streamlit as st
import random

st.set_page_config(
    page_title="✨ MBTI 진로 추천기 ✨",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 MBTI 기반 진로 추천기")
st.markdown("### 😎 나의 MBTI에 어울리는 진로를 알아보자!")
st.write("MBTI를 선택하면 어울리는 진로 2개를 추천해줄게 ✨")

# MBTI별 데이터
career_data = {
    "INTJ": [
        {
            "career": "🧠 데이터 사이언티스트",
            "major": "컴퓨터공학과, 데이터사이언스학과",
            "personality": "논리적이고 전략적으로 생각하는 사람!"
        },
        {
            "career": "🏗️ 건축가",
            "major": "건축학과",
            "personality": "창의적이면서 계획 세우기를 좋아하는 사람!"
        }
    ],

    "INTP": [
        {
            "career": "💻 프로그래머",
            "major": "컴퓨터공학과",
            "personality": "호기심 많고 새로운 걸 탐구하는 사람!"
        },
        {
            "career": "🔬 연구원",
            "major": "물리학과, 화학과",
            "personality": "분석적이고 깊게 생각하는 사람!"
        }
    ],

    "ENTJ": [
        {
            "career": "📈 CEO",
            "major": "경영학과",
            "personality": "리더십이 강하고 목표지향적인 사람!"
        },
        {
            "career": "⚖️ 변호사",
            "major": "법학과",
            "personality": "논리적으로 말 잘하는 사람!"
        }
    ],

    "ENTP": [
        {
            "career": "🚀 창업가",
            "major": "경영학과",
            "personality": "아이디어가 많고 도전을 즐기는 사람!"
        },
        {
            "career": "🎤 마케터",
            "major": "광고홍보학과",
            "personality": "재치 있고 사람들과 소통 잘하는 사람!"
        }
    ],

    "INFJ": [
        {
            "career": "🧑‍🏫 상담교사",
            "major": "심리학과, 교육학과",
            "personality": "공감 능력이 뛰어나고 따뜻한 사람!"
        },
        {
            "career": "✍️ 작가",
            "major": "문예창작과",
            "personality": "상상력이 풍부하고 감수성이 깊은 사람!"
        }
    ],

    "INFP": [
        {
            "career": "🎨 일러스트레이터",
            "major": "디자인학과",
            "personality": "창의적이고 감성적인 사람!"
        },
        {
            "career": "🎵 음악 프로듀서",
            "major": "실용음악과",
            "personality": "자신만의 감성을 표현하는 걸 좋아하는 사람!"
        }
    ],

    "ENFJ": [
        {
            "career": "🎙️ 아나운서",
            "major": "언론정보학과",
            "personality": "사람들에게 긍정적인 영향을 주는 사람!"
        },
        {
            "career": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "친절하고 책임감 있는 사람!"
        }
    ],

    "ENFP": [
        {
            "career": "📺 유튜버",
            "major": "미디어학과",
            "personality": "에너지 넘치고 표현력이 좋은 사람!"
        },
        {
            "career": "🎭 배우",
            "major": "연극영화과",
            "personality": "감정 표현이 풍부한 사람!"
        }
    ],

    "ISTJ": [
        {
            "career": "🏦 회계사",
            "major": "회계학과",
            "personality": "꼼꼼하고 책임감 강한 사람!"
        },
        {
            "career": "👮 경찰관",
            "major": "경찰행정학과",
            "personality": "원칙을 중요하게 생각하는 사람!"
        }
    ],

    "ISFJ": [
        {
            "career": "💉 간호사",
            "major": "간호학과",
            "personality": "배려심 많고 성실한 사람!"
        },
        {
            "career": "🏥 물리치료사",
            "major": "물리치료학과",
            "personality": "사람을 돕는 걸 좋아하는 사람!"
        }
    ],

    "ESTJ": [
        {
            "career": "📋 공무원",
            "major": "행정학과",
            "personality": "체계적이고 리더십 있는 사람!"
        },
        {
            "career": "💼 관리자",
            "major": "경영학과",
            "personality": "책임감 있고 추진력이 강한 사람!"
        }
    ],

    "ESFJ": [
        {
            "career": "🩺 치위생사",
            "major": "치위생학과",
            "personality": "친절하고 사람 챙기는 걸 좋아하는 사람!"
        },
        {
            "career": "🎉 이벤트 플래너",
            "major": "관광경영학과",
            "personality": "사교적이고 분위기 메이커인 사람!"
        }
    ],

    "ISTP": [
        {
            "career": "🔧 자동차 엔지니어",
            "major": "기계공학과",
            "personality": "손재주 좋고 문제 해결을 좋아하는 사람!"
        },
        {
            "career": "🛩️ 파일럿",
            "major": "항공운항학과",
            "personality": "침착하고 상황 판단이 빠른 사람!"
        }
    ],

    "ISFP": [
        {
            "career": "📸 사진작가",
            "major": "사진영상학과",
            "personality": "감각적이고 자유로운 사람!"
        },
        {
            "career": "💄 메이크업 아티스트",
            "major": "뷰티디자인학과",
            "personality": "예술 감각이 뛰어난 사람!"
        }
    ],

    "ESTP": [
        {
            "career": "⚽ 스포츠 코치",
            "major": "체육학과",
            "personality": "활동적이고 도전 정신이 강한 사람!"
        },
        {
            "career": "💰 영업 전문가",
            "major": "경영학과",
            "personality": "사람 만나는 걸 좋아하고 자신감 있는 사람!"
        }
    ],

    "ESFP": [
        {
            "career": "🎤 연예인",
            "major": "연극영화과",
            "personality": "밝고 끼가 많은 사람!"
        },
        {
            "career": "✈️ 승무원",
            "major": "항공서비스학과",
            "personality": "친화력 좋고 서비스 정신이 뛰어난 사람!"
        }
    ]
}

# MBTI 선택
mbti = st.selectbox(
    "👇 너의 MBTI를 선택해봐!",
    list(career_data.keys())
)

# 버튼
if st.button("✨ 진로 추천 받기 ✨"):

    st.balloons()

    st.subheader(f"💖 {mbti} 유형 추천 진로")

    careers = career_data[mbti]

    for idx, item in enumerate(careers, start=1):
        st.markdown(f"""
        ---
        ## {idx}. {item['career']}

        ### 📚 추천 학과
        👉 {item['major']}

        ### 😎 이런 성격에게 잘 어울려!
        👉 {item['personality']}
        """)

    st.success("🌟 미래의 멋진 모습을 응원할게!")
