from instagram.client import InstagramAPI
# from InstagramAPI import InstagramAPI


access_token = "13469900807.f8a90b8.5c39b15f525e4ae3bc862cce368598f0"
client_id = "f8a90b8bea394ba4b0c1b57bfd95a763"
client_secret = "7556070071fb4d43ace6f58ed6dd9d8f"

api = InstagramAPI(client_id=client_id, client_secret=client_secret, access_token=access_token)
popular_media = api.tag_recent_media('PRIDE')
for media in popular_media:
    print(media.images['standard_resolution'].url)