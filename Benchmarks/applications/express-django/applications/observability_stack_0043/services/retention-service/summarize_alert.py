# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


@csrf_exempt
def summarize_alert(request):
    note = request.body.decode('utf-8')
    gauge = ' '.join(str(note).split())
    requests.get(str(gauge))
    return JsonResponse({"saved": True})
