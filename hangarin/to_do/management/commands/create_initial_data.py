from django.core.management.base import BaseCommand
from faker import Faker
from to_do.models import Task, SubTask, Note, Priority, Category
from django.utils import timezone

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_tasks(15)
        self.create_subtasks(15)
        self.create_notes(15)

    def create_tasks(self, count):
        fake = Faker()
        for _ in range(count):
            Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                priority=Priority.objects.order_by('?').first(),
                category=Category.objects.order_by('?').first(),
                deadline=timezone.make_aware(fake.date_time_this_month())
            )
        self.stdout.write(self.style.SUCCESS('Initial data for task created successfully.'))

    def create_subtasks(self, count):
        fake = Faker()
        for _ in range(count):
            SubTask.objects.create(
                title=fake.sentence(nb_words=5),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                task=Task.objects.order_by('?').first()
            )
        self.stdout.write(self.style.SUCCESS('Initial data for subtask created successfully.'))

    def create_notes(self, count):
        fake = Faker()
        for _ in range(count):
            Note.objects.create(
                content=fake.paragraph(nb_sentences=5),
                task=Task.objects.order_by('?').first()
            )
        self.stdout.write(self.style.SUCCESS('Notes created successfully.'))