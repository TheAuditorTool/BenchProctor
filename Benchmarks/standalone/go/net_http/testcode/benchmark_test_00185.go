// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00185(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	var data string
	for _, token := range strings.Split(fieldValue, ",") {
		data = token
	}
	w.Header().Set("Location", data)
	w.WriteHeader(http.StatusSeeOther)
}
