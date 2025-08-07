from django.core.management.base import BaseCommand
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.blocking import BlockingScheduler
from tutorial.todos.models import Todo

def test_job():
    todos_object = Todo.objects.all()
    for todo_obj in todos_object:
        print("each time=========================")
        print(todo_obj.id)
        print(todo_obj.title)

    print("This is a scheduled job executing...")

class Command(BaseCommand):
    help = 'start django scheduler... '

    def handle(self, *args, **options):
        scheduler = BlockingScheduler()
        scheduler.remove_all_jobs()

        scheduler.add_job(
            test_job,
            trigger=CronTrigger(second='*/3'),
            id="test_job",
            max_instances=1,
            replace_existing=True
        )
        self.stdout.write("Added job ...")

        try:
            self.stdout.write("Start scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            self.stdout.write("Stopping scheduler...")
            scheduler.shutdown()
            self.stdout.write("Scheduler shut down successfully!")