# 🌐 04. 온톨로지 지식 그래프 명세서 (Ontology Schema)

본 명세서는 Neo4j 지식 그래프 및 Portable JSON DB(`knowledge_assets/ontology_graph.json`)의 그래프 스키마와 노드-엣지 인과 관계를 정의합니다.

---

## 🕸️ GRAPH NODE & EDGE ARCHITECTURE (100% Fully Connected Graph)

```
[ Root Node: 1 ]
  └── [ Layer 1: 4M Muscles (Nodes 2~5) ]
        ├── M1. Mapping (Node 2)
        ├── M2. Manpower (Node 3)
        ├── M3. Mastery (Node 4)
        └── M4. Mechanism (Node 5)
              └── [ Layer 2: 12 Themes (Nodes 101~112) ]
                    ├── T1 ~ T12
                    └── [ Layer 3: 5 Outcomes (Nodes 301~305) ]
                          ├── 🏆 재정건전성 (Node 301)
                          ├── 🏥 의료품질 (Node 302)
                          ├── ❤️ 환자경험 (Node 303)
                          ├── 🤝 조직문화 (Node 304)
                          └── 🌱 사회공헌 (Node 305)
```

---

## 🔑 CYPHER QUERY PROTOCOL (Neo4j 연동 예시)

```cypher
// Query 1. 5대 성과 열매와 100% 연결된 테마 경로 매핑
MATCH (r:Hospital {name: '서울대학교병원'})-[:HAS_MUSCLE]->(m:Muscle)-[:INCLUDES]->(t:Theme)-[:PRODUCES]->(o:Outcome)
RETURN r.name, m.name, t.code, t.name, o.name;

// Query 2. R3 구매 20배 레버리지 관계 쿼리
MATCH (t:Theme {code: 'T6'})-[:PRODUCES]->(o:Outcome {id: 'O1'})
RETURN t.name, o.name, t.leverage_factor;
```
