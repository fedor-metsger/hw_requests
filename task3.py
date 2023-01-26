
import time
import requests

QUESTIONS_URL = "https://api.stackexchange.com/2.3/questions"

def get_questions(days: int, tag: str):
    """Метод возвращает список вопросов за последние days дней с тегом tag"""

    fromdate = str(round(time.time()) - days * 3600 * 24)
    params = {
        "fromdate": fromdate,
        "tagged": tag,
        "pagesize": 100,
        "site": "stackoverflow"
    }
    all_questions, page = [], 1
    while True:
        params["page"] = page
        print(f"Получаю страницу {page}")
        response = requests.get(QUESTIONS_URL, params=params)
        if response.status_code != 200:
            print("Ошибка, status code: " + str(response))
            return None
        items = response.json()["items"]
        has_more = response.json()["has_more"]

        # print("Список вопросов получен успешно")
        # print(f"Получено {len(items)} вопросов")
        all_questions.extend(items)
        # print(f"has_more: {has_more}")
        if not has_more:
            return all_questions
        page += 1


def main():
    questions = get_questions(days=2, tag="Python")
    if not questions: return

    for q in questions:
        print(
            time.ctime(q["creation_date"]), q["tags"], q["title"]
        )
    print(f"\nВсего получено {len(questions)} вопрос(а/ов)")

if __name__ == "__main__":
    main()