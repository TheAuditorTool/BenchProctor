# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest18931(request):
    multipart_value = request.POST.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
