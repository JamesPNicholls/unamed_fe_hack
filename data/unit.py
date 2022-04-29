import json
class Cunit:
    def __init__(self, unit_id) -> None:
          
        return
    def get_data():
        with open('data/stat.json', 'r') as f:
            data = json.load(f)
        
        print(data)
        return

    def store_data():
        return


with open('data/stats.json', 'r') as f:
    data = json.load(f)

print(data['unit_stats'][0]['bases'][1])
