from django.shortcuts import render

posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Navid",
        "data": date(2021, 7, 12),
        "title": "Mountain Hiking",
        "excerpt": "Theres nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!"
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
        "slug": "rest-in-the-maldives",
        "image": "maldives.jpg",
        "author": "Navid",
        "data": date(2021, 6, 23),
        "title": "Have a rest in Maldives",
        "excerpt": "Theres nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!"
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
        "slug": "running-on-the-sands",
        "image": "maldives.jpg",
        "author": "Navid",
        "data": date(2021, 8, 10),
        "title": "Running on the sands",
        "excerpt": "Theres nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!"
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

# Create your views here.

def index(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")