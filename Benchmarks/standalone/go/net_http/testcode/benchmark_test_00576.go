// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00576(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	data := strings.ReplaceAll(uaValue, "\x00", "")
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
