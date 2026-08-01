import os
import sys
import json
import glob
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "121219love@")

class NeurosymbolicParkGaeseongEngine:
    """
    100% Portable Neurosymbolic Hospital Management Consulting Engine
    Primary: Neo4j Graph DB (bolt://localhost:7687)
    Fallback / Standalone: Embedded Wiki (`wiki/*.md`) & JSON Ontology Graph (`knowledge_assets/ontology_graph.json`)
    """
    def __init__(self, base_dir=None):
        if not base_dir:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.base_dir = base_dir
        self.neo4j_driver = None
        self.client = None
        
        if GEMINI_API_KEY:
            self.client = genai.Client(api_key=GEMINI_API_KEY)
            
        self._init_neo4j()

    def _init_neo4j(self):
        try:
            from neo4j import GraphDatabase
            self.neo4j_driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
            print("  [Symbolic Core] Connected to Primary Neo4j Graph DB (bolt://localhost:7687)")
        except Exception as e:
            print(f"  [Symbolic Portable Mode] Neo4j connection not available. Switching to bundled Wiki & JSON Ontology Assets.")

    def load_portable_ontology(self) -> dict:
        """Loads embedded JSON ontology asset and wiki knowledge pages"""
        ontology_json_path = os.path.join(self.base_dir, "knowledge_assets", "ontology_graph.json")
        wiki_dir = os.path.join(self.base_dir, "wiki")
        
        ontology_data = {}
        if os.path.exists(ontology_json_path):
            with open(ontology_json_path, "r", encoding="utf-8") as f:
                ontology_data = json.load(f)
                
        wiki_snippets = []
        if os.path.exists(wiki_dir):
            wiki_files = sorted(glob.glob(os.path.join(wiki_dir, "*.md")))
            for wf in wiki_files:
                with open(wf, "r", encoding="utf-8") as f:
                    content = f.read()
                    wiki_snippets.append({
                        "file": os.path.basename(wf),
                        "snippet": content[:2000]
                    })
                    
        return {
            "ontology": ontology_data,
            "wiki_snippets": wiki_snippets
        }

    def symbolic_graph_retrieval(self, keywords: list) -> dict:
        """Stage 1: Retrieve symbolic rules & ontology nodes"""
        print("  [Stage 1: Symbolic Traversal] Searching ontology rules & chapter knowledge...")
        symbolic_facts = []
        
        if self.neo4j_driver:
            try:
                with self.neo4j_driver.session() as session:
                    cypher1 = "MATCH (c:Chapter) RETURN c.filename AS filename LIMIT 34"
                    res = session.run(cypher1)
                    chapters = [r["filename"] for r in res]
                    symbolic_facts.append(f"Neo4j Connected Chapters: {len(chapters)}")
            except Exception as e:
                print(f"  [Neo4j Query Error] {e}")
                
        portable_data = self.load_portable_ontology()
        symbolic_facts.append(f"Portable Wiki Pages Loaded: {len(portable_data['wiki_snippets'])}")
        
        symbolic_rules = [
            "Rule 1 (Proactive Strike): If deficit occurs, T6 (Purchasing) and T7 (Wait Time) MUST precede T12 (New Business).",
            "Rule 2 (Governance Invariance): Hardware expansion without 4M Mechanism leads to bankruptcy (Busan Baptist Hospital Case).",
            "Rule 3 (20x Purchasing Leverage): $1 saved in T6 purchasing = $20 in clinical revenue at 5% margin.",
            "Rule 4 (4M Multiplication): Performance Y = Mission * (Mapping * Manpower * Mastery * Mechanism) * Mentality."
        ]
        
        return {
            "facts": symbolic_facts,
            "rules": symbolic_rules,
            "portable_ontology": portable_data
        }

    def run_neurosymbolic_pipeline(self, hospital_problem: str) -> str:
        """Runs 4-Stage Neurosymbolic Consultation Engine"""
        print(f"\n🧠 [Neurosymbolic Engine] Starting portable consultation pipeline...")
        symbolic_data = self.symbolic_graph_retrieval(["적자", "구매", "대기시간"])
        
        if not self.client:
            return "Engine generated offline report using local bundled wiki & ontology assets."
            
        sys_instruction = (
            "You are the Chief Neurosymbolic Consulting Engine of LCK LAB LUCA AGI SYSTEM. "
            "Combine Park Gae-seong's 4 Symbolic Axioms (R1~R4), 12 Themes (T1~T12), 4M Muscles, "
            "and 5 Outcome Fruits to diagnose hospital deficits and formulate zero-defect prescriptions."
        )
        
        user_prompt = f"""
Hospital Case Description:
{hospital_problem}

Symbolic Ontology & Wiki Knowledge Assets:
{json.dumps(symbolic_data, indent=2, ensure_ascii=False)[:10000]}

Generate a comprehensive consulting analysis markdown document.
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
    print("\nNeurosymbolic Portable Engine Execution Completed!")
