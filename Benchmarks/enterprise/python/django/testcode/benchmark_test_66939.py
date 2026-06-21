# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest66939(request):
    upload_name = request.FILES['upload'].name
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(upload_name),))
    return JsonResponse({'secret': str(secret)}, status=200)
