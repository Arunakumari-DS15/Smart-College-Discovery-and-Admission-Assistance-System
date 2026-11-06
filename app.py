from flask import Flask, render_template, request, jsonify
from collections import deque
import heapq

app = Flask(__name__)

# Public-facing information gathered from the college's official website.
# Verify every item with the Principal/HOD/admin before public deployment.
PROGRAMS = [
    {"name":"B.Tech CSE", "group":"B.Tech", "level":"Undergraduate",
     "description":"Computer Science and Engineering: programming, software development and computational problem-solving.",
     "keywords":["btech","cse","computer science","programming","software","engineering"],
     "interests":["computers","software","programming","technology","engineering"]},
    {"name":"B.Tech CSE – AI", "group":"B.Tech", "level":"Undergraduate",
     "description":"Computer Science and Engineering with Artificial Intelligence.",
     "keywords":["ai","artificial intelligence","machine learning","cse ai","btech"],
     "interests":["ai","computers","technology","programming","data"]},
    {"name":"B.Tech ECE", "group":"B.Tech", "level":"Undergraduate",
     "description":"Electronics and Communication Engineering.",
     "keywords":["ece","electronics","communication","circuits","btech"],
     "interests":["electronics","communication","engineering","technology"]},
    {"name":"B.Tech EEE", "group":"B.Tech", "level":"Undergraduate",
     "description":"Electrical and Electronics Engineering.",
     "keywords":["eee","electrical","electronics","power systems","btech"],
     "interests":["electrical","electronics","engineering","technology"]},
    {"name":"M.Tech CSE", "group":"M.Tech", "level":"Postgraduate",
     "description":"Postgraduate programme in Computer Science and Engineering.",
     "keywords":["mtech","cse","postgraduate","computer science"],
     "interests":["computers","software","research","technology"]},
    {"name":"MBA – General Management", "group":"MBA", "level":"Postgraduate",
     "description":"General Management with areas including Finance, Marketing and Human Resources, as described on the college website.",
     "keywords":["mba","management","finance","marketing","human resources","hr"],
     "interests":["business","management","finance","marketing","leadership"]},
    {"name":"MBA – Business Analytics", "group":"MBA", "level":"Postgraduate",
     "description":"Business Analytics focuses on data analysis and decision support.",
     "keywords":["mba","business analytics","analytics","data","management"],
     "interests":["business","management","data","analytics","technology"]},
    {"name":"MCA", "group":"MCA", "level":"Postgraduate",
     "description":"Master of Computer Applications.",
     "keywords":["mca","computer applications","software","programming","postgraduate"],
     "interests":["computers","software","programming","technology"]}
]

# Trie: prefix-based search.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word.lower():
            node = node.children.setdefault(ch, TrieNode())
            if word not in node.words:
                node.words.append(word)

    def search_prefix(self, prefix):
        node = self.root
        for ch in prefix.lower().strip():
            if ch not in node.children:
                return []
            node = node.children[ch]
        return node.words[:12]

trie = Trie()
for p in PROGRAMS:
    trie.insert(p["name"])
    trie.insert(p["group"])
    for keyword in p["keywords"]:
        trie.insert(keyword)

# Custom Hash Table with separate chaining.
class HashTable:
    def __init__(self, capacity=31):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def _index(self, key):
        return sum(ord(ch) for ch in key.lower()) % self.capacity

    def put(self, key, value):
        bucket = self.buckets[self._index(key)]
        for pair in bucket:
            if pair[0].lower() == key.lower():
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key):
        for stored_key, value in self.buckets[self._index(key)]:
            if stored_key.lower() == key.lower():
                return value
        return None

course_table = HashTable()
for p in PROGRAMS:
    course_table.put(p["name"], p)

# Max Heap: rank programmes by how many selected interests match.
def recommend(interests):
    heap = []
    selected = {x.lower().strip() for x in interests if x.strip()}
    for p in PROGRAMS:
        score = sum(1 for interest in selected if interest in p["interests"])
        if score:
            heapq.heappush(heap, (-score, p["name"], p))
    results = []
    while heap:
        score, _, p = heapq.heappop(heap)
        results.append({"score": -score, "program": p})
    return results

# Graph: college information categories and BFS traversal.
GRAPH = {
    "College": ["Academics", "Admissions", "Campus Life", "Achievements", "Placements"],
    "Academics": ["B.Tech", "M.Tech", "MBA", "MCA"],
    "Admissions": ["Admission Enquiry", "Eligibility Information"],
    "Campus Life": ["Hostel", "Library", "Laboratories", "Transport", "Activities"],
    "Achievements": ["Awards", "Accreditations"],
    "Placements": ["Training", "Recruiters", "Placement Reports"],
    "B.Tech": [], "M.Tech": [], "MBA": [], "MCA": [],
    "Admission Enquiry": [], "Eligibility Information": [],
    "Hostel": [], "Library": [], "Laboratories": [], "Transport": [], "Activities": [],
    "Awards": [], "Accreditations": [], "Training": [], "Recruiters": [], "Placement Reports": []
}

def graph_bfs(start="College"):
    visited, order = set(), []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        queue.extend(n for n in GRAPH.get(node, []) if n not in visited)
    return order

@app.route("/")
def home():
    query = request.args.get("q", "").strip()
    search_results = trie.search_prefix(query) if query else []
    selected_course = request.args.get("course", "")
    course_info = course_table.get(selected_course) if selected_course else None
    interest_values = request.args.getlist("interest")
    recommendations = recommend(interest_values) if interest_values else []
    return render_template(
        "index.html", programs=PROGRAMS, query=query,
        search_results=search_results, selected_course=selected_course,
        course_info=course_info, selected_interests=interest_values,
        recommendations=recommendations, graph=GRAPH, bfs_order=graph_bfs()
    )

@app.route("/api/graph")
def graph_api():
    return jsonify({"graph": GRAPH, "bfs_order": graph_bfs()})

if __name__ == "__main__":
    print("\\nASHOKA SMART COLLEGE DISCOVERY")
    print("Open: http://127.0.0.1:5000\\n")
    app.run(debug=True)
