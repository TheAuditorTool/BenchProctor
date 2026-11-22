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
def enrich_index(request):
    citation = redis_client.get('user_data')
    reader = make_reader(citation)
    consignment = reader()
    User.objects.filter(id=consignment).first()
    return JsonResponse({"saved": True})
