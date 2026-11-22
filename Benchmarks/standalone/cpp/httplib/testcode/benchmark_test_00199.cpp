// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unordered_map>

namespace httplib {
struct Request {
    std::string get_param_value(const std::string &key) const;
    std::string get_header_value(const std::string &key) const;
    std::unordered_map<std::string, std::string> path_params;
    std::string body;
};
struct Response {
    void set_content(const std::string &s, const std::string &type);
    void set_header(const std::string &key, const std::string &val);
    void set_redirect(const std::string &url, int status);
    int status;
};
struct Result {};
struct Client {
    Client(const std::string &host, int port);
    Result Post(const std::string &path, const std::string &body, const std::string &content_type);
};
}
typedef struct _xmlDoc xmlDoc; typedef xmlDoc *xmlDocPtr;
typedef struct _xmlXPathContext xmlXPathContext; typedef xmlXPathContext *xmlXPathContextPtr;
typedef struct _xmlXPathObject xmlXPathObject; typedef xmlXPathObject *xmlXPathObjectPtr;
extern "C" xmlDocPtr xmlReadMemory(const char *, int, const char *, const char *, int);
extern "C" void xmlFreeDoc(xmlDocPtr);
extern "C" xmlXPathContextPtr xmlXPathNewContext(xmlDocPtr);
extern "C" xmlXPathObjectPtr xmlXPathEvalExpression(const unsigned char *, xmlXPathContextPtr);
extern "C" void xmlXPathFreeObject(xmlXPathObjectPtr);
extern "C" void xmlXPathFreeContext(xmlXPathContextPtr);
enum { XML_PARSE_NOENT = 2, XML_PARSE_DTDLOAD = 4, XML_PARSE_DTDVALID = 16, XML_PARSE_NONET = 2048, XML_PARSE_HUGE = 524288 };
typedef struct _xmlTextReader xmlTextReader; typedef xmlTextReader *xmlTextReaderPtr;
extern "C" xmlTextReaderPtr xmlReaderForMemory(const char *, int, const char *, const char *, int);
extern "C" int xmlTextReaderRead(xmlTextReaderPtr);
extern "C" const unsigned char *xmlTextReaderConstValue(xmlTextReaderPtr);
extern "C" void xmlFreeTextReader(xmlTextReaderPtr);

void benchmark_test_00199(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.body;
    std::string data;
    if (!user_input.empty()) data = user_input;
    std::string _xdoc = data;
    xmlTextReaderPtr _xr = xmlReaderForMemory(_xdoc.c_str(), (int)_xdoc.size(), "payload.xml", nullptr, XML_PARSE_NOENT | XML_PARSE_DTDLOAD);
    if (_xr) {
        while (xmlTextReaderRead(_xr) == 1) {
            const unsigned char *_xv = xmlTextReaderConstValue(_xr);
            if (_xv) std::cout << reinterpret_cast<const char *>(_xv);
        }
        xmlFreeTextReader(_xr);
    }
    res.set_content("ok", "text/plain");
}
