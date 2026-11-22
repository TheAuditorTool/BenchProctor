// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha512"
	"encoding/hex"
	"fmt"
	"io"
	"net/http"
)

func BenchmarkTest00116(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	data := fmt.Sprintf("%s", cookieValue)
	digest := sha512.New()
	io.WriteString(digest, data)
	hashStr := hex.EncodeToString(digest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
