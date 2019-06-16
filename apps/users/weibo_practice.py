def get_url():

    weibo_url = "https://api.weibo.com/oauth2/authorize"
    redirect_uri = "http://192.168.27.53:8000/weibo"

    auth_url = weibo_url+"?client_id={client_id}&redirect_uri={redirect_uri}".format(client_id=2080090311, redirect_uri=redirect_uri)
    return auth_url


if __name__ == "__main__":
    print(get_url())