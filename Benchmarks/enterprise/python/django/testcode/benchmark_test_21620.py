# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest21620(request):
    upload_name = request.FILES['upload'].name
    db.execute('DELETE FROM accounts WHERE id = ?', (str(upload_name),))
    return JsonResponse({"saved": True})
