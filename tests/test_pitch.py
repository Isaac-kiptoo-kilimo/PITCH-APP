from app.models import Pitch,User
from app import db

def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_review = Pitch(pitch_id=12345,pitch_title='Review for movies',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review='This movie is the best thing since sliced bread',user = self.user_James )

def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_id,12345)
        self.assertEquals(self.new_pitch.pitch_title,'Review for movies')
        



