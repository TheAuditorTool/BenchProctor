# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def compact_profile(request):
    preface = request.META.get('HTTP_ORIGIN', '')
    bulletin = f'{preface!s}'
    parsed = json.loads(bulletin)
    return JsonResponse({'parsed': str(parsed)}, status=200)
