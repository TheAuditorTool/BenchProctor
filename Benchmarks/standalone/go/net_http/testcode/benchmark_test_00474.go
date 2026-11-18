// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00474(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	capture := func() string { return strings.TrimSpace(headerValue) }
	data := capture()
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
