// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00135(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	sessionCookie := &http.Cookie{Name: "session", Value: uaValue, Path: "/", Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode}
	w.Header().Add("Set-Cookie", sessionCookie.String())
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
