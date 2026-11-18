# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


@csrf_exempt
def render_receipt(request):
    transcript = request.META.get('HTTP_USER_AGENT', '')
    requests.get(str(transcript))
    return JsonResponse({"saved": True})
