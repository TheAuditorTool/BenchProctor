// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
)

func BenchmarkTest00564(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	data := fmt.Sprintf("%s", authHeader)
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
