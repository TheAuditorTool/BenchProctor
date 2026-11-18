// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
)

func BenchmarkTest00165(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	sum := sha256.Sum256([]byte(originValue))
	hashStr := fmt.Sprintf("%x", sum)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
