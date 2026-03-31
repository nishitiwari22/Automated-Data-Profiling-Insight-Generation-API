import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_correlation_heatmap(df):
    os.makedirs("data", exist_ok=True)

    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")

    file_path = "data/heatmap.png"
    plt.savefig(file_path)
    plt.close()

    return file_path