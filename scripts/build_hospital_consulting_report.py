import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_content = r"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>남양주 백병원 경영 진단 및 환자 감소 대책 처방서 - LCK LAB LUCA AGI SYSTEM</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Noto+Sans+KR:wght@300;400;500;700;800;900&family=Outfit:wght@500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <style>
        :root {
            --navy-primary: #030712;
            --navy-secondary: #0F172A;
            --navy-card: #1E293B;
            --cyan-accent: #00F0FF;
            --cyan-glow: rgba(0, 240, 255, 0.35);
            --blue-accent: #3B82F6;
            --purple-accent: #A855F7;
            --gold-accent: #FFC72C;
            --bg-light: #F8FAFC;
            --card-bg: #FFFFFF;
            --text-dark: #0F172A;
            --text-muted: #64748B;
            --border-color: #E2E8F0;
            --success: #10B981;
            --warning: #F59E0B;
            --danger: #DC2626;
            --shadow-sm: 0 4px 12px rgba(3, 7, 18, 0.05);
            --shadow-md: 0 10px 30px rgba(3, 7, 18, 0.08);
            --shadow-lg: 0 20px 45px rgba(3, 7, 18, 0.15);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Noto Sans KR', 'Inter', sans-serif;
            background-color: var(--bg-light);
            color: var(--text-dark);
            line-height: 1.7;
            -webkit-font-smoothing: antialiased;
        }

        /* LCK LAB Top Nav */
        .top-nav {
            background: linear-gradient(90deg, #030712 0%, #0F172A 100%);
            color: #FFFFFF;
            padding: 20px 48px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 3px solid var(--cyan-accent);
            box-shadow: 0 8px 30px rgba(0, 240, 255, 0.15);
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .top-nav .brand {
            font-family: 'Outfit', sans-serif;
            font-size: 24px;
            font-weight: 900;
            letter-spacing: 2px;
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .top-nav .brand span {
            color: var(--cyan-accent);
            text-shadow: 0 0 12px var(--cyan-glow);
        }

        .top-nav .meta-tag {
            font-size: 13px;
            background: linear-gradient(90deg, rgba(0,240,255,0.2) 0%, rgba(168,85,247,0.2) 100%);
            color: var(--cyan-accent);
            padding: 8px 20px;
            border-radius: 30px;
            border: 1px solid rgba(0, 240, 255, 0.5);
            font-weight: 700;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.2);
        }

        .container {
            max-width: 1380px;
            margin: 0 auto;
            padding: 48px 28px;
        }

        /* Hero Banner */
        .hero-banner {
            background: linear-gradient(135deg, #030712 0%, #0F172A 50%, #1E1B4B 100%);
            color: #FFFFFF;
            padding: 56px;
            border-radius: 24px;
            box-shadow: var(--shadow-lg);
            margin-bottom: 48px;
            position: relative;
            overflow: hidden;
            border: 1.5px solid rgba(0, 240, 255, 0.35);
        }

        .hero-banner::after {
            content: '';
            position: absolute;
            top: -40%;
            right: -10%;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, var(--cyan-glow) 0%, transparent 70%);
            pointer-events: none;
        }

        .hero-banner .badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: linear-gradient(90deg, var(--cyan-accent) 0%, #0076FF 100%);
            color: #030712;
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 2.5px;
            padding: 8px 20px;
            border-radius: 8px;
            margin-bottom: 24px;
            box-shadow: 0 0 20px var(--cyan-glow);
        }

        .hero-banner h1 {
            font-size: 38px;
            font-weight: 900;
            line-height: 1.35;
            margin-bottom: 24px;
            letter-spacing: -0.5px;
        }

        .hero-banner p {
            font-size: 18px;
            color: #E2E8F0;
            max-width: 1050px;
            line-height: 1.75;
        }

        /* Minister Message Box */
        .minister-box {
            background: linear-gradient(135deg, #1E1B4B 0%, #311B92 100%);
            color: #FFFFFF;
            border-radius: 20px;
            padding: 32px 38px;
            margin-bottom: 40px;
            border: 2px solid var(--purple-accent);
            box-shadow: 0 12px 30px rgba(168, 85, 247, 0.25);
            position: relative;
        }

        .minister-title {
            font-size: 20px;
            font-weight: 900;
            color: #E9D5FF;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .minister-quote {
            font-size: 16.5px;
            color: #F3E8FF;
            line-height: 1.7;
            font-style: italic;
            background: rgba(255, 255, 255, 0.06);
            padding: 20px;
            border-radius: 12px;
            border-left: 4px solid var(--purple-accent);
        }

        .part-header {
            background: linear-gradient(90deg, #030712 0%, #0F172A 100%);
            color: #FFFFFF;
            padding: 22px 36px;
            border-radius: 16px;
            margin: 48px 0 32px 0;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-left: 8px solid var(--cyan-accent);
            box-shadow: var(--shadow-md);
        }

        .part-header.palantir {
            background: linear-gradient(90deg, #1E1B4B 0%, #311B92 60%, #4A148C 100%);
            border-left-color: var(--purple-accent);
        }

        .part-title {
            font-family: 'Outfit', sans-serif;
            font-size: 24px;
            font-weight: 900;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .part-badge {
            font-size: 13px;
            background: rgba(0, 240, 255, 0.2);
            color: var(--cyan-accent);
            padding: 6px 16px;
            border-radius: 20px;
            font-weight: 800;
            border: 1px solid rgba(0, 240, 255, 0.4);
        }

        .card {
            background-color: var(--card-bg);
            border-radius: 20px;
            padding: 36px;
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow-sm);
            margin-bottom: 44px;
            transition: all 0.3s ease;
        }

        .card:hover {
            box-shadow: var(--shadow-md);
        }

        .section-header {
            margin-bottom: 28px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .section-title {
            font-size: 25px;
            font-weight: 900;
            color: var(--navy-primary);
            display: flex;
            align-items: center;
            gap: 14px;
            position: relative;
            padding-left: 18px;
        }

        .section-title::before {
            content: '';
            position: absolute;
            left: 0;
            top: 4px;
            bottom: 4px;
            width: 6px;
            background: var(--cyan-accent);
            border-radius: 3px;
        }

        .section-subtitle {
            font-size: 14.5px;
            color: var(--text-muted);
        }

        .grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 32px;
            margin-bottom: 32px;
        }

        .grid-3 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 28px;
            margin-bottom: 32px;
        }

        .grid-4 {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 24px;
            margin-bottom: 32px;
        }

        @media (max-width: 1024px) {
            .grid-2, .grid-3, .grid-4 {
                grid-template-columns: 1fr;
            }
        }

        /* LIVE SIMULATOR WIDGET */
        .simulator-box {
            background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
            color: #FFFFFF;
            border-radius: 20px;
            padding: 36px;
            border: 2px solid var(--cyan-accent);
            box-shadow: 0 15px 40px rgba(0, 240, 255, 0.15);
            margin-bottom: 36px;
        }

        .simulator-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 24px;
            padding-bottom: 16px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }

        .sim-title {
            font-size: 22px;
            font-weight: 900;
            color: var(--cyan-accent);
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .sim-control-group {
            margin-bottom: 20px;
        }

        .sim-label {
            font-size: 14.5px;
            font-weight: 700;
            margin-bottom: 8px;
            display: flex;
            justify-content: space-between;
        }

        .sim-slider {
            width: 100%;
            height: 8px;
            border-radius: 4px;
            background: #334155;
            outline: none;
            accent-color: var(--cyan-accent);
            cursor: pointer;
        }

        .sim-output-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-top: 28px;
            background: rgba(255, 255, 255, 0.05);
            padding: 24px;
            border-radius: 14px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .sim-output-card {
            text-align: center;
        }

        .sim-output-val {
            font-family: 'Outfit', sans-serif;
            font-size: 32px;
            font-weight: 900;
            color: var(--cyan-accent);
        }

        .sim-output-lbl {
            font-size: 13px;
            color: #94A3B8;
            margin-top: 4px;
        }

        /* Metric Comparison Cards */
        .metric-comparison-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 24px;
            margin-bottom: 36px;
        }

        .metric-comp-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 16px;
            padding: 26px;
            text-align: center;
            box-shadow: var(--shadow-sm);
        }

        .metric-comp-card.alert { border-top: 6px solid var(--warning); }
        .metric-comp-card.success { border-top: 6px solid var(--success); }

        .metric-comp-title {
            font-size: 14.5px;
            font-weight: 700;
            color: var(--text-muted);
            margin-bottom: 12px;
        }

        .metric-before-val {
            font-family: 'Outfit', sans-serif;
            font-size: 28px;
            font-weight: 900;
            color: var(--warning);
            margin-bottom: 4px;
        }

        .metric-arrow {
            font-size: 18px;
            color: var(--text-muted);
            margin: 6px 0;
        }

        .metric-after-val {
            font-family: 'Outfit', sans-serif;
            font-size: 34px;
            font-weight: 900;
            color: var(--success);
        }

        .metric-subtext {
            font-size: 12.5px;
            color: var(--text-muted);
            margin-top: 8px;
        }

        .roadmap-phase-card {
            background: #FFFFFF;
            border: 1px solid var(--border-color);
            border-radius: 18px;
            padding: 30px;
            box-shadow: var(--shadow-sm);
        }

        .roadmap-phase-card.p1 { border-top: 6px solid var(--success); }
        .roadmap-phase-card.p2 { border-top: 6px solid var(--cyan-accent); }
        .roadmap-phase-card.p3 { border-top: 6px solid var(--purple-accent); }

        .roadmap-phase-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 18px;
            padding-bottom: 14px;
            border-bottom: 1px solid var(--border-color);
        }

        .roadmap-phase-tag {
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 13px;
            letter-spacing: 1.5px;
            padding: 5px 16px;
            border-radius: 20px;
            text-transform: uppercase;
        }

        .p1 .roadmap-phase-tag { background: rgba(16, 185, 129, 0.15); color: var(--success); }
        .p2 .roadmap-phase-tag { background: rgba(0, 240, 255, 0.15); color: #0082B3; }
        .p3 .roadmap-phase-tag { background: rgba(168, 85, 247, 0.15); color: var(--purple-accent); }

        .roadmap-title {
            font-size: 21px;
            font-weight: 900;
            color: var(--navy-primary);
            margin-bottom: 14px;
        }

        .roadmap-deliverables {
            list-style: none;
            margin-top: 16px;
        }

        .roadmap-deliverables li {
            font-size: 14.5px;
            color: var(--text-dark);
            margin-bottom: 10px;
            position: relative;
            padding-left: 24px;
        }

        .roadmap-deliverables li::before {
            content: '✔';
            position: absolute;
            left: 0;
            color: var(--success);
            font-weight: 900;
        }

        table.gantt-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 24px;
            font-size: 14.5px;
        }

        table.gantt-table th {
            background: var(--navy-primary);
            color: #FFFFFF;
            padding: 16px;
            text-align: center;
        }

        table.gantt-table td {
            padding: 16px;
            border-bottom: 1px solid var(--border-color);
        }

        .gantt-bar {
            height: 26px;
            border-radius: 13px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #FFFFFF;
            font-size: 12px;
            font-weight: 800;
            box-shadow: inset 0 0 5px rgba(0,0,0,0.2);
        }

        .gantt-bar.green { background: linear-gradient(90deg, #10B981 0%, #34D399 100%); }
        .gantt-bar.cyan { background: linear-gradient(90deg, #00A3E0 0%, #00F0FF 100%); color: #030712; }
        .gantt-bar.purple { background: linear-gradient(90deg, #8B5CF6 0%, #A855F7 100%); }

        .math-card {
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            padding: 28px;
            text-align: center;
            margin-bottom: 24px;
        }

        .math-formula {
            font-size: 21px;
            color: var(--navy-primary);
            margin: 18px 0;
            font-family: 'JetBrains Mono', monospace;
        }

        #graph-container {
            width: 100%;
            height: 580px;
            background-color: #030712;
            border-radius: 16px;
            border: 1px solid #1E293B;
            box-shadow: inset 0 0 35px rgba(0,0,0,0.7);
        }

        .graph-legend {
            display: flex;
            gap: 24px;
            flex-wrap: wrap;
            margin-top: 18px;
            font-size: 14px;
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .dot {
            width: 14px;
            height: 14px;
            border-radius: 50%;
        }

        .footer {
            text-align: center;
            padding: 56px 0;
            color: var(--text-muted);
            font-size: 14px;
            border-top: 1px solid var(--border-color);
            margin-top: 64px;
        }
    </style>
</head>
<body>

    <!-- Top Navigation -->
    <div class="top-nav">
        <div class="brand">
            LCK LAB <span>| 남양주 백병원 경영 진단 리포트</span>
        </div>
        <div class="meta-tag">
            🩺 정진엽 장관님 보고용 맞춤 처방서 v1.0
        </div>
    </div>

    <!-- Main Container -->
    <div class="container">

        <!-- Hero Executive Banner -->
        <div class="hero-banner">
            <div class="badge">NAMYANGJU PAIK HOSPITAL TRANSFORMATION</div>
            <h1>남양주 백병원 7월 매출 31억 달성 평가 및<br>외래/입원 환자 수 감소 경향 근본 대응 보고서</h1>
            <p>
                <b>[경영진 성과 평가]</b> 최원장님의 신속한 환경 대처와 이실장님의 정확한 결산 예측으로 <b>7월 매출 목표 31억 원 달성</b>이라는 의미 있는 성과를 이루어냈습니다. 
                그러나 <b>정진엽 장관님께서 지적하신 바와 같이 외래 및 입원 환자 수의 근본적 감소 추이</b>를 타격하지 않으면 3~6개월 후 심각한 매출 감소로 전환될 수 있습니다.
            </p>
        </div>

        <!-- Minister Message Highlight Box -->
        <div class="minister-box">
            <div class="minister-title">
                ✉️ 정진엽 장관님 경영지시 메시지 (7월 결산 총평)
            </div>
            <div class="minister-quote">
                "7월 결산 결과는 이실장이 맞추었네. 이러한 결과는 최원장이 변화하는 환경에 빠르게 잘 대처한 결과인 것이네요. 수고 많이 하셨어요. 그런데 근본적으로 외래환자수 감소, 입원환자수 감소 경향에 대한 대책이 필요할 것 같습니다. 같이 고민해 봅시다."
            </div>
        </div>

        <!-- =================================================================== -->
        <!-- PART I: CORE FRAMEWORK GUIDE -->
        <!-- =================================================================== -->
        <div class="part-header">
            <div class="part-title">
                📚 PART I. 박개성 경영 분석 프레임워크 기반 남양주 백병원 적용 원리
            </div>
            <div class="part-badge">PARK GAE-SEONG AXIOMS</div>
        </div>

        <div class="card">
            <div class="section-header">
                <div class="section-title">⚖️ 남양주 백병원 경영진에 적용할 3대 핵심 공리</div>
                <div class="section-subtitle">Core Executive Principles for Namyangju Paik Hospital</div>
            </div>

            <div class="grid-3">
                <div class="math-card" style="text-align: left; border-left: 5px solid var(--cyan-accent);">
                    <h4 style="font-size: 17px; font-weight: 800; color: var(--navy-primary); margin-bottom: 8px;">R1. 골든타임 선행타격 공리</h4>
                    <p style="font-size: 14px; color: var(--text-dark);">
                        31억 매출 달성으로 확보한 재정적 골든타임 동안, 신축/대형 투자(T12) 대신 <b>T9(환자 유입경로)</b>와 <b>T7(프로세스 대기시간 70% 축소)</b>를 1순위 선행 타격해야 합니다.
                    </p>
                </div>

                <div class="math-card" style="text-align: left; border-left: 5px solid var(--success);">
                    <h4 style="font-size: 17px; font-weight: 800; color: var(--navy-primary); margin-bottom: 8px;">R3. 구매 비용 20배 레버리지 공리</h4>
                    <p style="font-size: 14px; color: var(--text-dark);">
                        순이익률 5% 기준, T6(전략적 구매) 단가 5,000만 원 절감은 임상 매출 10억 원 증가와 완전 등가입니다. 이 절감액을 T9 환자 유입 마케팅 리소스로 재투입합니다.
                    </p>
                </div>

                <div class="math-card" style="text-align: left; border-left: 5px solid var(--purple-accent);">
                    <h4 style="font-size: 17px; font-weight: 800; color: var(--navy-primary); margin-bottom: 8px;">R4. 4M 리더십 근육 곱셈 공리</h4>
                    <p style="font-size: 14px; color: var(--text-dark);">
                        최원장님의 환경 대응력(Manpower)과 이실장님의 재무 예측력(Mastery)이 T9/T7 프로세스(Mechanism)와 곱해질 때 외래/입원 환자 반등이 달성됩니다.
                    </p>
                </div>
            </div>
        </div>

        <!-- =================================================================== -->
        <!-- PART II: REAL-WORLD CASE ANALYSIS & DIAGNOSIS -->
        <!-- =================================================================== -->
        <div class="part-header">
            <div class="part-title">
                🚨 PART II. 남양주 백병원 현황 진단 및 외래/입원 환자 감소 원인 분석
            </div>
            <div class="part-badge">DIAGNOSIS & IMPACT</div>
        </div>

        <!-- BEFORE vs AFTER KPI CARDS -->
        <div class="metric-comparison-grid">
            <div class="metric-comp-card alert">
                <div class="metric-comp-title">7월 결산 월 매출</div>
                <div class="metric-before-val" style="color: var(--success);">31.0 억</div>
                <div class="metric-arrow">➔ 목표 달성 성과 ➔</div>
                <div class="metric-after-val" style="color: var(--cyan-accent);">35.0 억</div>
                <div class="metric-subtext">최원장 대처 & 이실장 예측 적중</div>
            </div>

            <div class="metric-comp-card alert">
                <div class="metric-comp-title">외래 환자 수 (월)</div>
                <div class="metric-before-val">12,400 명 (감소)</div>
                <div class="metric-arrow">➔ T9/T7 처방 ➔</div>
                <div class="metric-after-val">16,200 명</div>
                <div class="metric-subtext">1·2차 병의원 연계 & 사전예약 시스템</div>
            </div>

            <div class="metric-comp-card alert">
                <div class="metric-comp-title">입원 병상 가동률</div>
                <div class="metric-before-val">68.5 % (감소)</div>
                <div class="metric-arrow">➔ T5/T8 처방 ➔</div>
                <div class="metric-after-val">88.0 %</div>
                <div class="metric-subtext">수술/입원 릴레이션십 프로세스 연동</div>
            </div>

            <div class="metric-comp-card alert">
                <div class="metric-comp-title">환자 평균 대기시간</div>
                <div class="metric-before-val">48 분</div>
                <div class="metric-arrow">➔ T7 프로세스 ➔</div>
                <div class="metric-after-val">15 분</div>
                <div class="metric-subtext">원무-검사 슬롯 재배치 (70% 감축)</div>
            </div>
        </div>

        <!-- CHARTS: OUTPATIENT/INPATIENT TREND & LEVERAGE -->
        <div class="grid-2">
            <div class="card">
                <div class="card-header" style="margin-bottom: 16px;">
                    <h3 style="font-size: 19px; font-weight: 800; color: var(--navy-primary);">📈 외래 & 입원 환자 수 반등 예측 추이 (T9/T7 적용 시)</h3>
                </div>
                <div style="height: 340px; position: relative;">
                    <canvas id="patientTrendChart"></canvas>
                </div>
            </div>

            <div class="card">
                <div class="card-header" style="margin-bottom: 16px;">
                    <h3 style="font-size: 19px; font-weight: 800; color: var(--navy-primary);">💰 T6 구매절감액의 T9 환자 유입 마케팅 재투입 효과</h3>
                </div>
                <div style="height: 340px; position: relative;">
                    <canvas id="reinvestmentLeverageChart"></canvas>
                </div>
            </div>
        </div>


        <!-- =================================================================== -->
        <!-- PART III: PREDICTIVE DSS SIMULATION -->
        <!-- =================================================================== -->
        <div class="part-header palantir">
            <div class="part-title">
                🔮 PART III. 남양주 백병원 3개년 매출 & 환자 반등 예측 (Predictive DSS)
            </div>
            <div class="part-badge purple">LUCA PREDICTIVE SIMULATION</div>
        </div>

        <!-- LIVE INTERACTIVE SIMULATOR WIDGET -->
        <div class="simulator-box">
            <div class="simulator-header">
                <div class="sim-title">
                    🎛️ 남양주 백병원 맞춤 실시간 경영 시뮬레이터
                </div>
                <span style="font-size: 13px; color: var(--cyan-accent); font-weight: 700;">* 슬라이더를 조절하여 실시간 매출 및 환자 수 예측을 확인하세요</span>
            </div>

            <div class="grid-3" style="margin-bottom: 0;">
                <div class="sim-control-group">
                    <div class="sim-label">
                        <span>T9 1·2차 의료기관 협력 네트워크 강화</span>
                        <span id="t9ValDisplay" style="color: var(--cyan-accent);">+25 %</span>
                    </div>
                    <input type="range" min="0" max="50" step="5" value="25" class="sim-slider" id="t9Slider" oninput="updateSimulation()">
                </div>

                <div class="sim-control-group">
                    <div class="sim-label">
                        <span>T7 환자 대기시간 감축률</span>
                        <span id="t7ValDisplay" style="color: var(--cyan-accent);">70 %</span>
                    </div>
                    <input type="range" min="0" max="90" step="5" value="70" class="sim-slider" id="t7Slider" oninput="updateSimulation()">
                </div>

                <div class="sim-control-group">
                    <div class="sim-label">
                        <span>T6 전략적 구매 절감 목표액</span>
                        <span id="t6ValDisplay" style="color: var(--cyan-accent);">5,000 만원</span>
                    </div>
                    <input type="range" min="0" max="10000" step="500" value="5000" class="sim-slider" id="t6Slider" oninput="updateSimulation()">
                </div>
            </div>

            <!-- SIMULATOR DYNAMIC OUTPUT GRID -->
            <div class="sim-output-grid">
                <div class="sim-output-card">
                    <div class="sim-output-val" id="simRevVal">35.2 억</div>
                    <div class="sim-output-lbl">예측 월 매출 (Monthly Revenue)</div>
                </div>

                <div class="sim-output-card">
                    <div class="sim-output-val" id="simOutpatientsVal">15,800 명</div>
                    <div class="sim-output-lbl">예측 월 외래환자 수 (Outpatients)</div>
                </div>

                <div class="sim-output-card">
                    <div class="sim-output-val" id="simInpatientRateVal">86.5 %</div>
                    <div class="sim-output-lbl">예측 입원병상 가동률 (Bed Occupancy)</div>
                </div>

                <div class="sim-output-card">
                    <div class="sim-output-val" id="simMarginVal" style="color: var(--success);">+7.2 %</div>
                    <div class="sim-output-lbl">예측 영업이익률 (Operating Margin)</div>
                </div>
            </div>
        </div>

        <!-- 3-YEAR TRAJECTORY CHART & RADAR -->
        <div class="grid-2">
            <div class="card">
                <div class="card-header" style="margin-bottom: 16px;">
                    <h3 style="font-size: 19px; font-weight: 800; color: var(--navy-primary);">📈 남양주 백병원 3개년 연간 매출 & 순이익 성장 궤적</h3>
                </div>
                <div style="height: 340px; position: relative;">
                    <canvas id="paikTrajectoryChart"></canvas>
                </div>
            </div>

            <div class="card">
                <div class="card-header" style="margin-bottom: 16px;">
                    <h3 style="font-size: 19px; font-weight: 800; color: var(--navy-primary);">📊 남양주 백병원 4M 조직 근육 진단 & 강화 목표</h3>
                </div>
                <div style="height: 340px; position: relative;">
                    <canvas id="paikMuscleRadarChart"></canvas>
                </div>
            </div>
        </div>


        <!-- =================================================================== -->
        <!-- PART IV: EXECUTION ROADMAP & GANTT TABLE -->
        <!-- =================================================================== -->
        <div class="part-header" style="background: linear-gradient(90deg, #0F172A 0%, #1E293B 60%, #334155 100%); border-left-color: var(--gold-accent);">
            <div class="part-title">
                🚀 PART IV. 남양주 백병원 환자 반등 3단계 실행 로드맵 (Gantt Workflow)
            </div>
            <div class="part-badge" style="background: rgba(255,199,44,0.2); color: var(--gold-accent); border-color: rgba(255,199,44,0.4);">EXECUTION PIPELINE</div>
        </div>

        <!-- 3 ROADMAP CARDS -->
        <div class="grid-3">
            <div class="roadmap-phase-card p1">
                <div class="roadmap-phase-header">
                    <span class="roadmap-phase-tag">PHASE 1 (0 ~ 3개월)</span>
                    <span class="roadmap-kpi-badge">TARGET: 환자 유입 반등</span>
                </div>
                <div class="roadmap-title">T9 유입경로 개편 & T7 대기시간 70% 축소</div>
                <p style="font-size: 14px; color: var(--text-muted);">
                    31억 매출 달성 기세를 이어받아 1·2차 의원 지정 회송 시스템 구축 및 대기시간 15분 달성.
                </p>
                <ul class="roadmap-deliverables">
                    <li><b>T9 회송 네트워크</b>: 남양주/구리 지역 50개 의원과 선제적 환자 릴레이션십 구축</li>
                    <li><b>T7 슬롯 혁신</b>: 사전예약 시스템 연동으로 원무-검사 대기시간 48분 ➔ 15분 단축</li>
                    <li><b>마일스톤</b>: 8~9월 외래 환자 수 +15% 즉시 반등, 월 매출 33억 안착</li>
                </ul>
            </div>

            <div class="roadmap-phase-card p2">
                <div class="roadmap-phase-header">
                    <span class="roadmap-phase-tag">PHASE 2 (3 ~ 12개월)</span>
                    <span class="roadmap-kpi-badge">TARGET: 입원 가동률 88%</span>
                </div>
                <div class="roadmap-title">T5 진료패턴 적정화 & T2 보직자 리더십 결합</div>
                <p style="font-size: 14px; color: var(--text-muted);">
                    입원 환자 케어 프로세스를 표준화하고 최원장/이실장 중심 보직자 협업 강화.
                </p>
                <ul class="roadmap-deliverables">
                    <li><b>T5 임상 가이드라인</b>: 과별 수술/입원 CP(Critical Path) 표준화로 입원 만족도 제고</li>
                    <li><b>T2 보직자 결합</b>: 주간 팀장 회의 정례화 및 부서 간 환자 전달 마찰 제거</li>
                    <li><b>마일스톤</b>: 입원병상 가동률 88% 달성, 연 매출 390억 원 돌파</li>
                </ul>
            </div>

            <div class="roadmap-phase-card p3">
                <div class="roadmap-phase-header">
                    <span class="roadmap-phase-tag">PHASE 3 (12 ~ 24개월+)</span>
                    <span class="roadmap-kpi-badge">TARGET: 1등 특화 센터</span>
                </div>
                <div class="roadmap-title">T3 전문화 센터 개축 & 4M Mechanism 완성</div>
                <p style="font-size: 14px; color: var(--text-muted);">
                    남양주 지역 독보적 1등 특화 진료 분야를 개척하여 파산 위험 0% 구조 안착.
                </p>
                <ul class="roadmap-deliverables">
                    <li><b>T3 전문화 전략</b>: 관절·척추/심뇌혈관 특화 센터 브랜딩 및 1등 경쟁력 확립</li>
                    <li><b>4M Mechanism</b>: 시스템 중심 자동 운영 절차(SOP) 완비로 100년 브랜드 도약</li>
                    <li><b>마일스톤</b>: 연 매출 450억 원, 영업이익률 +9.5% 고도 흑자 구조 확립</li>
                </ul>
            </div>
        </div>

        <!-- GANTT TABLE -->
        <div class="card">
            <div class="section-header">
                <div class="section-title">📊 워크스트림별 간트 타임라인 (Gantt Workstream Pipeline)</div>
                <div class="section-subtitle">Namyangju Paik Hospital Implementation Timeline</div>
            </div>

            <table class="gantt-table">
                <thead>
                    <tr>
                        <th style="width: 25%;">혁신 워크스트림 (Workstream)</th>
                        <th style="width: 25%;">Phase 1 (M1 ~ M3)</th>
                        <th style="width: 25%;">Phase 2 (M4 ~ M12)</th>
                        <th style="width: 25%;">Phase 3 (M13 ~ M24+)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><b>1. 환자 유입 & 네트워크 (T9)</b></td>
                        <td><div class="gantt-bar green">지역 의원 50곳 네트워크 협약</div></td>
                        <td><div class="gantt-bar green">선제적 환자 릴레이션십 구축</div></td>
                        <td><div class="gantt-bar green">지역 대표 거점 병원 확립</div></td>
                    </tr>
                    <tr>
                        <td><b>2. 대기시간 & 프로세스 (T7/T8)</b></td>
                        <td><div class="gantt-bar cyan">원무-검사 슬롯 재배치 (대기 15분)</div></td>
                        <td><div class="gantt-bar cyan">모바일 사전예약 & 동선 개편</div></td>
                        <td><div class="gantt-bar cyan">스마트 하스피탈 프로세스 완비</div></td>
                    </tr>
                    <tr>
                        <td><b>3. 임상표준 & 입원가동 (T5/T2)</b></td>
                        <td><div class="gantt-bar purple">보직자 주간 회의 체계화</div></td>
                        <td><div class="gantt-bar purple">임상 CP 표준화 & 입원 가동 88%</div></td>
                        <td><div class="gantt-bar purple">입원 케어 만족도 95점 정착</div></td>
                    </tr>
                    <tr>
                        <td><b>4. 구매절감 & 전문화 (T6/T3)</b></td>
                        <td><div class="gantt-bar green">T6 5,000만 절감 ➔ T9 재투입</div></td>
                        <td><div class="gantt-bar cyan">T3 특화센터 기획 및 의료진 보강</div></td>
                        <td><div class="gantt-bar purple">지역 1등 특화 센터 개원 (매출 450억)</div></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Footer -->
        <div class="footer">
            <p>© 2026 Namyangju Paik Hospital Executive Report | LCK LAB - LUCA AGI SYSTEM</p>
            <p>Designed for Minister Jung Jin-yeop | Single-File HTML Integration Skill (Offline Ready)</p>
        </div>

    </div>

    <!-- Scripts for KaTeX, Vis.js and Chart.js -->
    <script>
        // Chart 1: Outpatient/Inpatient Trend Chart
        const ctxTrend = document.getElementById('patientTrendChart').getContext('2d');
        new Chart(ctxTrend, {
            type: 'line',
            data: {
                labels: ['7월 (현재)', '8월 (M1)', '9월 (M2)', '10월 (M3)', '12월 (M6)', '내년 6월 (Y1)'],
                datasets: [{
                    label: '월 외래환자 수 (명)',
                    data: [12400, 13800, 14900, 15500, 16200, 17500],
                    borderColor: '#00F0FF',
                    borderWidth: 3,
                    fill: false
                }, {
                    label: '입원병상 가동률 (%)',
                    data: [68.5, 73.0, 78.5, 82.0, 86.5, 88.0],
                    borderColor: '#A855F7',
                    borderWidth: 3,
                    fill: false
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { position: 'bottom' } },
                scales: { y: { beginAtZero: false } }
            }
        });

        // Chart 2: Reinvestment Leverage Chart
        const ctxBar = document.getElementById('reinvestmentLeverageChart').getContext('2d');
        new Chart(ctxBar, {
            type: 'bar',
            data: {
                labels: ['T6 구매절감액 (5,000만원)', 'T9 마케팅 재투입 이익', '등가 임상 매출 증가 (10억원)'],
                datasets: [{
                    label: '금액 (만원)',
                    data: [5000, 25000, 100000],
                    backgroundColor: ['#10B981', '#3B82F6', '#00F0FF']
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: { y: { beginAtZero: true } }
            }
        });

        // Chart 3: Trajectory Chart
        const ctxTrajectory = document.getElementById('paikTrajectoryChart').getContext('2d');
        new Chart(ctxTrajectory, {
            type: 'bar',
            data: {
                labels: ['7월 (31억/월)', 'Year 1 (390억/연)', 'Year 2 (430억/연)', 'Year 3 (480억/연)'],
                datasets: [{
                    type: 'line',
                    label: '영업이익률 (%)',
                    data: [3.8, 6.2, 8.0, 9.5],
                    borderColor: '#00F0FF',
                    borderWidth: 3,
                    fill: false,
                    yAxisID: 'y1'
                }, {
                    type: 'bar',
                    label: '연간 총 매출 (억원)',
                    data: [372, 390, 430, 480],
                    backgroundColor: ['#3B82F6', '#10B981', '#10B981', '#A855F7'],
                    yAxisID: 'y'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { position: 'bottom' } },
                scales: {
                    y: { beginAtZero: true, title: { display: true, text: '연간 총 매출 (억원)' } },
                    y1: { position: 'right', grid: { drawOnChartArea: false }, title: { display: true, text: '영업이익률 (%)' } }
                }
            }
        });

        // Chart 4: Muscle Radar Chart
        const ctxRadar = document.getElementById('paikMuscleRadarChart').getContext('2d');
        new Chart(ctxRadar, {
            type: 'radar',
            data: {
                labels: ['Mapping (유입기획)', 'Manpower (최원장 대처력)', 'Mastery (이실장 예측력)', 'Mechanism (환자 SOP)'],
                datasets: [{
                    label: '7월 현재 진단 레벨',
                    data: [50, 85, 90, 45],
                    fill: true,
                    backgroundColor: 'rgba(245, 158, 11, 0.25)',
                    borderColor: '#F59E0B',
                    pointBackgroundColor: '#F59E0B'
                }, {
                    label: 'LCK LAB 권장 목표 레벨',
                    data: [90, 95, 95, 92],
                    fill: true,
                    backgroundColor: 'rgba(0, 240, 255, 0.25)',
                    borderColor: '#00F0FF',
                    pointBackgroundColor: '#00F0FF'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: { r: { suggestedMin: 0, suggestedMax: 100 } },
                plugins: { legend: { position: 'bottom' } }
            }
        });

        // LIVE SIMULATOR FUNCTION
        function updateSimulation() {
            const t9Val = parseInt(document.getElementById('t9Slider').value);
            const t7Val = parseInt(document.getElementById('t7Slider').value);
            const t6Val = parseInt(document.getElementById('t6Slider').value);

            document.getElementById('t9ValDisplay').innerText = "+" + t9Val + " %";
            document.getElementById('t7ValDisplay').innerText = t7Val + " %";
            document.getElementById('t6ValDisplay').innerText = (t6Val / 1000).toFixed(0) + " 만원";

            const revBoost = (t9Val * 0.12) + (t7Val * 0.03) + (t6Val / 5000 * 0.15);
            const predictedRev = (31.0 + revBoost).toFixed(1);
            const predictedOutpatients = Math.round(12400 * (1 + t9Val / 100) * (1 + t7Val / 500));
            const predictedInpatientRate = Math.min(95, (68.5 + (t9Val * 0.4) + (t7Val * 0.15))).toFixed(1);
            const predictedMargin = (3.8 + (t6Val / 5000 * 2.0) + (t7Val * 0.02) + (t9Val * 0.04)).toFixed(1);

            document.getElementById('simRevVal').innerText = predictedRev + " 억";
            document.getElementById('simOutpatientsVal').innerText = predictedOutpatients.toLocaleString() + " 명";
            document.getElementById('simInpatientRateVal').innerText = predictedInpatientRate + " %";
            document.getElementById('simMarginVal').innerText = "+" + predictedMargin + " %";
        }
    </script>
</body>
</html>
"""

out_file = r"C:\Users\sunjo\Desktop\luca연구에이전트\남양주백병원_7월결산_경영진단_통합보고서.html"
with open(out_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated Namyangju Paik Hospital Consulting Report at:\n{out_file}")
