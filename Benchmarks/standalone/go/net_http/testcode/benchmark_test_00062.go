// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
)

func BenchmarkTest00062(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	var data string
	if cookieValue != "" {
		data = cookieValue
	}
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
