from django.db import models

class Task(models.Model):
    task = models.IntegerField(blank = True)
    description = models.CharField(max_length=200, blank = True)
    monthly_updated = models.BooleanField(default=False, blank = True)
    weekly_updated = models.BooleanField(default=False, blank = True)
    daily_updated = models.BooleanField(default=False, blank = True)

    def __str__(self):
        return self.description

class UpdateType(models.Model):
    # add only three field from admin view
    #field is Daily, Weekly, Monthly
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.duration

class TaskTracker(models.Model):
    task = models.IntegerField()
    email = models.EmailField()
    update_type = models.ForeignKey(UpdateType, on_delete=models.CASCADE)

    def __str__(self):
        return self.email