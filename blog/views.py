from datetime import date
from unittest import load_tests
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Navid",
        "date": date(2021, 7, 12),
        "title": "Mountain Hiking",
        "excerpt":"Theres nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content":"""
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum in fuga quo sunt neque, 
            minima fugiat provident, doloremque rerum debitis autem saepe aliquid minus sequi, 
            reiciendis iste vero quod nesciunt?
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum in fuga quo sunt neque, 
            minima fugiat provident, doloremque rerum debitis autem saepe aliquid minus sequi, 
            reiciendis iste vero quod nesciunt?
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum in fuga quo sunt neque, 
            minima fugiat provident, doloremque rerum debitis autem saepe aliquid minus sequi, 
            reiciendis iste vero quod nesciunt?
        """
    },
    {
        "slug": "visiting-the-maldives",
        "image": "maldives.jpg",
        "author": "Navid",
        "date": date(2021, 6, 23),
        "title": "Malidives is perfect!",
        "excerpt": "If its not the paradise so where is it!?",
        "content":"""
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum in fuga quo sunt neque, 
            minima fugiat provident, doloremque rerum debitis autem saepe aliquid minus sequi, 
            reiciendis iste vero quod nesciunt?
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum in fuga quo sunt neque, 
            minima fugiat provident, doloremque rerum debitis autem saepe aliquid minus sequi, 
            reiciendis iste vero quod nesciunt?
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum in fuga quo sunt neque, 
            minima fugiat provident, doloremque rerum debitis autem saepe aliquid minus sequi, 
            reiciendis iste vero quod nesciunt?
        """
    },
    {
        "slug": "going-to-the-beach",
        "image": "sands.jpg",
        "author": "Navid",
        "date": date(2021, 8, 10),
        "title": "Going to the beach!",
        "excerpt": "Running on hot sands is an amazing feeling that you can't have with a bitch!",
        "content":"""
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum in fuga quo sunt neque, 
            minima fugiat provident, doloremque rerum debitis autem saepe aliquid minus sequi, 
            reiciendis iste vero quod nesciunt?
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum in fuga quo sunt neque, 
            minima fugiat provident, doloremque rerum debitis autem saepe aliquid minus sequi, 
            reiciendis iste vero quod nesciunt?
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorum in fuga quo sunt neque, 
            minima fugiat provident, doloremque rerum debitis autem saepe aliquid minus sequi, 
            reiciendis iste vero quod nesciunt?
        """
    }
]

def get_key(post):
    return post['date']

# Create your views here.

def index(request):
    sorted_post = sorted(all_posts, key=get_key)
    latest_posts = sorted_post[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    selected_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": selected_post
    })