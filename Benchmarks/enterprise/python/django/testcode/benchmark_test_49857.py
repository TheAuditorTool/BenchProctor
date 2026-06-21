# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49857(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
