import os
import json
import logging
from django.core.management.base import BaseCommand, CommandError
from userReview.models import Product, User, Review
# from django.conf import settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


class Command(BaseCommand):
    media_path = "/vagrant/reviewSystem/userReview"

    def add_arguments(self, parser):
        parser.add_argument('--name', help="file name run benchmark on.")

    def handle(self, *args, **options):
        try:
            file_name = None
            if options['name']:
                file_name = options['name']
            file_path = os.path.join(Command.media_path, "userReview", "media", file_name)
            self.load_file(file_path=file_path)
        except Exception as e:
            import traceback
            traceback.print_exc()
            raise CommandError(e)

    @staticmethod
    def load_file(file_path):
        with open(file_path, 'r', encoding="iso-8859-1") as f:
            try:
                while True:
                    entities = dict()
                    count = 8
                    while count >= 0:
                        line = f.readline()
                        logger.info(line)
                        if line != "\n":
                            data = line.strip().split(':')
                            entities[data[0]] = data[1]
                        count -= 1
                    logger.info("Entity: "+json.dumps(entities))
                    product_id = entities["product/productId"].strip()
                    product, created = Product.objects.get_or_create(
                        defaults={"productId": product_id},
                        productId=product_id)
                    logger.info("CREATED: "+str(created))
                    user_id = entities["review/userId"].strip()
                    user_profile = entities["review/profileName"].strip()
                    user, created = User.objects.get_or_create(
                        defaults={"userId": user_id, "profileName": user_profile},
                        userId=user_id,
                    )
                    logger.info("CREATED: "+str(created))
                    review = Review.objects.create(
                        productId=product,
                        userId=user,
                        helpfulness=entities["review/helpfulness"].strip(),
                        score=entities["review/score"].strip(),
                        time=entities["review/time"].strip(),
                        summary=entities["review/summary"].strip(),
                        text=entities["review/text"].strip()
                    )
                    logger.info("Review: "+str(review)+" Entered")
            except Exception as e:
                logger.error(e)



