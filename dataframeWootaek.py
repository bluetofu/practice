import json

#json -> dict

def json_to_df(filename):
    json_file = json.loads(open(filename, 'rb'))
    json_file_df = DataFrame(json_file, columns=['username'])

    return json_file_df

print(json_to_df('../../dataset.json'))
