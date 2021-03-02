import tweepy #pip install tweepy
import json


def candidatosTwitter():

    consumer_key="oU3eRnB0ENoGq124quINXdrAZ"
    consumer_secret=""
    access_token = "418197577-pXUdPpPC6NJDbmaAgQSpNRkvEMSt1xep5foYjBqk"
    access_token_secret = ""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

    data = api.get_user("CarlosHerreraSi")
    dataRM = api.get_user("raulmoronO")
    dataJM = api.get_user("Magana_DeLaMora")
    Candidatos = []

    #print(json.dumps(data._json, indent=2))
    #Carlos Herrera
    CarlosHerrera = []
    followers = str(data.followers_count)
    noFavoritos = str(data.favourites_count)
    uTweet = str(data.status.text)
    CarlosHerrera.append("2")
    CarlosHerrera.append(followers)
    CarlosHerrera.append(noFavoritos)
    CarlosHerrera.append(uTweet)

    #Raúl Morón Orozco
    RaulMoron = []
    RMfollowers = str(dataRM.followers_count)
    RMnoFavoritos = str(dataRM.favourites_count)
    RMuTweet = str(dataRM.status.text)
    RaulMoron.append("1")
    RaulMoron.append(RMfollowers)
    RaulMoron.append(RMnoFavoritos)
    RaulMoron.append(RMuTweet)

    #Juan Antonio Magaña de la Mora
    JuanMagania = []
    JMfollowers = str(dataJM.followers_count)
    JMnoFavoritos = str(dataJM.favourites_count)
    JMuTweet = str(dataJM.status.text)
    JuanMagania.append("3")
    JuanMagania.append(JMfollowers)
    JuanMagania.append(JMnoFavoritos)
    JuanMagania.append(JMuTweet)

    Candidatos.append(RaulMoron)
    Candidatos.append(CarlosHerrera)
    Candidatos.append(JuanMagania)
    print(Candidatos)
    return Candidatos

candidatosTwitter()
