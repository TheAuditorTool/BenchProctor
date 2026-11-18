// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
	"net/url"
)

func BenchmarkTest00528(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	data, _ := url.QueryUnescape(fieldValue)
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
