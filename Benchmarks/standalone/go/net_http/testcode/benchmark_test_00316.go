// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/md5"
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00316(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	segments := strings.Split(fieldValue, ",")
	data := strings.Join(segments, " ")
	hash := md5.Sum([]byte(data))
	hashStr := fmt.Sprintf("%x", hash)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
