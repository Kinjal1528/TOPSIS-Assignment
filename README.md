# TOPSIS Python Package

This project implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method as a Python package with command-line interface support.

---

## 📌 Features
- Accepts CSV or XLSX input files
- Command-line based execution
- Validates weights, impacts, and input data
- Outputs TOPSIS score and rank for each alternative

---

## 📂 Input File Format
- First column: Alternatives (name/id)
- Remaining columns: Numeric criteria values

Example:

| Model | C1 | C2 | C3 | C4 | C5 |
|------|----|----|----|----|----|

---

## ⚙️ Installation

```bash
pip install .

## ▶️ Usage

```bash
topsis <inputFile> <weights> <impacts> <outputFile>


---

### 2️⃣

```markdown
### Example

```bash
topsis data.csv "1,1,1,1,1" "+,+,-,+,+" result.csv


---

### 3️⃣ After Example, ADD THIS

```markdown
---

## 📊 Output
The output file contains:
- Topsis Score
- Rank

---

## 🛠️ Dependencies
- Python >= 3.7
- pandas
- numpy

---

## 👤 Author
Kinjal
