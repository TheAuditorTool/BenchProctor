# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def publish_promotion(request):
    notice = request.FILES['upload'].name
    reader = make_reader(notice)
    backorder = reader()
    requests.get(str(backorder))
    return JsonResponse({"saved": True})
