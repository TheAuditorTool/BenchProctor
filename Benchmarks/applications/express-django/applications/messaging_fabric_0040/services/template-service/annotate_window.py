# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def annotate_window(request, path_param):
    preface = request.path.split('/')[-1]
    reader = make_reader(preface)
    bulletin = reader()
    db.execute("SELECT * FROM users WHERE id = '" + str(bulletin) + "'")
    return JsonResponse({"saved": True})
