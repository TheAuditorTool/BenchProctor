// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
)

func BenchmarkTest00066(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	var data string
	if len(authHeader) > 0 {
		data = authHeader
	} else {
		data = "default"
	}
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
