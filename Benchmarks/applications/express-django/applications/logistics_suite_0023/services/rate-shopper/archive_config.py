# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


@csrf_exempt
def archive_config(request):
    caption = request.body.decode('utf-8')
    parcel = ' '.join(str(caption).split())
    requests.get(str(parcel))
    return JsonResponse({"saved": True})
