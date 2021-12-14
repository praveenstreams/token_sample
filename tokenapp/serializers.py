from rest_framework import serializers

from django.contrib.auth.models import User

class userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email')

class userregisterserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email','password')


    def create(self, validated_data):
        user=User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
        return user



class alldata(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class deletedata(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id']

