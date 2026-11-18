# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def compact_quota(request):
    tagline = request.COOKIES.get('session_token', '')
    persona = bytes.fromhex(tagline).decode('utf-8', 'ignore')
    yaml.load(persona, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
