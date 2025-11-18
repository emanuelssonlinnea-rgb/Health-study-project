import pandas as pd

REQUIRED = ["id","age","sex","height","weight","systolic_bp","cholesterol","smoker","disease"]

def load_data(path: str) -> pd.DataFrame:
    """
    Läser CSV 
    """
    df = pd.read_csv(path)
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return df

df = load_data("C:/Users/Mauro/Desktop/Del 1/Health-study-project/health_study_dataset.csv")


def coerce_numeric(df: pd.DataFrame) -> pd.DataFrame: #ensuring data is correctly classed, following "Mini-EDA med Python från Joakim"
    """
    Ensures numerical columns are numerical category
    """
    out = df.copy()
    for c in {"id","age","height","weight","systolic_bp","cholesterol", "disease"}:
        out[c] = pd.to_numeric(out[c], errors="coerce")
    return out



df = df.dropna(subset=["id","age","sex","height","weight","systolic_bp","cholesterol","smoker","disease"]).copy()

