# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07779(request):
    multipart_value = request.POST.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
