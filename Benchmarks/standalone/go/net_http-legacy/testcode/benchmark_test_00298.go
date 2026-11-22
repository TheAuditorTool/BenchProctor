// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00298(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	fieldValue := r.FormValue("field")
	data := strings.ReplaceAll(fieldValue, "\x00", "")
	w.Header().Set("Location", data)
	w.WriteHeader(http.StatusSeeOther)
}
