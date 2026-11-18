#include <string>
#include <unordered_map>
#include <functional>
#include <vector>
#include <utility>
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <unistd.h>

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
struct Server {
    typedef std::function<void(const Request &, Response &)> Handler;
    void Get(const std::string &pattern, Handler handler);
    void Post(const std::string &pattern, Handler handler);
    bool listen(const std::string &host, int port);
    std::vector<std::pair<std::string, Handler>> routes_;
};

static thread_local std::unordered_map<std::string, std::string> _req_headers;
static thread_local std::string _res_body;
static thread_local std::string _res_type;
static thread_local std::string _res_location;
static thread_local std::vector<std::pair<std::string, std::string>> _res_headers;
static thread_local bool _res_body_set = false;

static const char *_httplib_reason(int code) {
    switch (code) {
        case 200: return "OK";
        case 302: return "Found";
        case 400: return "Bad Request";
        case 401: return "Unauthorized";
        case 403: return "Forbidden";
        case 404: return "Not Found";
        case 500: return "Internal Server Error";
        default:  return "OK";
    }
}

static std::string _httplib_lower(const std::string &s) {
    std::string out = s;
    for (char &c : out) if (c >= 'A' && c <= 'Z') c = (char)(c + 32);
    return out;
}

std::string Request::get_param_value(const std::string &key) const {
    auto it = path_params.find(key);
    return it == path_params.end() ? std::string() : it->second;
}

std::string Request::get_header_value(const std::string &key) const {
    auto it = _req_headers.find(_httplib_lower(key));
    return it == _req_headers.end() ? std::string() : it->second;
}

void Response::set_content(const std::string &s, const std::string &type) {
    _res_body = s;
    _res_type = type;
    _res_body_set = true;
}

void Response::set_header(const std::string &key, const std::string &val) {
    _res_headers.emplace_back(key, val);
}

void Response::set_redirect(const std::string &url, int code) {
    _res_location = url;
    status = code;
}

static thread_local std::string _client_host;
static thread_local int _client_port = 0;

Client::Client(const std::string &host, int port) {
    _client_host = host;
    _client_port = port;
}

Result Client::Post(const std::string &path, const std::string &body,
                    const std::string &content_type) {
    int cfd = socket(AF_INET, SOCK_STREAM, 0);
    if (cfd < 0) return Result{};
    struct addrinfo hints;
    std::memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    struct addrinfo *res = nullptr;
    std::string _ports = std::to_string(_client_port);
    if (getaddrinfo(_client_host.c_str(), _ports.c_str(), &hints, &res) == 0 && res) {
        if (connect(cfd, res->ai_addr, res->ai_addrlen) == 0) {
            std::string _req = std::string("POST ") + path + " HTTP/1.1\r\n"
                             + "Host: " + _client_host + "\r\n"
                             + "Content-Type: " + content_type + "\r\n"
                             + "Content-Length: " + std::to_string(body.size()) + "\r\n"
                             + "Connection: close\r\n\r\n" + body;
            ssize_t _wn = write(cfd, _req.data(), _req.size());
            (void)_wn;
        }
        freeaddrinfo(res);
    }
    close(cfd);
    return Result{};
}

void Server::Get(const std::string &pattern, Handler handler) {
    routes_.emplace_back(pattern, handler);
}

void Server::Post(const std::string &pattern, Handler handler) {
    routes_.emplace_back(pattern, handler);
}

static void _httplib_split(const std::string &s, char sep, std::vector<std::string> &out) {
    std::string cur;
    for (char c : s) {
        if (c == sep) { out.push_back(cur); cur.clear(); }
        else cur.push_back(c);
    }
    out.push_back(cur);
}

static bool _httplib_match(const std::string &pattern, const std::string &path,
                           std::unordered_map<std::string, std::string> &params) {
    std::vector<std::string> pp, tp;
    _httplib_split(pattern, '/', pp);
    _httplib_split(path, '/', tp);
    if (pp.size() != tp.size()) return false;
    for (std::size_t i = 0; i < pp.size(); ++i) {
        if (!pp[i].empty() && pp[i][0] == ':') {
            params[pp[i].substr(1)] = tp[i];
        } else if (pp[i] != tp[i]) {
            return false;
        }
    }
    return true;
}

