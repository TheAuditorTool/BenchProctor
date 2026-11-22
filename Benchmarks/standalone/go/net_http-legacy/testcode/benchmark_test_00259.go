// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"strings"
)

func BenchmarkTest00259(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	originValue := r.Header.Get("Origin")
	data := originValue
	if _, after, ok := strings.Cut(originValue, ","); ok {
		data = after
	}
	w.Header().Add("Set-Cookie", "session=" + url.QueryEscape(data) + "; Path=/; Secure; HttpOnly; SameSite=Strict")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
