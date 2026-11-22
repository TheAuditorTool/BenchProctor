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
typedef struct _xmlTextReader *xmlTextReaderPtr;
extern xmlTextReaderPtr xmlReaderForMemory(const char *_buffer, int _size, const char *_url, const char *_encoding, int _options);
extern int xmlTextReaderRead(xmlTextReaderPtr _reader);
extern const unsigned char *xmlTextReaderConstValue(xmlTextReaderPtr _reader);
extern void xmlFreeTextReader(xmlTextReaderPtr _reader);

void benchmark_test_00412(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("QUERY_STRING");
    if (user_input == NULL) user_input = "";
    const char *data = (strlen(user_input) > 0) ? user_input : "";
    xmlTextReaderPtr _reader = xmlReaderForMemory(data, (int)strlen(data), "noname.xml", NULL, XML_PARSE_NOENT);
    if (_reader != NULL) {
        while (xmlTextReaderRead(_reader) == 1) {
            const unsigned char *_text = xmlTextReaderConstValue(_reader);
            if (_text != NULL) fputs((const char *)_text, stdout);
        }
        xmlFreeTextReader(_reader);
    }
}
