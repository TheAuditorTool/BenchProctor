// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
)

func BenchmarkTest00326(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	data := fmt.Sprintf("%s", authHeader)
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
