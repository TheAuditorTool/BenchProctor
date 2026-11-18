// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00562(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	http.SetCookie(w, &http.Cookie{Name: "session", Value: uaValue, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
