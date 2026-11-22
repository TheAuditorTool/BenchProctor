# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def compact_signature(request):
    footnote = request.META.get('HTTP_AUTHORIZATION', '')
    def normalize(value):
        return value.strip()
    addendum = normalize(footnote)
    parsed = json.loads(addendum)
    return JsonResponse({'parsed': str(parsed)}, status=200)
