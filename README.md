# 📘 Automated Book Publication Workflow – Internship Assignment

## 👩‍💻 Submitted by: Sakshi Tomar

This project demonstrates an AI-driven workflow for scraping, rewriting, and finalizing book content from a web source.

---

## 🔧 Features

1. **Web Scraping & Screenshot**  
   - Uses Playwright to fetch content from:
     https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1

2. **AI Writing & Reviewing**  
   - Rewrites scraped content using GPT-based LLM.
   - Then reviews and edits it via another AI step.

3. **Human-in-the-Loop**  
   - Allows user to manually edit final version.

---

## 📂 Files Included

- `scraping_and_screenshot.py` – Scrapes chapter and saves screenshot/text
- `ai_spin_review.py` – AI Writer & Reviewer
- `human_input.py` – Human review and editing
- `chapter1.txt`, `final_output.txt`, `final_version.txt` – Output files
- `README.md` – This file

---

## 📹 Demo Video

👉 [Click here to watch the demo video](https://your-video-link.com)

---

## 📌 Notes

- Developed using Python
- Playwright and OpenAI used as tools
- Simplified version; RL search and ChromaDB not included (optional part)