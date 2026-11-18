// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
)

func BenchmarkTest00049(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(multipartValue)
	os.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
