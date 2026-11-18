// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
)

func BenchmarkTest00460(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	form := submissionForm{payload: multipartValue}
	data := form.payload
	os.Remove("/var/app/data/" + data)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
