from rest_framework import serializers
from api.models import Weekday
from api.models import Campaign
# Serializers define the API representation.
class WeekdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Weekday
        fields = [ 'id', 'day' ]

class CampaignSerializer(serializers.ModelSerializer):
    weekday = WeekdaySerializer()
    class Meta:
        model = Campaign
        fields = ['id', 'campaign_id', 'auto_fb_post_mode', 'current_amount', 'goal', 'donators', 'days_active', 'title', 'description', 'has_beneficiary',
         'user_first_name', 'user_last_name', 'currencyCode', 'visible_in_search', 'campaign_hearts', 'social_share_total','DescriptionLength', 'weekday', 'time_of_day' ]


