# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def reconcile_policy(request):
    wording = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    backorder = normalize(wording)
    parsed = json.loads(backorder)
    return JsonResponse({'parsed': str(parsed)}, status=200)
