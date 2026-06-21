# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest02654(request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    kind = 'json' if str(profile_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = profile_value
            data = parsed
        case _:
            data = profile_value
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
