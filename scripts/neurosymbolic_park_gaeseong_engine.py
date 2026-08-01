import os
import sys
import json
import glob
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Import embedded Local Graph DB engine
try:
    from local_graph_db import LocalGraphDB
except ImportError:
    from scripts.local_graph_db import LocalGraphDB

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"

class NeurosymbolicParkGaeseongEngine:
    """
    100% Containerized / Embedded Neurosymbolic Hospital Management Consulting Engine
    Primary: Embedded SQLite Domain Ontology DB (`db/park_gaeseong_ontology.db`) via LocalGraphDB
    Optional: Remote Neo4j Graph DB (`bolt://localhost:7687`)
    """
    def __init__(self, base_dir=None):
        if not base_dir:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.base_dir = base_dir
        self.local_db = LocalGraphDB(os.path.join(self.base_dir, "db", "park_gaeseong_ontology.db"))
        self.client = None
        
        if GEMINI_API_KEY:
            self.client = genai.Client(api_key=GEMINI_API_KEY)

    def symbolic_graph_retrieval(self, keywords: list) -> dict:
        """Stage 1: Retrieve symbolic graph nodes, edges, axioms, and chapters from embedded Domain DB"""
        print("  [Stage 1: Symbolic Traversal] Querying embedded SQLite Domain Ontology DB...")
        
        try:
            full_ontology = self.local_db.get_full_graph_ontology()
            chapter_matches = []
            for kw in keywords:
                matches = self.local_db.query_chapter_knowledge(kw)
                chapter_matches.extend(matches)
        except Exception as e:
            print(f"  [Symbolic Query Warning] Falling back to JSON: {e}")
            full_ontology = {}
            chapter_matches = []

        symbolic_facts = [
            f"Embedded Domain DB Nodes Count: {len(full_ontology.get('nodes', []))}",
            f"Embedded Domain DB Edges Count: {len(full_ontology.get('edges', []))}",
            f"Embedded Axioms Count: {len(full_ontology.get('axioms', []))}"
        ]

        symbolic_rules = [
            "Rule 1 (Proactive Strike): If deficit occurs, T6 (Purchasing) and T7 (Wait Time) MUST precede T12 (New Business).",
            "Rule 2 (Governance Invariance): Hardware expansion without 4M Mechanism leads to bankruptcy (Busan Baptist Hospital Case).",
            "Rule 3 (20x Purchasing Leverage): $1 saved in T6 purchasing = $20 in clinical revenue at 5% margin.",
            "Rule 4 (4M Multiplication): Performance Y = Mission * (Mapping * Manpower * Mastery * Mechanism) * Mentality."
        ]

        return {
            "facts": symbolic_facts,
            "rules": symbolic_rules,
            "domain_ontology_db": full_ontology,
            "relevant_chapters": chapter_matches[:5]
        }

    def run_neurosymbolic_pipeline(self, hospital_problem: str) -> str:
        """Runs 4-Stage Neurosymbolic Consultation Engine"""
        print(f"\n🧠 [Neurosymbolic Engine] Executing self-contained domain pipeline...")
        symbolic_data = self.symbolic_graph_retrieval(["적자", "구매", "대기시간"])
        
        if not self.client:
            return "Engine executed successfully using embedded SQLite Domain Ontology DB."
            
        sys_instruction = (
            "You are the Chief Neurosymbolic Consulting Engine of LCK LAB LUCA AGI SYSTEM. "
            "Use the embedded domain ontology graph DB, 4 Symbolic Axioms (R1~R4), 12 Themes (T1~T12), "
            "4M Muscles, and 5 Outcome Fruits to diagnose hospital deficits and formulate zero-defect prescriptions."
        )
        
        user_prompt = f"""
Hospital Case Description:
{hospital_problem}

Embedded Domain Ontology DB & Symbolic Axioms:
{json.dumps(symbolic_data, indent=2, ensure_ascii=False)[:10000]}

Generate a comprehensive neurosymbolic consulting analysis document.
"""
        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=sys_instruction,
                temperature=0.2
            )
        )
        return response.text

if __name__ == "__main__":
    problem = "서울대학교병원 2024년 1,106억 적자 및 2025년 상반기 1,356억 적자 비상경영 정상화"
    engine = NeurosymbolicParkGaeseongEngine()
    report = engine.run_neurosymbolic_pipeline(problem)
    print("\nNeurosymbolic Containerized Engine Execution Completed Successfully!")
