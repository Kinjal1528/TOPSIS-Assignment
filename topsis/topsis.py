import pandas as pd
import numpy as np
import os
import sys


def topsis(input_file, weights, impacts, output_file):

    if not os.path.exists(input_file):
        raise FileNotFoundError("Input file not found")

    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    elif input_file.endswith('.xlsx'):
        df = pd.read_excel(input_file)
    else:
        raise ValueError("File must be CSV or XLSX")

    if df.shape[1] < 3:
        raise ValueError("Input file must contain at least 3 columns")

    data = df.iloc[:, 1:]

    if not data.apply(lambda col: pd.to_numeric(col, errors='coerce').notna().all()).all():
        raise ValueError("Criteria columns must be numeric")


    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        raise ValueError("Weights, impacts and criteria count mismatch")

    for i in impacts:
        if i not in ['+', '-']:
            raise ValueError("Impacts must be '+' or '-'")

    norm = data / np.sqrt((data ** 2).sum())
    weighted = norm * weights

    ideal_best, ideal_worst = [], []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False, method="dense").astype(int)

    df.to_csv(output_file, index=False)


def main():
    if len(sys.argv) != 5:
        print("Usage: topsis <inputFile> <weights> <impacts> <outputFile>")
        sys.exit(1)

    try:
        topsis(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        print("Topsis analysis completed successfully.")
    except Exception as e:
        print("Error:", e)
