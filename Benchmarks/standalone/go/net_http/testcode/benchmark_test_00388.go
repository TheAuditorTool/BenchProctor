// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"regexp"
	"strings"
)

func BenchmarkTest00388(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	data := dbValue
	if _, after, ok := strings.Cut(dbValue, ","); ok {
		data = after
	}
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		http.Error(w, "forbidden host", http.StatusForbidden)
		return
	}
	targetUrl := data
	http.Redirect(w, r, targetUrl, http.StatusFound)
}
