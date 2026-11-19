// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
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
typedef struct ldap LDAP; typedef struct ldapmsg LDAPMessage;
extern "C" int ldap_initialize(LDAP **, const char *);
extern "C" int ldap_search_ext_s(LDAP *, const char *, int, const char *, char **, int, void *, void *, void *, int, LDAPMessage **);
extern "C" int ldap_msgfree(LDAPMessage *);
extern "C" int ldap_unbind_ext_s(LDAP *, void *, void *);
enum { LDAP_SCOPE_SUBTREE = 2 };

void benchmark_test_00441(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.get_header_value("Referer");
    char _fmt_buf[512];
    std::snprintf(_fmt_buf, sizeof(_fmt_buf), "%s", user_input.c_str());
    std::string data = _fmt_buf;
    LDAP *_ld = nullptr;
    const char *_ldap_url = std::getenv("LDAP_URL");
    ldap_initialize(&_ld, _ldap_url ? _ldap_url : "ldap://directory:1389");
    std::string _filter = std::string("(uid=") + data + ")";
    LDAPMessage *_lres = nullptr;
    ldap_search_ext_s(_ld, "dc=example,dc=com", LDAP_SCOPE_SUBTREE, _filter.c_str(), nullptr, 0, nullptr, nullptr, nullptr, 0, &_lres);
    if (_lres) ldap_msgfree(_lres);
    ldap_unbind_ext_s(_ld, nullptr, nullptr);
    res.set_content("ok", "text/plain");
}
