from django.core.management.base import BaseCommand, CommandError
from news.models import Category, Post


class Command(BaseCommand):
    help = 'Delete posts with selected category'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no ')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = Category.objects.get(name_of_category=options['category'])
            Post.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {category.name_of_category}'))
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category {options["category"]}'))
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find post with category {category.name_of_category}'))
