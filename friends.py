from instapy import InstaPy

session = InstaPy()

session.login()

session.like_from_image(url='www.instagram.com', amount=100)

session.end()
