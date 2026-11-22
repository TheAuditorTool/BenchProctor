// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00072(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	relayPrefix := ""
	if len(rawBody) > 0 {
		relayPrefix = strings.ToLower(rawBody[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = rawBody
	case "f":
		data = rawBody
	default:
		data = rawBody
	}
	sessionCookie := &http.Cookie{Name: "session", Value: data, Path: "/", Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode}
	w.Header().Add("Set-Cookie", sessionCookie.String())
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
