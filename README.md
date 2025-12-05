# Linear Search Visualizer  
**Author:** Chirag Tilwani  
**Course:** CISC 121  
**Assignment:** Algorithm Visualization Project  

---

# 🔗 Live Hugging Face App  
https://huggingface.co/spaces/Chirag0831/linear_search_project  

---

# 📘 Project Overview

This project is a **visual simulation of the Linear Search algorithm** using **Python + Gradio**.  
The app takes a list of numbers and a target, then displays **each step** of the search algorithm.

The design uses a **red and black minimal theme** to make the interface clean and easy to read.

---

# 📂 Files Included

| File | Description |
|------|-------------|
| `app.py` | Main Python application with UI + algorithm |
| `requirements.txt` | Python dependencies for running the app |
| `README.md` | Full documentation (this file) |
| `screenshots/` | Visual proof: screenshots or demo GIF |

---

# 🧠 Computational Thinking Breakdown

## 1️⃣ Decomposition
The project was divided into smaller tasks:
- Build linear search algorithm that logs steps
- Process user input safely
- Create a GUI using Gradio
- Display algorithm steps dynamically
- Handle invalid inputs
- Produce screenshots for documentation

---

## 2️⃣ Pattern Recognition
Linear Search follows a common algorithm pattern:
- Loop through list
- Compare items one-by-one
- Stop only when target is found or list ends
- Keep track of each comparison

---

## 3️⃣ Abstraction
To simplify the program:
- The search logic is isolated inside `linear_search()`
- UI processing is handled in `run_search()`
- The user does not see internal data structures — only results

---

## 4️⃣ Algorithm Design

### **Linear Search Steps:**
1. Begin at index 0  
2. Compare list[i] with target  
3. If equal → return index  
4. Else move to next index  
5. If end reached → return “not found”

---

# 🔄 Flowchart


# 🧪 Edge Case Testing

| Case | Input | Expected Result |
|------|--------|----------------|
| Empty list | `""` | Error message |
| Not found | `1 2 3`, target `5` | “Not found” |
| Found first index | `5 4 3 2`, target `5` | index `0` |
| Found last index | `1 2 9`, target `9` | index `2` |
| Negative numbers | `-1 -3 5`, target `-3` | index `1` |

# Screenshots:
<img width="1912" height="893" alt="image" src="https://github.com/user-attachments/assets/899f6851-a487-4e00-aad1-66ca43092a8a" />


