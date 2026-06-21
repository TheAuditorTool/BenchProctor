# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest34466(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = to_text(auth_header)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
