// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha256"
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00069(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	data := func(v string) string { return strings.TrimSpace(v) }(fieldValue)
	sum := sha256.Sum256([]byte(data))
	hashStr := fmt.Sprintf("%x", sum)
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
