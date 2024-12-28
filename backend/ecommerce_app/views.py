import json
import traceback
import logging
log = logging.getLogger(__name__)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from ecommerce_app.models import Product
from ecommerce_app.serializers import ProductSerializer
from ecommerce_app.services import ProductSrv

@csrf_exempt
@api_view(['GET'])
def product_listing_view(request):
    try:
        paginator = PageNumberPagination()
        paginator.page_size = 10

        products = Product.objects.all()
        page = paginator.paginate_queryset(products, request)

        if request.GET.get('category'):
            products = products.filter(category=request.GET.get('category'))

        if request.GET.get('price'):
            products = products.filter(price=request.GET.get('price'))

        if request.GET.get('ordering'):
            print('ere')
            products = products.order_by(request.GET.get('ordering'))

        serializer = ProductSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        log.error(traceback.format_exc())
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def create_product_view(request):
    try:
        data = json.loads(request.body)
        srv = ProductSrv(data)
        data, msg, code = srv.create_record()

        if code == status.HTTP_201_CREATED:
            return Response({"data": data, "response_msg": msg, "response_code": code})
        else:
            return Response({"error": msg}, status=code)
    except Exception as e:
        log.error(traceback.format_exc())
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_product_view(request, pk):
    try:
        data = json.loads(request.body)
        srv = ProductSrv(data)
        data, msg, code = srv.update_record(pk)

        if code == status.HTTP_200_OK:
            return Response({"data": data, "response_msg": msg, "response_code": code})
        else:
            return Response({"error": msg}, status=code)
    except Exception as e:
        log.error(traceback.format_exc())
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@csrf_exempt
@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_product_view(request, pk):
    try:
        srv = ProductSrv(None)
        data, msg, code = srv.delete_record(pk)

        if code == status.HTTP_204_NO_CONTENT:
            return Response({"response_msg": msg, "response_code": code})
        else:
            return Response({"error": msg}, status=code)
    except Exception as e:
        log.error(traceback.format_exc())
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        