from instapy import InstaPy

session = InstaPy()

session.login()

session.set_upper_follower_count(limit=2500)

# session.like_by_tags(['dog', 'cat', 'animal', 'animals'], amount=100)
# session.set_do_comment(True, percentage=100)
# session.set_comments(['So cute!', 'Haha. So cute!', 'So lovely!'])
# session.set_do_follow(enabled=True, percentage=10, times=2)

session.set_do_comment(True, percentage=50)
session.set_do_follow(enabled=True, percentage=25, times=1)
session.set_comments(['Great post!', 'Awesome!', 'Love it!', 'Awesome view!', 'Wish to be there!'])
session.like_by_tags(['programming', 'nodejs', 'reactjs', 'angular', 'jquery', 'webdevelopment', 'landscape', 'traveling', 'travel', 'backpacking', 'city'], amount=50)

# session.clarifai_check_img_for(['nsfw'], comment=True, comments=['So hot!', 'Wow. So hot!'])
# session.clarifai_check_img_for(['cat', 'dog'], comment=True, comments=['So cute!', 'Haha. So cute!', 'So lovely!'])

session.set_use_clarifai(enabled=True)

session.end()
