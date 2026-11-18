# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from marshmallow import Schema, fields, validate, ValidationError
from app_runtime import db


def BenchmarkTest00580(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = str(comment_value).replace('\x00', '')
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
