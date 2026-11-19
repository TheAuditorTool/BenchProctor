// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

typedef struct _xmlDoc *xmlDocPtr;
typedef struct _xmlXPathContext *xmlXPathContextPtr;
typedef struct _xmlXPathObject *xmlXPathObjectPtr;
#define XML_PARSE_NOENT 2
#define XML_PARSE_DTDVALID 16
#define XML_PARSE_NONET 2048
#define XML_PARSE_HUGE 524288
extern xmlDocPtr xmlReadMemory(const char *_buffer, int _size, const char *_url, const char *_encoding, int _options);
extern void xmlFreeDoc(xmlDocPtr _doc);
extern xmlXPathContextPtr xmlXPathNewContext(xmlDocPtr _doc);
extern xmlXPathObjectPtr xmlXPathEvalExpression(const unsigned char *_str, xmlXPathContextPtr _ctxt);
struct c_payload { const char *value; };

void benchmark_test_00666(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("QUERY_STRING");
    if (user_input == NULL) user_input = "";
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    xmlDocPtr _doc = xmlReadMemory(data, (int)strlen(data), "noname.xml", NULL, XML_PARSE_NOENT);
    if (_doc) xmlFreeDoc(_doc);
}
