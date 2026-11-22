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
typedef struct _xmlParserCtxt *xmlParserCtxtPtr;
extern xmlParserCtxtPtr xmlNewParserCtxt(void);
extern xmlDocPtr xmlCtxtReadMemory(xmlParserCtxtPtr _ctxt, const char *_buffer, int _size, const char *_url, const char *_encoding, int _options);
extern void xmlFreeParserCtxt(xmlParserCtxtPtr _ctxt);

void benchmark_test_00447(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    FILE *_src_fp = fopen("/etc/app/config", "r");
    if (_src_fp != NULL) {
        if (fgets(user_input_buf, sizeof(user_input_buf), _src_fp) == NULL) user_input_buf[0] = '\0';
        fclose(_src_fp);
    }
    const char *user_input = user_input_buf;
    char data[512];
    switch (user_input[0]) {
        case '\0':
            data[0] = '\0';
            break;
        default:
            snprintf(data, sizeof(data), "%s", user_input);
            break;
    }
    xmlParserCtxtPtr _pctx = xmlNewParserCtxt();
    if (_pctx == NULL) return;
    xmlDocPtr _doc = xmlCtxtReadMemory(_pctx, data, (int)strlen(data), "noname.xml", NULL, XML_PARSE_NONET);
    if (_doc) xmlFreeDoc(_doc);
    xmlFreeParserCtxt(_pctx);
}
