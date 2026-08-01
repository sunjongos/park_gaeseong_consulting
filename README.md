# 🏥 LCK LAB - LUCA AGI SYSTEM: 박개성 병원 경영 컨설팅 신경기호학적 온톨로지 엔진
> **Park Gae-seong Hospital Management Consulting Neurosymbolic Ontology Skill**

[![Version](https://img.shields.io/badge/version-2.0%20Portable-00f3ff.svg)](#)
[![Zero-Defect](https://img.shields.io/badge/quality-5--Loop%20Verified-2ed573.svg)](#)
[![License](https://img.shields.io/badge/license-MIT-ffd700.svg)](#)
[![GitHub Stars](https://img.shields.io/badge/AGI%20Engine-Neurosymbolic-a855f7.svg)](#)

본 저장소(Repository)는 앤드류컴퍼니/엘리오앤컴퍼니 **박개성 대표의 저서 『박개성의 병원을 경영하는 이유』 34개 챕터 분석 자산 전수**와 **Neo4j 온톨로지 지식 그래프 DB**를 **LCK LAB - LUCA AGI SYSTEM 신경기호학적 모델(Neurosymbolic Hybrid Model)**로 결합한 최첨단 병원 경영 처방 엔진 스킬 패키지입니다.

스킬 패키지 내부에 **34개 챕터 지식 위키(Wiki)**와 **온톨로지 그래프 JSON DB (`knowledge_assets/ontology_graph.json`)**가 100% 동봉되어 있어, **Neo4j DB 미설치 PC(장관님 컴퓨터 등)에서도 100% 오프라인 자립형으로 가동**됩니다.

---

## 🗺️ REPOSITORY & WIKI ARCHITECTURE (저장소 및 위키 구조)

```
park_gaeseong_consulting/
├── README.md                          # 본 저장소 공식 마스터 가이드
├── SKILL.md                          # Antigravity / Agentic AI 스킬 실행 헌법
├── wiki/                              # 📚 34개 챕터 온톨로지 경영 지식 위키
│   ├── 00_OVERVIEW_WIKI_MAP.md       # 전체 지식맵 및 내비게이션
│   ├── 01_AXIOMS_AND_RULES_WIKI.md   # R1~R4 4대 경영 공리 & 부산침례병원 파산 사례
│   ├── 02_THEMES_T1_TO_T12_WIKI.md   # T1~T12 12대 실행 테마 전수 가이드
│   ├── 03_ORGANIZATIONAL_MUSCLES_4M_WIKI.md # 4M 조직 근육 (Mapping, Manpower, Mastery, Mechanism)
│   ├── 04_ONTOLOGY_GRAPH_SPECIFICATION.md   # 그래프 노드·엣지 스키마 명세
│   └── 05_CHAPTERS_INDEX.md          # 34개 챕터 전수 분석 색인
├── knowledge_assets/                 # 📦 동봉된 핵심 지식 자산
│   ├── ontology_graph.json          # 4M-12Themes-5Outcomes 온톨로지 DB
│   └── chapters/                     # 34개 챕터 심층 분석 마크다운 (34 Files)
└── scripts/                          # ⚙️ 자율 실행 및 보고서 생성 파이프라인
    ├── neurosymbolic_park_gaeseong_engine.py  # 신경기호학적 추론 & T-SIRT 검증 엔진
    └── build_hospital_consulting_report.py   # 오프라인 인라이닝 이중 보고서(HTML/Word) 생성기
```

---

## 🧬 NEUROSYMBOLIC 4-STAGE PIPELINE (4단계 신경기호학적 파이프라인)

```
[Stage 1. Symbolic Traversal] ──> [Stage 2. Neural Generation] ──> [Stage 3. Symbolic Immune System] ──> [Stage 4. Predictive Synthesis]
   - Neo4j / Portable JSON          - Gemini 2.5 / Flash Neural        - T-SIRT 수식 및 공리 검증          - 오프라인 HTML & Word
   - R1~R4 & T1~T12 노드 추출       - 재무·운영 빅데이터 가설 생성     - R2 파산 경고 낭비 0% 교정         - 실시간 Live DSS 시뮬레이터
```

---

## ⚖️ PARK GAE-SEONG 4 AXIOMS & FORMULAS (4대 경영 공리 및 수리 수식)

### 1. 병원 종합 성과 방정식 (Hospital Performance Equation)
$$Y_{\text{Performance}} = f(\text{Mission}) \times \left( \prod_{j=1}^{4} M_j \right) \times \left( \sum_{i=1}^{12} T_i \cdot w_i \right) - \text{Friction}$$

### 2. R3 T6 구매절감 20배 영업이익 레버리지 방정식
$$\Delta \pi = \Delta S_{\text{T6}} = \frac{\Delta Y_{\text{Clinical Revenue}}}{\text{Baseline Operating Margin Rate}}$$
> 상급종합병원 영업이익률 5% 산정 시, **물류/구매 절감 100억 원(\(\Delta S_{\text{T6}}\))은 진료매출 2,000억 원 증대(\(\Delta Y\))와 동등한 순이익 창출 효과** 발생.

### 3. R1~R4 4대 경영 공리
- **R1. 선행타격의 법칙 (Proactive Strike)**: 적자 발생 즉시 T6(구매)와 T7(대기시간)을 선행 타격하여 순이익 확보.
- **R2. 거버넌스 불변 법칙 (Governance Invariance)**: 운영체제 없는 하드웨어 투자는 파산 유발 (**부산침례병원 800병상 파산 경고 사례**).
- **R3. 구매 20배 레버리지 (20x Purchasing Leverage)**: 수가 한계 상 황에서 자재비 1원 절감 = 매출 20원의 이익 효과.
- **R4. 4M 조직 근육 곱셈 (4M Multiplication)**: $Y = M_1 \times M_2 \times M_3 \times M_4$ 의 곱. 하나라도 0이면 전체 성과는 0.

---

## ⚡ QUICK START (실행 가이드)

### 1. 스킬 클론 (Clone Repository)
```bash
git clone https://github.com/sunjongos/park_gaeseong_consulting.git
```

### 2. 병원 경영 진단 및 오프라인 이중 보고서 생성
```bash
python scripts/build_hospital_consulting_report.py
```
- 실행 완료 시 오프라인 단일 HTML 보고서(`*_integrated.html`)가 브라우저로 자동 기동되며, MS Word 문서(`.docx`)가 동시 생성됩니다.

---

## 💯 5-LOOP QUALITY ASSURANCE (5대 무결점 규격)

1. **온톨로지 완전 연결 (Zero Floating Nodes)**: Root ➔ 4M ➔ T1~T12 ➔ 5대 성과(🏆재정, 🏥품질, ❤️환자, 🤝조직, 🌱사회) 100% 연결.
2. **T1~T12 전수 해설 수록**: 실행 정의 및 세부 목표 12개 테마 전수 명시.
3. **KaTeX 수리 방정식 명시**: 성과 수식 $Y$ 및 R3 구매 20배 레버리지 수식 렌더링.
4. **오프라인 100% 인라이닝 (Single-File Protocol)**: Vis.js, Chart.js, KaTeX 자산 100% 내장으로 외부 서버 의존도 0%.
5. **이중 포맷 출력**: 오프라인 HTML 및 공식 MS Word (.docx) 동시 발행.

---

## 🔐 LICENSE & CREDIT
- **Copyright 2026 LCK LAB & LUCA AGI SYSTEM Team.** All rights reserved.
- Based on the hospital management wisdom of CEO Park Gae-seong (Elio & Company).
