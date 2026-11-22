# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import redis_client
from app_runtime import User


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def annotate_receipt(request):
    tagline = redis_client.get('user_data')
    reader = make_reader(tagline)
    gauge = reader()
    User.objects.filter(id=gauge).first()
    return JsonResponse({"saved": True})
