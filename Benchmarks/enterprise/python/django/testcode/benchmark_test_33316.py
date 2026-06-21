# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33316(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    if request.session.get('role') != 'admin':
        return JsonResponse({'error': 'forbidden'}, status=403)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
