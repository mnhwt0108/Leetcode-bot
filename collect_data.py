import json 

def get_json():
    with open("problems.json") as file:
        return json.load(file)

def parse_data(json_obj):
    alg_list = json_obj["stat_status_pairs"]
    difficulty_ref = {1: "Easy", 2: "Medium", 3: "Hard"}
    parsed_data = {}

    for alg_json in alg_list:
        alg_stat = alg_json["stat"]

        question_id = alg_stat["question_id"]
        difficulty = alg_json["difficulty"]["level"]
        title_slug = alg_stat["question__title_slug"]
        question_title = alg_stat["question__title"]
        totalSub    = alg_stat["total_submitted"]
        description = difficulty + totalSub

        parsed_data[question_id] = {
            "url": "https://leetcode.com/problems/" + title_slug, 
            "difficulty": difficulty_ref[difficulty],
            "question_title": question_title,
            "description": description
        }
    return parsed_data

def get_data():
    json_obj = get_json()
    return parse_data(json_obj)