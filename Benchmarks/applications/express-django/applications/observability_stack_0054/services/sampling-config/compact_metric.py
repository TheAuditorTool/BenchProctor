# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def compact_metric(request):
    excerpt = request.META.get('HTTP_ORIGIN', '')
    cohort = f'{excerpt!s}'
    parsed = json.loads(cohort)
    return JsonResponse({'parsed': str(parsed)}, status=200)
