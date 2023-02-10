# Guitar Journal for The CS50 Project
#### Video Demo:
#### Description: A self paced curriculum for aspiring guitarists

## Introduction
The guitar journal is a project meant to document my learning progress with the guitar while outlining a clear path to aspiring guitarists to becoming proficient with the guitar. The need to develop this project arises from the challenges I faced as I was learning the guitar. I continue to add to the course curriculum as I learn newer skills and gain more experience pertaining the correct way to learning the guitar.

>“The beautiful thing about learning is nobody can take it away from you.” – B B King.

## Structure
The Guitar Journal is designed to be a self paced curriculum. I got the idea from a programming course I'm taking called The Odin Project. The idea is that students teach themselves. The idea of a guided self-paced curriculum is ideal for flexibility as people aspiring to learn the guitar are of different ages, abilities, opportunities and timelines.

![This is an image of the odin project](/static/odin.png)

My guitar journal is structured in a similar style. After registering, one is redirected to the login page. After a successful log in, the content is displayed in a lesson-by-lesson structure.

![This is an image of my guitar website](static/indexpage.png)

## Resources
The Flask framework was used to develop the guitar journal. SQLite3 was used for data storage and HTML, CSS and Vanilla Javascript were used to develop the front-end of the web application.

## Timeline


## Problems encountered
1. ### Different routes for each lesson
I grappled to find a way to automate lesson retrieval by the flask app. It would be cumbersome and probably taxing on storage and speed if I declared a different route for each lesson. However in the end, since the lessons are few, I decided to declare app routes for each lesson. Will explore different method
```Python
@app.route("/lesson1", methods=["GET"])
def lesson():
    return render_template("lesson1.html")
```
2. ### Secure and ad-free web hosting
I have also not resolved the issue of where I will eventually deploy the website on. As the current traffic only consists of my two current students, I'm currently looking at free options that do not need payment.

- [Gunicorn to App Platform](https://docs.digitalocean.com/tutorials/app-deploy-flask-app/)

- [GitHub Live Pages](https://pages.github.com/)
