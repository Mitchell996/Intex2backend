import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'intex2backend.settings'
import django
import json
django.setup()

# regular imports
from api.models import Weekday, Campaign

# main script
def main():
    #categories will be a dictionary
    #key: string name of category
    #value: the actual category?
    Weekdays = {}
    with open('products.json') as json_file:
        data = json.load(json_file)
    campaigns = data['campaigns']
    #fill in everything from products
    for prod in campaigns:
        dbprod = Campaign()
        #dbprod.weekday = prod['weekday']
        try: 
            dbprod.weekday = Weekday.objects.get(day=prod['weekday'])
        except Weekday.DoesNotExist:
            newCategory = Weekday()
            newCategory.day = prod['weekday']
            Weekdays[prod['weekday']] = newCategory
            newCategory.save()
            dbprod.weekday = Weekday.objects.get(day=prod['weekday'])


        #print(prod['category'])
        #print(categories[prod['category']])
        #dbprod.Category = Category.objects.get(title=prod['category'])
        dbprod.url = prod['url']
        dbprod.campaign_id = prod['campaign_id']
        dbprod.auto_fb_post_mode = prod['auto_fb_post_mode']
        dbprod.currencyCode = prod['currencycode']
        dbprod.current_amount = prod['current_amount']
        dbprod.goal = prod['goal']
        dbprod.donators = prod['donators']
        dbprod.days_active = prod['days_active']
        dbprod.title = prod['title']
        dbprod.description = prod['description']
        dbprod.DescriptionLength = len(prod["description"])
        dbprod.has_beneficiary = prod['has_beneficiary']
        dbprod.user_first_name = prod['user_first_name']
        dbprod.user_last_name = prod['user_last_name']
        dbprod.visible_in_search = prod['visible_in_search']
        dbprod.campaign_hearts = prod['campaign_hearts']
        dbprod.social_share_total = prod['social_share_total']
        dbprod.is_charity = prod['is_charity']
        dbprod.time_of_day = prod['time_of_day']
        dbprod.save()
    
        
    

# bootstrap
if __name__ == '__main__':
    main()
