# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest00604(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = '%s' % (profile_value,)
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return JsonResponse({"saved": True})
