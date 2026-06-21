# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest06484(request):
    multipart_value = request.POST.get('multipart_field', '')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(multipart_value),))
    return JsonResponse({"saved": True})
