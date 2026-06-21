# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest05813(request):
    user_id = request.GET.get('id', '')
    data = default_blank(user_id)
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
