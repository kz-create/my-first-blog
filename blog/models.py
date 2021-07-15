from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# DBにどのようなデータを入れるのか（モデル）を定義するファイル

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.title

    # PostのURLは後ろにPKが入るため、URLが投稿後まで決まっていない
    # そのため、reverseを使用し、キーワードにプライマリーキーを設定することで自動的にリダイレクトしてくれる
    # kwargsは何が入るかまだ決まっていない時に使う
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})