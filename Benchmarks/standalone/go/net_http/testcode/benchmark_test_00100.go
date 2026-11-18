// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00100(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", originValue)
	data := relayBuilder.String()
	http.Redirect(w, r, data, http.StatusFound)
}
