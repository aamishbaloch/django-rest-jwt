from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.authentication import UserAuthentication
from authentication.permission import UserAccessPermission


class HomeView(APIView):
    """
    Returns home text if the user is authenticated successfully and has permissions.

    **Example requests**:

        GET /api/home/
    """

    authentication_classes = (UserAuthentication,)
    permission_classes = (UserAccessPermission,)

    def get(self, request):
        content = {
            'message': 'Welcome {} {}'.format(request.user.first_name, request.user.last_name)
        }
        return Response(content, status=status.HTTP_200_OK)
