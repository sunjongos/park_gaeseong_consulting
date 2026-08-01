---
name: park_gaeseong_consulting
description: "/박개성컨설팅 - 엘리오앤컴퍼니 박개성 대표 저서 34개 챕터 전수 자산과 portable 온톨로지 DB(knowledge_assets)를 탑재하여 다른 PC/장관님 컴퓨터에서도 100% 무결점으로 작동하는 LCK LAB LUCA AGI SYSTEM 신경기호학적 병원 경영 처방 스킬입니다."
---

# 🧠🔮 /박개성컨설팅 - LCK LAB - LUCA AGI SYSTEM 100% PORTABLE CONSULTING SKILL

본 스킬은 앤드류컴퍼니/엘리오앤컴퍼니 박개성 대표의 저서 **『박개성의 병원을 경영하는 이유』(34개 챕터 전수 자산)** 및 **온톨로지 지식 그래프 DB(`knowledge_assets/ontology_graph.json`)**를 스킬 자체 패키지에 100% 동봉하여, **Neo4j DB 연결 여부와 상관없이 어느 PC(장관님 컴퓨터 등)에서나 100% 오프라인 자립형으로 작동**하도록 설계된 궁극의 병원 경영 처방 엔진입니다.

---

## 📦 PORTABLE KNOWLEDGE BUNDLE STRUCTURE (동봉 지식 자산 명세)

```
park_gaeseong_consulting/
├── SKILL.md
├── knowledge_assets/
│   ├── ontology_graph.json          # 4M 근육, 12대 테마, 5대 성과, R1~R4 공리 온톨로지 DB
│   └── chapters/                     # 34개 챕터 전수 심층 분석 마크다운 자산 (34 Files)
│       ├── 01_00_프론트매터_서문_및_이책의지도_analysis.md
│       ├── 02_1부_01_100년을_살아남은_병원은_무엇이_다른가_analysis.md
│       └── ... (34개 챕터 전수)
└── scripts/
    └── build_hospital_consulting_report.py  # 100% 오프라인 HTML & Word 이중 보고서 생성기
```

---

## 🚨 DUAL-ENGINE FALLBACK PROTOCOL (이중 DB 연동 프로토콜)

> **[핵심 규정] 본 스킬은 이중 노드 추출 가동 방식을 채택합니다:**
> 1. **Primary Mode (Neo4j DB)**: `bolt://localhost:7687`이 구동 중일 경우 실시간 그래프 Cypher 쿼리 수행.
> 2. **Fallback Portable Mode**: Neo4j 미설치/미구동 PC 환경(장관님 PC 등)에서는 스킬 내 동봉된 `knowledge_assets/ontology_graph.json` 및 `chapters/*.md`를 자동으로 즉각 감지·로드하여 **100% 동일한 품질의 경영 진단 보고서를 생성**.

---

## 📐 MANDATORY ZERO-DEFECT QUALITY RULES (5대 무결점 규칙)

1. **온톨로지 지식 그래프 100% 완전 연결 (Zero Floating Nodes)**:
   - Root (노드 1) ➔ Layer 1 4M 근육 (노드 2~5) ➔ Layer 2 T1~T12 12대 테마 (노드 101~112) ➔ Layer 3 5대 성과 열매 (노드 301~305)까지 고립 노드 없이 100% 연결.
2. **T1~T12 12대 실행 테마 전수 해설 포함**:
   - T1(전략계획) ~ T12(신사업) 명칭 및 세부 실행 정의 전수 해설 표/카드 포함.
3. **R1~R4 4대 경영 공리 & 부산침례병원 파산 사례 수록**:
   - R1(선행타격), R2(거버넌스 불변 - 부산침례병원 800병상 파산 경고), R3(20배 구매레버리지), R4(4M 곱셈).
4. **KaTeX 수리 방정식 전수 명시**:
   - 종합 성과 방정식 \(Y_{\text{Performance}}\) 및 R3 구매 20배 레버리지 방정식 명시.
5. **이중 출력 및 100% 오프라인 인라이닝**:
   - 단일 HTML 파일(`*_integrated.html`)과 MS Word 문서(`.docx`) 2종 동시 발행 및 브라우저 자동 기동.

---

## 🚀 실행 프로토콜

```bash
# 어느 PC에서나 스킬 실행 스크립트를 즉시 가동하여 보고서 자동 생성
python .agent/skills/park_gaeseong_consulting/scripts/build_hospital_consulting_report.py
```
