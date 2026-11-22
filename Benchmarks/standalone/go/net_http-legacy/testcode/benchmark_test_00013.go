// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00013(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	var data string
	for _, token := range strings.Split(commentText, ",") {
		data = token
	}
	sessionCookie := &http.Cookie{Name: "session", Value: data, Path: "/", Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode}
	w.Header().Add("Set-Cookie", sessionCookie.String())
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
