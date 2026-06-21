# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest04304(request):
    user_id = request.GET.get('id', '')
    data = to_text(user_id)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return JsonResponse({"saved": True})
