# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def format_report(request):
    caption = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    consignment = normalize(caption)
    parsed = json.loads(consignment)
    return JsonResponse({'parsed': str(parsed)}, status=200)
