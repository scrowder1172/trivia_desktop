import requests


class QuestionData:

    def __init__(self, question_count: int = 10):
        """
        Build class to retrieve questions
        :param question_count: int
        """
        self.question_count = question_count
        self.get_question_data()

    def get_question_data(self):
        """
        Query opentdb.com for list of questions
        :return:
        """
        api_parameters = {
            "amount": self.question_count,
            "type": "boolean"
        }

        opentdb_url = "https://opentdb.com/api.php"
        response = requests.get(url=opentdb_url, params=api_parameters)

        # raise error if return code is not 200
        response.raise_for_status()

        data = response.json()
        return data['results']

