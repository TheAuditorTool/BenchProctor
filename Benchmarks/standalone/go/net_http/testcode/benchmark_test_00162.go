// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"
)

func BenchmarkTest00162(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	data := strings.Join(strings.FieldsFunc(fieldValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	os.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
