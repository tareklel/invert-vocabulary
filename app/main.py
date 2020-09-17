import pandas as pd
from app.invert import Invert
import sys
import os


def run_cycle(csv: str, col: str):
    """
    insert csv and col to be inverted
    :param csv: string of csv file
    :param col: series name
    :return: inverse table
    """
    df = pd.read_csv(csv, encoding='latin1')
    series = df[col].astype("str")

    print("stemming series")
    series = series.apply(lambda x: Invert.stem_list(x))

    print("getting unique terms")
    final_series = Invert.terms_series(series)

    print("creating inverted dataframe")
    df = Invert.create_inverse(final_series, series)
    # split csv path to head and tail, if head exists path will be added
    head, tail = os.path.split(csv)
    if head:
        head = f'{head}/'
    inversefile = f'{head}inverse_{tail}'
    df.to_csv(inversefile, index= False)
    print(f'inverse file stored in {inversefile}')

    return df


if __name__ == "__main__":
    run_cycle(sys.argv[1], sys.argv[2])




