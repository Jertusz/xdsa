from rest_framework import mixins, generics, permissions, status
from rest_framework.response import Response

from api.models import *
from api.serializers import *
from api.permissions import *


# Create your views here.
class ProductList(generics.ListAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaff]


class ProductCreate(generics.CreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaff]


class ProductModify(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaff]


class OrderList(generics.ListAPIView):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [StaffReadOnly]


class UserOrderList(generics.ListAPIView):
    
    permission_classes = [permissions.IsAuthenticated]


    def list(self, request, pk):
        try:
            queryset = self.get_queryset()
        except Order.DoesNotExist:
            return Response(None)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user)
        return queryset


class OrderDetail(generics.RetrieveAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [StaffOrUserReadOnly]


class OrderCreate(generics.CreateAPIView):

    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrUser]


class OrderModify(generics.RetrieveUpdateAPIView):

    queryset = Order.objects.all()
    serializer_class = ModifyOrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaff]


class UserList(generics.ListAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class UserDetail(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdminOrUser)


class UserRegister(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_class = (IsNotUserAdminStaff, )


class AdminModifyUser(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class UserModifyUser(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
