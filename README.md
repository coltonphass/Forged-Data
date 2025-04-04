# Benford's Law Forgery Detector

This Python program analyzes numerical data files using **Benford's Law** to detect potential forgeries. It scans the leading digits of numbers in a file, compares their frequencies to the expected Benford distribution, and calculates a **forgery coefficient** to measure deviation.

---

## 🔍 Features

- Processes multiple data files automatically
- Calculates:
  - **Frequency totals** for digits 1-9
  - **Relative frequencies**
  - **Benford offset values**
  - **Forgery coefficient** (deviation from Benford's Law)
- Summarizes results in a clean and readable table
- Handles errors gracefully (invalid data, missing files)
- Ideal for educational use, statistics projects, or data validation tasks

---

## 📁 Files Analyzed

This version is set up to scan these sample files:

```
P02_DataFile_0.dat
P02_DataFile_1.dat
P02_DataFile_2.dat
P02_DataFile_3.dat
P02_DataFile_4.dat
P02_DataFile_5.dat
P02_DataFile_6.dat
P02_DataFile_7.dat
P02_DataFile_8.dat
P02_DataFile_9.dat
```

> 📌 Make sure these files are in the same directory as your Python script or adjust the file paths accordingly.

---

## ▶️ How to Run

1. Make sure you have **Python 3** installed.
2. Place your `.dat` files in the same directory.
3. Run the script:

```bash
python Forged_Data_Python.py
```

or simply run the sln in visual studio!

---

## 📊 Sample Output

![Sim Demo](./demo.gif)


## 📚 What is Benford's Law?

Benford's Law predicts that in many naturally occurring datasets, the number **1** appears as the leading digit about **30% of the time**, while larger digits appear less frequently. Major deviations from this expected pattern may suggest **manipulated or fraudulent data**.

---

## 🛠️ Functions Breakdown

- `calculateBenfordProbability(digit)` – Calculates expected frequency
- `analyzeDataFile(filePath)` – Main logic for analyzing a single file
- `main()` – Orchestrates the analysis for multiple files and prints results

---


## 🧠 Educational Use

This tool is great for:
- Learning about **data forensics**
- Practicing **Python file I/O and logic**
- Understanding **real-world applications of mathematics**

---
