import facebook


FB_APP_ID = '161370024354090'
FB_SECRET = '96f4d8e91f54e8df0c18b6afb03c2f67'
FB_ACCESS_TOKEN = 'EAACSwZBL6oSoBAPCs0SIkJBe3t6HVJ406yqptk8xCpHxXCUpIjSFEoaDajiSA3OgH80p7vA3GkmROZAc70Bos60G1MJRfzwm' \
                  'Sk3OUTRmP6IsJ7JWBXt2Aq7CQJ0hql8LGHBzAqhfjqSmU5biyAI9DOlynXMtoZD'
FB_PAGE_ID = '1228860087206181'


def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])

    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
    graph = facebook.GraphAPI(page_access_token)

    return graph

if __name__ == "__main__":

    config = {
        "page_id": FB_PAGE_ID,
        "access_token": FB_ACCESS_TOKEN
    }

    api = get_api(config)

    msg = "Picture, world!"

    attachment = {"name": "Link name",
                  "link": "https://www.example.com/",
                  "caption": "{*actor*} posted a new review",
                  "description": "This is a longer description of the attachment",
                  "picture": "https://pp.vk.me/c637416/v637416095/7e339/PzAQHheRIvk.jpg"}

    # status = api.put_wall_post(msg, attachment)
