from django.forms import ModelForm

from instagram.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = [
            'message', 'is_public'
        ]

# form = PostForm(request.POST)
