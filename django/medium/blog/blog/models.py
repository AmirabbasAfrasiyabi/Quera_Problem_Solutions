from django.db import models, transaction


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.author})"

    def copy(self):
        """
        Make a full copy of this BlogPost and all its Comments.
        The new post will get the current datetime (auto_now_add).
        Returns the id of the newly created BlogPost.
        """
        with transaction.atomic():
            # create the new post (date_created will be set to now by auto_now_add)
            new_post = BlogPost.objects.create(
                title=self.title,
                body=self.body,
                author=self.author,
            )

            # copy comments
            for c in self.comments.all():
                Comment.objects.create(blog_post=new_post, text=c.text)

        return new_post.id


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=500)

    def __str__(self):
        return f"Comment on {self.blog_post_id}: {self.text[:30]}"
