from pathlib import Path 
import base64
import io
import pandas as pd
import json

def parse_content(content, filename):
    
    filename = Path(filename)
    print(filename)
    
    if not filename.suffix in [".feather", ".csv"]:
        return "Invalid filetype - please upload, .csv or .feather file."
    
    _, content_string = content.split(',')
    decoded_content = base64.b64decode(content_string)
    
    try:
        if '.csv' in filename.suffix:
            data = pd.read_csv(io.StringIO(decoded_content.decode('utf-8')))
            
        elif '.feather' in filename.suffix:
            data = pd.read_feather(io.BytesIO(decoded_content))
            
    except Exception as e:
        print(e)
        return 'There was an error processing this file.'

    return data


def json_to_df(data):
    data = json.loads(data)
    return pd.DataFrame(data=data['data'], index=data['index'], columns=data['columns'])