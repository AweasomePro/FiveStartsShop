from rest_framework import views

from rest_framework.response import Response

from zhongtong.http import requset


class PriceViewSet(views.APIView):

    def get(self, request, format=None):
        # serializer = SnippetSerializer(data=request.data)

        s = requset.postPriceAndHourInterface("湖北", "荆州市", "浙江", "金华市")

        return Response(data=s)
