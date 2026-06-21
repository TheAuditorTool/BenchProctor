# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26195(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
