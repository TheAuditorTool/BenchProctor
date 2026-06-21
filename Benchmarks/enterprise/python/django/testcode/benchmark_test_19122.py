# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest19122(request):
    multipart_value = request.POST.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
