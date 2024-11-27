from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

from .models import Users, InfoCUBranch, InfoProduct, History
from .serializers import UsersSerializer, InfoCUBranchSerializer, InfoProductSerializer, HistorySerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class InfoCUBranchViewSet(viewsets.ModelViewSet):
    queryset = InfoCUBranch.objects.all()
    serializer_class = InfoCUBranchSerializer


class InfoProductViewSet(viewsets.ModelViewSet):
    queryset = InfoProduct.objects.all()
    serializer_class = InfoProductSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        # Get user by username
        user = Users.objects.get(TCEMAIL=email)
        # Check password
        if (password == user.TCPASSWORD):
            # Serialize user data
            user_data = {
                'id': user.id,
                'username': user.TCUSERNAME,
                'email': user.TCEMAIL,
                'gender': user.TCGENDER,
            }
            return Response({'message': 'Login successful', 'user': user_data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
    except Users.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def report(request):
    if request.method == 'GET':
        history = History.objects.filter(createdDate__date=request.GET.get('date'))
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        date_from = request.data.get('date_from')
        date_to = request.data.get('date_to')
        history = History.objects.filter(createdDate__range=[date_from, date_to])
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def filter_history(request):
    name = request.GET.get('name', '')
    code = request.GET.get('code', '')
    price = request.GET.get('price', '')

    history = History.objects.filter(
        infoProducts__itemName__icontains=name,
        infoProducts__itemCode__icontains=code,
        infoProducts__itemPrice__icontains=price
    ).distinct()

    serializer = HistorySerializer(history, many=True)
    return Response(serializer.data)
