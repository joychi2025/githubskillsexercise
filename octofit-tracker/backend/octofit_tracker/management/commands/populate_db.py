from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate octofit_db with test data.'

    def handle(self, *args, **kwargs):
        # 清空現有資料
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # 建立測試用戶
        user1 = User.objects.create(username='alice', email='alice@example.com', password='password1')
        user2 = User.objects.create(username='bob', email='bob@example.com', password='password2')
        user3 = User.objects.create(username='carol', email='carol@example.com', password='password3')

        # 建立團隊
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')
        team1.members.add(user1, user2)
        team2.members.add(user3)

        # 建立活動
        Activity.objects.create(user=user1, activity_type='Running', duration=timedelta(hours=1))
        Activity.objects.create(user=user2, activity_type='Walking', duration=timedelta(minutes=45))
        Activity.objects.create(user=user3, activity_type='Cycling', duration=timedelta(hours=2))

        # 建立排行榜
        Leaderboard.objects.create(user=user1, score=120)
        Leaderboard.objects.create(user=user2, score=100)
        Leaderboard.objects.create(user=user3, score=150)

        # 建立訓練菜單
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')
        Workout.objects.create(name='Jump Rope', description='Jump rope for 10 minutes')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
