from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import StudentReward, Reward

from reward.serializers import StudentRewardSerializer


STUDENTREWARD_URL = reverse('reward:studentreward-list')


def sample_reward(reward='Test Reward'):
    """Create and return a sample reward"""
    return Reward.objects.create(reward=reward)

def sample_studentreward(user, **params):
    """Create and return a sample studentreward"""
    defaults = {
        'student': user,
        'reward': sample_reward(),
        'notes': 'sample test',
    }
    defaults.update(params)

    return StudentReward.objects.create(**defaults)

def detail_url(studentreward_id):
    """Return studentacheviement detail URL"""
    return reverse('reward:studentreward', args=[studentreward_id])


class PublicStudentRewardAPITests(TestCase):
    """Test the publically available stedentreward API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        res = self.client.get(STUDENTREWARD_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateStudentRewardAPITests(TestCase):
    """Test the private studentreward API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'scott@gmail.com',
            'testpass123'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_studentreward_list(self):
        """Test retrieving a list of student rewards"""
        sample_studentreward(user=self.user)
        sample_studentreward(user=self.user)

        res = self.client.get(STUDENTREWARD_URL)

        studentrewards = StudentReward.objects.all()
        serializer = StudentRewardSerializer(studentrewards, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_view_studentreward_detail(self):
        """Testing viewing a single studentreward"""
        studentreward = sample_studentreward(user=self.user)

        url = detail_url(studentreward.id)
        res = self.client.get(url)
        serializer = StudentRewardSerializer(studentreward)

        self.assertEqual(res.data, serializer.data)