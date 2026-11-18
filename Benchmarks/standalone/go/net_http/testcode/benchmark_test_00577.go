// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net"
	"net/http"
	"net/url"
	"regexp"
	"strings"
)

func BenchmarkTest00577(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(userID)
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
