// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00585(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	var data string
	if len(fieldValue) > 0 {
		data = fieldValue
	} else {
		data = "default"
	}
	http.Redirect(w, r, data, http.StatusFound)
}
