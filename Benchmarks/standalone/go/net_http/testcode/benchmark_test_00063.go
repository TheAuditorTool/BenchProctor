// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00063(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	var data string
	for _, token := range strings.Split(originValue, ",") {
		data = token
	}
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
