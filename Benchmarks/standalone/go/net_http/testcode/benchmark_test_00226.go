// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00226(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	var data string
	for _, token := range strings.Split(fieldValue, ",") {
		data = token
	}
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	w.Header().Set("X-Wrapped", strconv.Itoa(int(wrapped)))
}
