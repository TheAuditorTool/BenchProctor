// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00180(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	data := func(v string) string { return strings.TrimSpace(v) }(refererValue)
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
