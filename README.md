### Unchained | a Blogging platform

#### Installation And Running Instructions
```
Pre-installation you will need to set up Social Media Keys as follows:

- set up an app on developers.facebook. Get your app & secret key. Set redirect url to http://localhost:8000
- set up an app with Google API. Get your app & secret key. Set your redirect url to: http://localhost:8000/complete/google-oauth2/  
        -- Ensure you ENABLE both the api for Gmail API and Google+ API from their list of all APIs.
- Save your Facebook & Google keys as environment variables in your bash profile:
export SOCIAL_AUTH_FACEBOOK_KEY=""
export SOCIAL_AUTH_FACEBOOK_SECRET=""
export SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=""
export SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=""

Activate your python environment then CD into the blog directory:
(your_environment)$ pip install -r requirements.txt
(your_environment)$ python manage.py migrate
(your_environment)$ python manage.py runserver
visit http://localhost:8000 in your preferred browser (unless thats IE then do yourself a favour and download Chrome or Firefox)
 ```
#### Using the Site

On visiting the web page you'll be greeted by a big green banner with a menu button on the right side.
Hover over it and choose your preferred log in, Facebook, Google+ or good old fashioned email sign up.

![alt tag](http://i67.tinypic.com/s2e5x1.png)

You'll probably want to make a blog post, right?
Easy.
Once your logged in hover back over that same menu button and hit the new post link.
You'll be taken away to a wonderful page where you can write down all your thoughts
and concerns about this awful world we live in. You can even add an Image.
And did I mention Emojis? Oh yes. Emojis as well.
Go wild, let out all you angst then when you are ready hit the publish post button and It will be saved and posted on the site.
If you aren't ready, well don't worry! Save it as a draft and come back later. Nobody will be able to see your half-written posts but you.  

![alt tag](http://i67.tinypic.com/2jalv60.png)

Once uploaded you can share your posts and even your profile on social media using the links.
If you see a post you like you can leave comments, and don't worry, if you make a post that has unpleasant comments you can remove them yourself.
If you visit your profile page (The same drop down menu as before) you'll be able to view all your own posts. Want to add a profile pic. No problem, go to the edit profile link in the same drop down menu you can add a profile pic, a short bio and where you currently live.

![alt tag](http://i64.tinypic.com/1op3bo.png)

#### Tech Stuff
Built with love by:
```
 * Glenn Bemont
 * James Steel
 * Jennifer Hanratty
 * Liam Taylor
 * Stevie Winston-Gore
 * Irene Oppo
```



#### User Stories
```
As a user
So that I can talk to the world
I would like to be able to post some text.
```
```
As a user
So that I can have all my posts in the one place
I would like to have a blogging account.
```
```
As a user
So that it is easier to sign up
I would like to be able to use my social media accounts to sign up or log in.
```
```
As a blogger
So that I can connect to other bloggers
I would like to be able to post comments on other blogs.
```
```
As a user
So that I can connect to other people
I would like to be able to share blog posts to other people.
```
```
As a user
So that I can connect to other
I would like to 'recommend' or 'like' other people's posts.
```
```
As a blogger
So that I can edit my text
I would like to be able to edit my blog posts.
```
```
As a blogger
So that I can maintain my blog
I would like to be able to delete blog posts.
```
```
As a blogger
So that I can maintain my blog
I would like to be able save a draft of my post before I decide to post.
```
```
As a user
So that my page looks more interesting
I would like to be able to post images to my posts.
```
```
As a user
So that my page looks pretty cool
I would like to be able to post emojis to my page.
```
```
As a user
So that I have a lot of fun
I would like to be able to post emojis as comments on other posts.
```
```
As a user
So that I can promote my blog
I would like to be able to have a profile associated with my account.
```
