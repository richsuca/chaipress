# Script generates sample post data for 1000 posts at 30 day intervals
# Purpose: Find out how long it would take to generate website 
#          if there are a large no. of posts. That is, do we need to cache?

import random 
import datetime
alpha_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\
             01234567890.,":;\''
title_set = "abcdefghijklmnopqrstuvwxyz '"
post_dir = './post-sample/'
next_date = datetime.datetime.now()
add_days = datetime.timedelta(days=30)
post_pre = 'p-'

def title():
    return ''.join(random.choice(title_set) for _ in range(30))

def text():
    return ''.join(random.choice(alpha_set) for _ in range(5000))

for i in range(1000):
    post_name = post_pre + str(i)
    post_file = post_dir + post_name + '.md'
    with open(post_file, encoding='utf-8', mode='w') as p:
        p.write("title: " + title() + '\n')
        p.write("name: " + post_name + '\n')
        p.write("date: " + next_date.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        p.write("text:\n" + text() + '\n')
    next_date = next_date + add_days


# Stats from MacBook Air
# Generates 1000 posts @ 5000 characters per post
# in 8.5 seconds
# Total file size for posts: 7.8M

# Generates website for 1000 posts in 3 seconds
# website file size: 29M