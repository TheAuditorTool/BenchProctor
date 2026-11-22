# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def collect_checkpoint(request):
    preface = request.META.get('HTTP_ORIGIN', '')
    grievance = f'{preface!s}'
    parsed = json.loads(grievance)
    return JsonResponse({'parsed': str(parsed)}, status=200)
