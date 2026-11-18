// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
)

func BenchmarkTest00091(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	var data string
	if len(fieldValue) > 0 {
		data = fieldValue
	} else {
		data = "default"
	}
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
