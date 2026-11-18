# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


@csrf_exempt
def verify_checkpoint(request):
    phrase = request.body.decode('utf-8')
    persona = ' '.join(str(phrase).split())
    requests.get(str(persona))
    return JsonResponse({"saved": True})
