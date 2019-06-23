import time
from jikanpy import Jikan
jikan = Jikan()

ITERATE = 5


class UserData:

    def __init__(self, id, score):
        self.id = id
        self.score = score


class AnimeData:

    def __init__(self, title, id, url, score, scored_by, rank, popularity, genres):
        self.title = title
        self.id = id
        self.url = url
        self.score = score
        self.scored_by = scored_by
        self.rank = rank
        self.popularity = popularity
        self.genres = genres


def get_user_data(animelist):
    """
    Returns a list. Each item in the list is UserData.
    """
    user_data_lst = []

    for i in range(ITERATE):
        anime = animelist[i]
        temp = UserData(anime["mal_id"], anime["score"])
        user_data_lst.append(temp)

    return user_data_lst


def get_anime_data(user_data_lst):
    """
    Returns a list. Each item in the list is AnimeData.
    """
    anime_data_list = []

    for i in range(ITERATE):
        time.sleep(2)
        anime = jikan.anime(user_data_lst[i].id)
        temp = AnimeData(anime["title"], anime["mal_id"], anime["url"], anime["score"], anime["scored_by"],
                         anime["rank"], anime["popularity"], anime["genres"])
        anime_data_list.append(temp)

    return anime_data_list


def get_recommendations(user):
    """

    """
    animelist = jikan.user(username=user, request="animelist")["anime"]

    user_data_lst = get_user_data(animelist)
    anime_data_lst = get_anime_data(user_data_lst)

    return anime_data_lst


if __name__ == "__main__":
    get_recommendations("God_Of_Play")
