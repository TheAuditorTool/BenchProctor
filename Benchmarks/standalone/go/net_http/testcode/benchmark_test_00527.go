// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00527(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	form := submissionForm{payload: multipartValue}
	data := form.payload
	http.Redirect(w, r, data, http.StatusFound)
}
