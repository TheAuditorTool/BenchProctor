// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
)

func BenchmarkTest00265(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	hash := md5.Sum([]byte(uaValue))
	hashStr := fmt.Sprintf("%x", hash)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
