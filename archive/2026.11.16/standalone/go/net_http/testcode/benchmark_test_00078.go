// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00078(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	capture := func() string { return strings.TrimSpace(refererValue) }
	data := capture()
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
