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


def get_genres(genres):
    """
    Returns a list of genre ids.
    """
    ret = []
    for genre in genres:
        ret.append(genre["mal_id"])
    return ret


def recommend_recurse(id, n, page, recommendations):
    """
    Helper for recommend_wrapper.
    """

    time.sleep(2)
    animelist = jikan.top(type="anime", page=page)["top"]
    for anime in animelist:
        time.sleep(2)
        full_anime = jikan.anime(anime["mal_id"])
        if (id in get_genres(full_anime["genres"])) and not((full_anime["title"]) in recommendations):
            recommendations += full_anime["title"] + "`" + full_anime["url"] + "~"
            n -= 1
            if n == 0:
                return recommendations
    return recommend_recurse(id, n, page + 1, recommendations)


def recommend_wrapper(top_genres, n):
    """
    Returns a string.
    n is the number of anime to recommend per genre.
    """
    recommendations = ""
    for id in top_genres:
        recommendations = recommend_recurse(id, n, 1, recommendations)
    return recommendations


def algorithm(user_data_lst, anime_data_lst):
    """
    Returns a string
    """

    genre_occurrences = [0 for i in range(43)]
    for anime in anime_data_lst:
        for genre in anime.genres:
            n = genre["mal_id"] - 1
            genre_occurrences[n] += 1

    genre_id_lst = [i + 1 for i in range(43)]
    # find the 3 top genres
    top_genres = sorted(zip(genre_occurrences, genre_id_lst), reverse=True)[:3]
    top_genres_lst = []
    for i in range(len(top_genres)):
        top_genres_lst.append(top_genres[i][1])

    return recommend_wrapper(top_genres_lst, 2)


def get_recommendations(user):
    """

    """
    animelist = jikan.user(username=user, request="animelist")["anime"]

    user_data_lst = get_user_data(animelist)
    anime_data_lst = get_anime_data(user_data_lst)

    return algorithm(user_data_lst, anime_data_lst)


if __name__ == "__main__":
    print(get_recommendations("achins"))
