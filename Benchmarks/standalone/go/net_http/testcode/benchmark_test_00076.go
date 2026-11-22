// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00076(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	capture := func() string { return strings.TrimSpace(multipartValue) }
	data := capture()
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	w.Header().Set("X-Wrapped", strconv.Itoa(int(wrapped)))
}
