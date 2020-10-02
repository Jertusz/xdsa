from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SubProductSerializer(ProductSerializer):
    class Meta:
        model = Product
        exclude = ['quantity']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def create(self, validated_data):
        user = super(RegisterUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.groups.add(1)
        user.save()
        return user


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = SubProductSerializer(read_only=True)
    total = serializers.SerializerMethodField('total_price')

    class Meta:
        model = Order
        fields = '__all__'

    def total_price(self, obj):
        return obj.product_quantity * obj.product.price


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['product', 'product_quantity']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['status'] = 'Pending'
        validated_data['user'] = user
        return super(CreateOrderSerializer, self).create(validated_data)

    def validate_product_quantity(self, product_quantity):
        product_id = self.initial_data['product']
        quantity_in_orders = Order.objects.filter(product=product_id)
        quantity_in_orders = sum([x.product_quantity for x in quantity_in_orders])
        total_quantity = Product.objects.get(id=product_id).quantity
        if quantity_in_orders + product_quantity > total_quantity:
            raise serializers.ValidationError('Order quantity exceeds avaliable quantity')
        return product_quantity


class ModifyOrderSerializer(serializers.ModelSerializer):
    product = SubProductSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    quantity = serializers.CharField(source='order.product_quantity', read_only=True)
    class Meta:
        model = Order
        fields = ['product', 'user', 'quantity', 'status']

