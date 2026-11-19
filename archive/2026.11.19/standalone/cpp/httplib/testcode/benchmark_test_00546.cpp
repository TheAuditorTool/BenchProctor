// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <regex>
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

void benchmark_test_00546(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("Authorization");
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    static const std::regex _schema("^[a-zA-Z0-9 _.%~\\-]+$");
    if (!std::regex_match(data, _schema)) { res.status = 400; res.set_content("bad request", "text/plain"); return; }
    std::string safe = data;
    std::string _xsrc = "<users><user name=\"admin\" role=\"root\"/></users>";
    xmlDocPtr _xdoc = xmlReadMemory(_xsrc.c_str(), (int)_xsrc.size(), "users.xml", nullptr, XML_PARSE_NONET);
    xmlXPathContextPtr _xctx = xmlXPathNewContext(_xdoc);
    std::string _xexpr = std::string("/users/user[@name='") + safe + "']";
    xmlXPathObjectPtr _xobj = xmlXPathEvalExpression(reinterpret_cast<const unsigned char *>(_xexpr.c_str()), _xctx);
    if (_xobj) xmlXPathFreeObject(_xobj);
    xmlXPathFreeContext(_xctx);
    xmlFreeDoc(_xdoc);
    res.set_content("ok", "text/plain");
}
