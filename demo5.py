# @Author : huzejun
# @Time : 2025/3/28 21:32
import csv


def find_code(csv_file_path, district_name) -> str:
    """
    根据区域或者城市的名字，返回该区域的编码
    :param csv_file_path:
    :param district_name:
    :return:
    """
    district_map = {}
    with open(csv_file_path, mode='r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            district_id = row['district_id'].strip()
            district = row['district'].strip()
            if district not in district_map:
                district_map[district] = district_id

    return district_map.get(district_name, None)


if __name__ == '__main__':
    print(find_code('weather_district_id.csv', '洞口'))
