// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00173(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	var data string
	for _, token := range strings.Split(cookieValue, ",") {
		data = token
	}
	sessionCookie := &http.Cookie{Name: "session", Value: data, Path: "/", HttpOnly: true, SameSite: http.SameSiteStrictMode}
	w.Header().Add("Set-Cookie", sessionCookie.String())
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
