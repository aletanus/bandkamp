from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner
from rest_framework import generics
from drf_spectacular.utils import extend_schema


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        operation_id="users_List",
        responses={200: UserSerializer},
        description="User listing route",
        summary="Summary: User listing route",
        tags=["Tag: User listing route"]
    )
    def get(self, request, *args, **kargs):
        return super().get(request, *args, **kargs)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
