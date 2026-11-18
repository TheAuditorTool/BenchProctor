// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
)

func BenchmarkTest00072(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	data := fmt.Sprintf("%s", cookieValue)
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
