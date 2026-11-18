// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"encoding/hex"
	"net/http"
)

func BenchmarkTest00525(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	hexBytes, _ := hex.DecodeString(cookieValue)
	data := string(hexBytes)
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
