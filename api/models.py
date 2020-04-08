from django.db import models
from jsonfield import JSONField
# Create your models here.
class Weekday(models.Model):
    day = models.TextField()

class Product(models.Model):
    name = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField()
    filename = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Campaign(models.Model):
    url = models.TextField()
    campaign_id = models.TextField()
    auto_fb_post_mode = models.TextField()
    current_amount = models.IntegerField()
    goal = models.TextField()
    donators = models.TextField()
    days_active = models.IntegerField()
    title = models.TextField()
    description = models.TextField()
    has_beneficiary = models.TextField()
    user_first_name = models.TextField()
    user_last_name = models.TextField()
    currencyCode = models.TextField()
    visible_in_search = models.TextField()
    campaign_hearts = models.TextField()
    social_share_total = models.TextField()
    DescriptionLength = models.IntegerField()
    weekday = models.ForeignKey(Weekday, on_delete=models.PROTECT)
    time_of_day = models.DateTimeField()
    is_charity = models.textField
