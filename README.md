# 🌱 AI Fertilizer Recommendation using Endee

## 📌 Project Overview
This project is a simple AI-based fertilizer recommendation system. It demonstrates semantic search by suggesting the best fertilizer based on crop and soil type.

The system takes user input (crop and soil) and returns the most relevant fertilizer using similarity matching.

---

## 🎯 Objective
To build a basic AI application using the concept of vector databases like Endee for semantic search and recommendation.

---

## ⚙️ System Design

### 🧩 Components:
1. **Dataset**
   - Contains crop, soil, and fertilizer information
   - Stored in a text file (`data.txt`)

2. **Processing Layer**
   - User input is processed and split into words
   - Compared with dataset entries

3. **Search Logic**
   - Matching score is calculated based on similarity
   - Best match or closest match is returned

4. **Output**
   - Displays recommended fertilizer

---

## 🧠 Use of Endee

:contentReference[oaicite:0]{index=0} is a vector database used for semantic search.

In this project:
- Endee repository was forked and used as the base
- The concept of vector-based similarity search is demonstrated
- A simplified implementation is used due to time constraints

This shows how data can be stored and retrieved based on meaning rather than exact matches.

---

## 🚀 Features

- Semantic search (based on similarity)
- Handles unknown inputs
- Provides closest match suggestions
- Uses both structured and natural language data

---

## 📂 Dataset

The dataset includes:
- Crop name
- Soil type
- Fertilizer recommendation

Example:
