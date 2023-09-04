from django.db import models


# define the URL model and methode which will update the count field
class Url(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    long_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=7)
    count = models.IntegerField(default=0)

    def track(self):
        self.count += 1
        self.save()
        return self.count
