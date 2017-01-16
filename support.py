def get_list_formmated(leaderboard_list):
    """

    :param leaderboard_list:
    :return:
    """
    post = '[Ranking da Semana]\n\n'
    text = '{}) {} - Pontos: {}\n'
    for i, users in enumerate(leaderboard_list):
        post += text.format(i + 1, users['username'], users['points'])
    return post
