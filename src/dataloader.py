import pandas as pd
import os
from .variables import DATA_FOLDER

def load_data(filename) -> pd.DataFrame:
    
    return pd.read_feather(os.path.join(DATA_FOLDER, filename))
    
    