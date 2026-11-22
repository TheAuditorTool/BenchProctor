// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00180(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	relayPrefix := ""
	if len(originValue) > 0 {
		relayPrefix = strings.ToLower(originValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = originValue
	case "f":
		data = originValue
	default:
		data = originValue
	}
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
