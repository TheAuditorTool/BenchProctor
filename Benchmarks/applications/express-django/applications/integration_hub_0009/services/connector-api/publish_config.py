# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def publish_config(request):
    heading = request.FILES['upload'].name
    handshake, _sep, _rest = str(heading).partition('\x00')
    parsed = json.JSONDecoder().decode(str(handshake))
    return JsonResponse({'parsed': str(parsed)}, status=200)
