// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00049(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	data := fieldValue
	if _, after, ok := strings.Cut(fieldValue, ","); ok {
		data = after
	}
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
