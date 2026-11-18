// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00584(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", uaValue)
	data := relayBuilder.String()
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
