
from django.core.management.base import BaseCommand
from pymongo import MongoClient
from bson.objectid import ObjectId

class Command(BaseCommand):
    help = 'Populate octofit_db with test data using pymongo.'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Users
        users = [
            {"_id": ObjectId(), "username": "alice", "email": "alice@example.com", "password": "password1"},
            {"_id": ObjectId(), "username": "bob", "email": "bob@example.com", "password": "password2"},
            {"_id": ObjectId(), "username": "carol", "email": "carol@example.com", "password": "password3"},
        ]
        db.users.insert_many(users)

        # Teams
        teams = [
            {"_id": ObjectId(), "name": "Team Alpha", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Team Beta", "members": [users[2]["_id"]]},
        ]
        db.teams.insert_many(teams)


        # Activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Running", "duration": 3600},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Walking", "duration": 2700},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Cycling", "duration": 7200},
        ]
        db.activity.insert_many(activities)

        # Leaderboard (修正: 確保插入三筆資料)
        leaderboard = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 120},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[2]["_id"], "score": 150},
        ]
        if leaderboard:
            db.leaderboard.insert_many(leaderboard)

        # Workouts (修正: 確保插入三筆資料)
        workouts = [
            {"_id": ObjectId(), "name": "Pushups", "description": "Do 20 pushups"},
            {"_id": ObjectId(), "name": "Situps", "description": "Do 30 situps"},
            {"_id": ObjectId(), "name": "Jump Rope", "description": "Jump rope for 10 minutes"},
        ]
        if workouts:
            db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully using pymongo.'))
