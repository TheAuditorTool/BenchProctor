# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def build_summary(request):
    summary = request.FILES['upload'].name
    phrase, _sep, _rest = str(summary).partition('\x00')
    parsed = json.JSONDecoder().decode(str(phrase))
    return JsonResponse({'parsed': str(parsed)}, status=200)
