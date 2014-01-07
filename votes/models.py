from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=256)
    votes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-votes']

    def __unicode__(self):
        return '%s (%s votes)' % (self.name, self.votes)
