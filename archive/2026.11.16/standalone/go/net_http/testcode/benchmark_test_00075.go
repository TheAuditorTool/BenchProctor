// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net"
	"net/http"
	"net/url"
	"regexp"
	"strings"
)

func BenchmarkTest00075(w http.ResponseWriter, r *http.Request) {
	_apiResp, _apiErr := http.Get("https://api.svc.cluster/data")
	if _apiErr != nil {
		return
	}
	defer _apiResp.Body.Close()
	_apiBytes, _ := io.ReadAll(_apiResp.Body)
	apiValue := string(_apiBytes)
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(apiValue)
	parsedURL, _ := url.Parse(data)
	checkedHost := parsedURL.Hostname()
	if resolvedAddrs, lookupErr := net.LookupHost(checkedHost); lookupErr == nil && len(resolvedAddrs) > 0 {
		checkedHost = resolvedAddrs[0]
	}
	if regexp.MustCompile("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)").MatchString(checkedHost) {
		http.Error(w, "private range blocked", http.StatusForbidden)
		return
	}
	targetUrl := data
	conn, err := net.Dial("tcp", targetUrl)
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
