# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest25172(request):
    upload_name = request.FILES['upload'].name
    data = upload_name if upload_name else 'default'
    if request.session.get('role') != 'admin':
        return JsonResponse({'error': 'forbidden'}, status=403)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
