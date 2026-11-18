// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
)

func BenchmarkTest00444(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	sum := sha256.Sum256([]byte(authHeader))
	hashStr := fmt.Sprintf("%x", sum)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
