# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import Template, Context


def make_reader(raw):
    def read():
        return raw.strip()
    return read

@csrf_exempt
def validate_manifest(request):
    remark = request.META.get('HTTP_AUTHORIZATION', '')
    reader = make_reader(remark)
    persona = reader()
    resp = HttpResponse(content_type='text/html')
    resp.write(Template('<div>{{ value }}</div>').render(Context({'value': str(persona)})))
    return resp
