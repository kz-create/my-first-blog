from django.contrib import admin
from .models import Post

# admin画面に表示するアドミンユーザーのモデルを記述する

# admin画面にregisterとして"Post"を追加する
admin.site.register(Post)
