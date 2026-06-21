# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest61832(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return JsonResponse({"saved": True})
