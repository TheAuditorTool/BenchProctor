// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
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
typedef struct ldap LDAP; typedef struct ldapmsg LDAPMessage;
extern "C" int ldap_initialize(LDAP **, const char *);
extern "C" int ldap_search_ext_s(LDAP *, const char *, int, const char *, char **, int, void *, void *, void *, int, LDAPMessage **);
extern "C" int ldap_msgfree(LDAPMessage *);
extern "C" int ldap_unbind_ext_s(LDAP *, void *, void *);
enum { LDAP_SCOPE_SUBTREE = 2 };
struct berval { unsigned long bv_len; char *bv_val; };
extern "C" int ldap_compare_ext_s(LDAP *, const char *, const char *, struct berval *, void *, void *);
enum { LDAP_COMPARE_TRUE = 6 };
static std::string cpp_own(const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); }

void benchmark_test_00274(const httplib::Request &req, httplib::Response &res)
{
    std::string user_input = req.path_params.at("id");
    std::string data = cpp_own(user_input);
    std::string arg = std::regex_match(data, std::regex("^(admin|user|guest|service)$")) ? data : std::string("admin");
    LDAP *_ld = nullptr;
    const char *_ldap_url = std::getenv("LDAP_URL");
    ldap_initialize(&_ld, _ldap_url ? _ldap_url : "ldap://directory:1389");
    std::string _dn = std::string("uid=") + arg + ",ou=people,dc=example,dc=com";
    struct berval _role = { 5, const_cast<char *>("admin") };
    int _rc = ldap_compare_ext_s(_ld, _dn.c_str(), "employeeType", &_role, nullptr, nullptr);
    std::cout << (_rc == LDAP_COMPARE_TRUE ? "admin" : "user") << std::endl;
    ldap_unbind_ext_s(_ld, nullptr, nullptr);
    res.set_content("ok", "text/plain");
}
