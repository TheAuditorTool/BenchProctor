# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def audit_membership(request):
    paragraph = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    wording = normalize(paragraph)
    parsed = json.loads(wording)
    return JsonResponse({'parsed': str(parsed)}, status=200)
