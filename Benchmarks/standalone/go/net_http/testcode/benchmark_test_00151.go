// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"strings"
)

func BenchmarkTest00151(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	segments := strings.Split(headerValue, ",")
	data := strings.Join(segments, " ")
	w.Header().Add("Set-Cookie", "session=" + url.QueryEscape(data) + "; Path=/; Secure; HttpOnly; SameSite=Strict")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
