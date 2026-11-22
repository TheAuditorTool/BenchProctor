// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net"
	"net/http"
	"net/url"
)

func BenchmarkTest00277(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	userID := r.URL.Query().Get("id")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(userID)
	dialURL, dialErr := url.Parse(data)
	if dialErr != nil {
		http.Error(w, "invalid url", http.StatusBadRequest)
		return
	}
	conn, err := net.Dial("tcp", net.JoinHostPort(dialURL.Hostname(), "80"))
	if err == nil {
		defer conn.Close()
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
