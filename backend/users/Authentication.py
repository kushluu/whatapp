import jwt
from rest_framework.authentication import BaseAuthentication
from users.models import User
from .serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed


class Authentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('not user')
        try:
            payload_Data = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('not user')

        user = User.objects.filter(id=payload_Data['id']).first()
        serializer = UserSerializer(user)
        # user=serializer.data
        return (user, None)


