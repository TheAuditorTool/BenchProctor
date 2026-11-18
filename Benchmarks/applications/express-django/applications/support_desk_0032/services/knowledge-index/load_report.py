# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


@csrf_exempt
def load_report(request):
    note = request.META.get('HTTP_USER_AGENT', '')
    requests.get(str(note))
    return JsonResponse({"saved": True})
