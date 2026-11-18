// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net"
	"net/http"
	"net/url"
	"regexp"
)

func BenchmarkTest00195(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	parsedURL, _ := url.Parse(fieldValue)
	checkedHost := parsedURL.Hostname()
	if resolvedAddrs, lookupErr := net.LookupHost(checkedHost); lookupErr == nil && len(resolvedAddrs) > 0 {
		checkedHost = resolvedAddrs[0]
	}
	if regexp.MustCompile("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)").MatchString(checkedHost) {
		http.Error(w, "private range blocked", http.StatusForbidden)
		return
	}
	targetUrl := fieldValue
	conn, err := net.Dial("tcp", targetUrl)
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
