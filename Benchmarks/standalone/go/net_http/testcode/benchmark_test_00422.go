// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"net/http"
)

func BenchmarkTest00422(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	hexBytes, _ := hex.DecodeString(headerValue)
	data := string(hexBytes)
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
