import json
import numpy as np
import pandas as pd

df = pd.read_csv("Final_Secret_Grades.csv")
json_out = '''
{
    "title": "All Secret Scores",
    "students": []
}
'''

json_out = json.loads(json_out)

for i, j in df.iterrows():
    student_dict = {"Secret Code": j.get(0)}
    for k in range(1, len(j.index)):
        sub_title = list(j.index)[k]
        student_dict.update({sub_title.strip("_score"): j.get(k)})
    json_out['students'].append(student_dict)

# json_out = json.dumps(json_out, indent=2)

with open('scores.json', 'w') as f:
    json.dump(json_out, f, indent=2)