bool Server::listen(const std::string &host, int port) {
    (void)host;
    int sfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sfd < 0) return false;
    int opt = 1;
    setsockopt(sfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
    struct sockaddr_in addr;
    std::memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = INADDR_ANY;
    addr.sin_port = htons((unsigned short)port);
    if (bind(sfd, (struct sockaddr *)&addr, sizeof(addr)) < 0) { close(sfd); return false; }
    if (::listen(sfd, 16) < 0) { close(sfd); return false; }
    for (;;) {
        int cfd = accept(sfd, nullptr, nullptr);
        if (cfd < 0) continue;
        std::string raw;
        char buf[4096];
        ssize_t n;
        while (raw.find("\r\n\r\n") == std::string::npos) {
            n = read(cfd, buf, sizeof(buf));
            if (n <= 0) break;
            raw.append(buf, (std::size_t)n);
            if (raw.size() > (1u << 20)) break;
        }
        std::string target;
        std::string::size_type sp1 = raw.find(' ');
        std::string::size_type sp2 = sp1 == std::string::npos ? sp1 : raw.find(' ', sp1 + 1);
        if (sp1 != std::string::npos && sp2 != std::string::npos)
            target = raw.substr(sp1 + 1, sp2 - sp1 - 1);
        std::string route = target, query;
        std::string::size_type q = target.find('?');
        if (q != std::string::npos) { route = target.substr(0, q); query = target.substr(q + 1); }
        Request req;
        _req_headers.clear();
        _res_body.clear();
        _res_type.clear();
        _res_location.clear();
        _res_headers.clear();
        _res_body_set = false;
        if (!query.empty()) {
            std::vector<std::string> pairs;
            _httplib_split(query, '&', pairs);
            for (const std::string &kv : pairs) {
                std::string::size_type eq = kv.find('=');
                if (eq != std::string::npos)
                    req.path_params[kv.substr(0, eq)] = kv.substr(eq + 1);
            }
        }
        std::string::size_type hend = raw.find("\r\n\r\n");
        if (hend != std::string::npos) {
            req.body = raw.substr(hend + 4);
            std::string _lh = raw.substr(0, hend);
            for (char &_c : _lh) if (_c >= 'A' && _c <= 'Z') _c = (char)(_c + 32);
            std::string::size_type _clp = _lh.find("content-length:");
            long _clen = _clp == std::string::npos ? -1 : std::strtol(raw.c_str() + _clp + 15, nullptr, 10);
            while (_clen >= 0 && (long)req.body.size() < _clen) {
                n = read(cfd, buf, sizeof(buf));
                if (n <= 0) break;
                req.body.append(buf, (std::size_t)n);
            }
        }
        if (hend != std::string::npos) {
            std::string::size_type _hs = raw.find("\r\n");
            if (_hs != std::string::npos && _hs < hend) {
                std::string _hblock = raw.substr(_hs + 2, hend - _hs - 2);
                std::vector<std::string> _hlines;
                _httplib_split(_hblock, '\n', _hlines);
                for (std::string &_hl : _hlines) {
                    while (!_hl.empty() && (_hl.back() == '\r' || _hl.back() == '\n')) _hl.pop_back();
                    std::string::size_type _hc = _hl.find(':');
                    if (_hc == std::string::npos) continue;
                    std::string::size_type _hv = _hl.find_first_not_of(" \t", _hc + 1);
                    _req_headers[_httplib_lower(_hl.substr(0, _hc))] =
                        _hv == std::string::npos ? std::string() : _hl.substr(_hv);
                }
            }
        }
        Response res;
        res.status = 200;
        bool matched = false;
        for (const auto &r : routes_) {
            std::unordered_map<std::string, std::string> params;
            if (_httplib_match(r.first, route, params)) {
                for (const auto &kv : params) req.path_params[kv.first] = kv.second;
                r.second(req, res);
                matched = true;
                break;
            }
        }
        if (!matched) res.status = 404;
        std::string body = _res_body_set ? _res_body
                                         : (res.status == 200 ? std::string("ok") : std::string("err"));
        std::string reply = std::string("HTTP/1.1 ") + std::to_string(res.status) + " "
                          + _httplib_reason(res.status) + "\r\n";
        if (_res_body_set && !_res_type.empty()) reply += "Content-Type: " + _res_type + "\r\n";
        if (!_res_location.empty()) reply += "Location: " + _res_location + "\r\n";
        for (const auto &_rh : _res_headers) reply += _rh.first + ": " + _rh.second + "\r\n";
        reply += "Content-Length: " + std::to_string(body.size()) + "\r\n";
        reply += "Connection: close\r\n\r\n" + body;
        ssize_t wn = write(cfd, reply.data(), reply.size());
        (void)wn;
        close(cfd);
    }
    close(sfd);
    return true;
}
}
