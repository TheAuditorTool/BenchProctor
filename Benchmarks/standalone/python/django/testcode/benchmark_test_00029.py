# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pydantic import Field, ValidationError, create_model


def BenchmarkTest00029(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = str(origin_value).split(',')
    data = ' '.join(parts)
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.\\-]+$")))(value=str(data))
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    request.session.update({'data': str(processed)})
    return JsonResponse({"saved": True})
