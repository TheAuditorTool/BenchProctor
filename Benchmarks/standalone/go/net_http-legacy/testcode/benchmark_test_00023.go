// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00023(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	uaValue := r.Header.Get("User-Agent")
	relayPrefix := ""
	if len(uaValue) > 0 {
		relayPrefix = strings.ToLower(uaValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = uaValue
	case "f":
		data = uaValue
	default:
		data = uaValue
	}
	sessionCookie := &http.Cookie{Name: "session", Value: data, Path: "/", Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode}
	w.Header().Add("Set-Cookie", sessionCookie.String())
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
