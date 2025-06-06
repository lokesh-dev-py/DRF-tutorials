from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments import highlight
from pygments.formatters import HtmlFormatter

# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGES_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLES_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    owner = models.ForeignKey(
        "auth.User", related_name="snippets", on_delete=models.CASCADE
    )
    highlighted = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGES_CHOICES, default="python", max_length=100
    )
    style = models.CharField(choices=STYLES_CHOICES, default="friendly", max_length=100)

    def save(self, *args, **kwargs):
        """
        Use Pygments to create a highlighted HTML representation of the code
        """
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}
        formatter = HtmlFormatter(
            style=self.style, linenos=linenos, full=True, **options
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["created"]
