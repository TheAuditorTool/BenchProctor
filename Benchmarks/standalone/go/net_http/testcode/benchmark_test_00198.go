// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00198(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	capture := func() string { return strings.TrimSpace(authHeader) }
	data := capture()
	sessionCookie := &http.Cookie{Name: "session", Value: data, Path: "/", HttpOnly: true, SameSite: http.SameSiteStrictMode}
	w.Header().Add("Set-Cookie", sessionCookie.String())
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
