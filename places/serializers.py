import datetime
from django.contrib.auth import get_user_model
from rest_framework import serializers
from places.models import Place, Photo, SNSType, SNSUrl
from users.models import User

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'image',
        ]

class SNSUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = SNSUrl
        fields = [
            'sns_type_url',
            'sns_url',
        ]
class PlaceSerializer(serializers.ModelSerializer):
    open_hours = serializers.SerializerMethodField()
    place_like = serializers.SerializerMethodField()
    class Meta:
        model = Place
        fields = [
            'id',
            'place_name',
            'category',
            'vegan_category',
            'tumblur_category',
            'reusable_con_category',
            'pet_category',
            'open_hours',
            'etc_hours',
            'place_review',
            'address',
            'rep_pic',
            'short_cur',
            'left_coordinate',
            'right_coordinate',
            'place_like',
            ]
    def get_open_hours(self,obj):
        '''
        오늘 요일만 보내주기 위한 함수
        '''
        days = ['mon_hours','tues_hours','wed_hours','thurs_hours','fri_hours','sat_hours','sun_hours']
        a = datetime.datetime.today().weekday()
        place = Place.objects.filter(id=obj.id).values(days[a])[0]
        return place[days[a]]

    def get_place_like(self,obj):
        '''
        장소의 좋아요 여부를 알려주기 위한 함수
        '''
        place = Place.objects.get(id=obj.id)
        re_user =  self.context['request'].user.id
        like_id = place.place_likeuser_set.all()
        users = User.objects.filter(id__in=like_id)
        if users.filter(id=re_user).exists():
            return 'ok'
        else:
            return 'none'

class PlaceDetailSerializer(serializers.ModelSerializer):
    open_hours = serializers.SerializerMethodField()
    photos = PhotoSerializer(many=True,read_only=True)
    sns = SNSUrlSerializer(many=True,read_only=True)
    class Meta:
        model = Place
        fields = [
            'id',
            'place_name',
            'category',
            'vegan_category',
            'tumblur_category',
            'reusable_con_category',
            'pet_category',
            'open_hours',
            'etc_hours',
            'mon_hours',
            'tues_hours',
            'wed_hours',
            'thurs_hours',
            'fri_hours',
            'sat_hours',
            'sun_hours',
            'place_review',
            'address',
            'rep_pic',
            'short_cur',
            'left_coordinate',
            'right_coordinate',
            'photos',
            'sns',
            ]
    def get_open_hours(self,obj):
        '''
        오늘 요일만 보내주기 위한 함수
        '''
        days = ['mon_hours','tues_hours','wed_hours','thurs_hours','fri_hours','sat_hours','sun_hours']
        a = datetime.datetime.today().weekday()
        place = Place.objects.filter(id=obj.id).values(days[a])[0]
        return place[days[a]]

