// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00387(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", refererValue)
	data := relayBuilder.String()
	http.Redirect(w, r, data, http.StatusFound)
}
