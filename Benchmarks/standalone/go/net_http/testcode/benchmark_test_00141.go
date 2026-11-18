// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00141(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	data := originValue
	if _, after, ok := strings.Cut(originValue, ","); ok {
		data = after
	}
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
