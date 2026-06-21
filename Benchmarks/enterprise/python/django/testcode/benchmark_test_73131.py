# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest73131(request):
    multipart_value = request.POST.get('multipart_field', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(multipart_value),))
    return JsonResponse({"saved": True})
