# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pydantic import Field, ValidationError, create_model


def BenchmarkTest00223(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.\\-]+$")))(value=str(data))
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
