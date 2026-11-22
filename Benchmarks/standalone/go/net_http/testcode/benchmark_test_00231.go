// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00231(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", multipartValue)
	data := relayBuilder.String()
	http.RedirectHandler(data, http.StatusFound).ServeHTTP(w, r)
}
