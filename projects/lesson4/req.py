import requests

URL_NAMES = "http://api.data.mos.ru/v1/datasets/2009/rows"

def get_names(url, year=None):
    result = requests.get(URL_NAMES)

    if result.status_code == 200:
        if year:
            new_data = []
            data = result.json()
            for data_row in data:
                if year == data_row['Cells']['Year']:
                    new_data.append(data_row)

            return new_data

        else:
            return result.json()
    else:
        return print("Error")

