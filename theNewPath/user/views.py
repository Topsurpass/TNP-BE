from rest_framework import viewsets
from .models import  User
from .serializers import  UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreateView(viewsets.ModelViewSet):
    """Api view for listing, creating and modifying a user."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LogoutView(APIView):
    """Api view for logging out a user."""	
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get("refresh")
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({"detail": "Successfully logged out."}, status=200)
            except Exception as e:
                return Response({"detail": str(e)}, status=400)
        return Response({"detail": "No refresh token found in the request."}, status=400)
    