# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pydantic import Field, ValidationError, create_model


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00163(request):
    field_value = request.POST.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.\\-]+$")))(value=str(data))
    except ValidationError:
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
