# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def merge_revision(request):
    note = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    byline = normalize(note)
    parsed = json.loads(byline)
    return JsonResponse({'parsed': str(parsed)}, status=200)
