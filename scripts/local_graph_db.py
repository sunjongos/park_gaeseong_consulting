import sqlite3
import os
import json

class LocalGraphDB:
    """
    Containerized / Embedded Local Graph DB Engine
    Operates like an embedded Neo4j DB for domain-specific Neurosymbolic reasoning.
    Does not require external Neo4j server processes.
    """
    def __init__(self, db_path=None):
        if not db_path:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            db_path = os.path.join(base_dir, "db", "park_gaeseong_ontology.db")
        self.db_path = db_path

    def get_connection(self):
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"Embedded Domain Ontology DB not found at: {self.db_path}")
        return sqlite3.connect(self.db_path)

    def query_all_nodes(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, layer, group_type, properties_json FROM nodes")
        rows = cursor.fetchall()
        nodes = []
        for r in rows:
            nodes.append({
                "id": r[0],
                "name": r[1],
                "layer": r[2],
                "group_type": r[3],
                "properties": json.loads(r[4]) if r[4] else {}
            })
        conn.close()
        return nodes

    def query_all_edges(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT from_id, to_id, rel_type, weight FROM edges")
        rows = cursor.fetchall()
        edges = []
        for r in rows:
            edges.append({
                "from": r[0],
                "to": r[1],
                "rel_type": r[2],
                "weight": r[3]
            })
        conn.close()
        return edges

    def query_axioms(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT code, name, definition, formula FROM axioms")
        rows = cursor.fetchall()
        axioms = []
        for r in rows:
            axioms.append({
                "code": r[0],
                "name": r[1],
                "definition": r[2],
                "formula": r[3]
            })
        conn.close()
        return axioms

    def query_chapter_knowledge(self, keyword=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        if keyword:
            cursor.execute("SELECT chapter_id, title, analysis_markdown FROM chapter_knowledge WHERE title LIKE ? OR analysis_markdown LIKE ? LIMIT 5", (f"%{keyword}%", f"%{keyword}%"))
        else:
            cursor.execute("SELECT chapter_id, title, analysis_markdown FROM chapter_knowledge LIMIT 34")
        rows = cursor.fetchall()
        chapters = []
        for r in rows:
            chapters.append({
                "chapter_id": r[0],
                "title": r[1],
                "summary": r[2][:500]
            })
        conn.close()
        return chapters

    def get_full_graph_ontology(self):
        """Returns fully connected domain ontology graph schema for Neurosymbolic reasoning"""
        return {
            "nodes": self.query_all_nodes(),
            "edges": self.query_all_edges(),
            "axioms": self.query_axioms(),
            "chapters_count": len(self.query_chapter_knowledge())
        }

if __name__ == "__main__":
    graph_db = LocalGraphDB()
    ontology = graph_db.get_full_graph_ontology()
    print(f"Local Graph DB Query Success: {len(ontology['nodes'])} Nodes, {len(ontology['edges'])} Edges, {len(ontology['axioms'])} Axioms!")
