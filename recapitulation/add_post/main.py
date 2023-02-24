def addPost(list_name, post_title, post_body):
    
    post = dict([
        ('title', post_title),
        ('body', post_body)
    ])
    
    list_name.append(post)


posts = [
  {
  "title": "About the importance of functional programming",
  "body": "Functional programming is ....." 
  },
  {
  "title": "OOP programming brings classes and objects into the code",
  "body": "OOP is  ....." 
  },
]

addPost(posts, 'title', 'content')

print(posts)