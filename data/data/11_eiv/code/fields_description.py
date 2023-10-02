import os
import json
import pandas as pd

root_dit = '/files/master/energy_database/data/11_eiv/11/data'
merge_dict = {}
filename = 'fields_explanation.csv'

for subdir, dirs, files in os.walk(root_dit):
    for file in files:
        if file == 'description.json':
            file_path = os.path.join(subdir, file)
            with open(file_path) as f:
                data = json.load(f)
            merge_dict.update(data)

unique_keys = set(merge_dict.keys())
new_dict = {k:merge_dict[k] for k in unique_keys}
sorted_dict = {k: v for k,v in sorted(new_dict.items())}
field_dict = pd.DataFrame.from_dict(sorted_dict,orient = 'index')
field_dict.to_csv(f"{os.path.join(root_dit,'0_database_summary')}/{filename}",index = True)