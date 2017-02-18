import csv


if __name__ == "__main__":

    answers = {'привет': "И тебе привет!", 'как дела': "Лучше всех", 'пока': "Увидимся"}

    with open('routes.csv', 'r', encoding='cp1251') as f:
        fields = [
                    'ID', 'Name', 'Longitude_WGS84', 'Latitude_WGS84', 'Street', 'AdmArea', 'District',
                    'RouteNumbers', 'StationName', 'Direction', 'Pavilion', 'OperatingOrgName', 'EntryState',
                    'system_object_id', 'global_id', 'geoData'
                 ]

        reader = csv.DictReader(f, fields, delimiter=';')

        list_key_routes = []
        list_value_routes = []
        for row in reader:
            list_key_routes += [row['Name']]
            list_value_routes += [len(row['RouteNumbers'].split(';'))]

        dict_routes = dict(zip(list_key_routes, list_value_routes))
        
        max_value = max(value for key, value in dict_routes.items())

        for key, value in dict_routes.items():
            if value == max_value:
                print('{} - {}'.format(key, value))
            
