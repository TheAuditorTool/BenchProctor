// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"strings"
)

func BenchmarkTest00259(w http.ResponseWriter, r *http.Request) {
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
	w.Header().Add("Set-Cookie", "session=" + url.QueryEscape(data) + "; Path=/; Secure; HttpOnly; SameSite=Strict")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
