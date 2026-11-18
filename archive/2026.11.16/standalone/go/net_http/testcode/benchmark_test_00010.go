// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"regexp"
)

func BenchmarkTest00010(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(hostValue)
	parsedURL, _ := url.Parse(data)
	if !regexp.MustCompile("^(api\\.svc\\.cluster|cdn\\.gocdn\\.net)$").MatchString(parsedURL.Hostname()) {
		http.Error(w, "forbidden host", http.StatusForbidden)
		return
	}
	targetUrl := data
	http.Redirect(w, r, targetUrl, http.StatusFound)
}
