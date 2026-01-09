from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
# Import models from octofit_tracker.models
from octofit_tracker.models import Team, Activity, Leaderboard, Workout
User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        print('Deleting all users, teams, activities, leaderboard, and workouts...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        print('All data deleted.')

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        print(f'Teams created: {Team.objects.all()}')

        # Create users (super heroes)
        users = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'team': marvel},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'team': marvel},
            {'username': 'batman', 'email': 'batman@dc.com', 'team': dc},
            {'username': 'superman', 'email': 'superman@dc.com', 'team': dc},
        ]
        for u in users:
            user = User.objects.create_user(username=u['username'], email=u['email'], password='password')
            print(f'User created: {user}')
            # Optionally, add team info to user profile if extended

        # Create activities
        a1 = Activity.objects.create(user='ironman', team='Marvel', type='Running', duration=30)
        a2 = Activity.objects.create(user='batman', team='DC', type='Cycling', duration=45)
        a3 = Activity.objects.create(user='superman', team='DC', type='Swimming', duration=60)
        a4 = Activity.objects.create(user='captainamerica', team='Marvel', type='Walking', duration=20)
        print(f'Activities created: {Activity.objects.all()}')

        # Create leaderboard
        l1 = Leaderboard.objects.create(team='Marvel', points=50)
        l2 = Leaderboard.objects.create(team='DC', points=60)
        print(f'Leaderboard created: {Leaderboard.objects.all()}')

        # Create workouts
        w1 = Workout.objects.create(name='Morning Cardio', description='A quick morning cardio session', difficulty='Easy')
        w2 = Workout.objects.create(name='Strength Training', description='Full body strength workout', difficulty='Hard')
        print(f'Workouts created: {Workout.objects.all()}')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
