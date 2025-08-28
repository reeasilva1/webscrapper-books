import pandas as pd

def save_to_csv(data: list[dict], filename: str):
    """Salva os dados em um CSV."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8")
