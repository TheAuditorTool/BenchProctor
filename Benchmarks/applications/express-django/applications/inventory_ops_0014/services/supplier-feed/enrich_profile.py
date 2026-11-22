# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def enrich_profile(request):
    excerpt = request.FILES['upload'].name
    restock, _sep, _rest = str(excerpt).partition('\x00')
    parsed = json.JSONDecoder().decode(str(restock))
    return JsonResponse({'parsed': str(parsed)}, status=200)
