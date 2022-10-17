import json

path = 'candidates.json'


def load_candidates_from_json(path='candidates.json'):
    """
    Возвращает всех кандидатов
    :param path: аргумент принимает путь к json файлу
    :return:  Функция возвращает список словарей с данными кандидатов
    """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_candidate(candidate_id):
    """
    :param candidate_id: аргумент принимает ID кандидата
    :return: возврщает словарь данных кандидата по указанному ID
    """
    candidates = load_candidates_from_json(path)

    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """
    :param candidate_name: аргумент принимает имя кандидата
    :return: возврщает cписок кандидатов по совпадению в имени
    """
    candidates = load_candidates_from_json(path)
    candidates_for_name = []
    for candidate in candidates:
        if candidate_name in candidate['name'].split():
            candidates_for_name.append(candidate)
    return candidates_for_name

def get_candidates_by_skill(skill_name):
    """
    :param skill_name: аргумент принимает навык кандидата
    :return: возврщает список данных кандидатов по указанному навыку
    """
    candidates = load_candidates_from_json(path)
    skills = []

    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            skills.append(candidate)
    return skills



