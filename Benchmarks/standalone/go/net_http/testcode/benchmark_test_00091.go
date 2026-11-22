// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
)

func BenchmarkTest00091(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	form := submissionForm{payload: multipartValue}
	data := form.payload
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	w.Header().Set("X-Wrapped", strconv.Itoa(int(wrapped)))
}
