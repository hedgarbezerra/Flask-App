from instagram.client import InstagramAPI

access_token = "125914ad349c44da94e174de0d34e3da"
client_secret = "3e3e0f9493714fffac9e730254796cf3"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)

api2 = InstagramAPI(client_id='	6b9e76139be2402bab6d3a7ced76d6ac', client_secret='3e3e0f9493714fffac9e730254796cf3')

if __name__ == '__main__':

    popular_media = api2.media_popular(count=20)
    for media in popular_media:
        print(media.images['standard_resolution'].url)