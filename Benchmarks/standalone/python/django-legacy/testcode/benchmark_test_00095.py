# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pydantic import Field, ValidationError, create_model


def BenchmarkTest00095(request):
    user_id = request.GET.get('id', '')
    pending = list(str(user_id).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        create_model('_InputModel', value=(str, Field(regex="^[a-zA-Z0-9 _.\\-]+$")))(value=str(data))
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
