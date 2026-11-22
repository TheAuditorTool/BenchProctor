# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def validate_snapshot(request):
    wording = request.FILES['upload'].name
    handshake, _sep, _rest = str(wording).partition('\x00')
    parsed = json.JSONDecoder().decode(str(handshake))
    return JsonResponse({'parsed': str(parsed)}, status=200)
