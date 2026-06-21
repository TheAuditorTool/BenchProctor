# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest03818(request):
    user_id = request.GET.get('id', '')
    data = to_text(user_id)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
