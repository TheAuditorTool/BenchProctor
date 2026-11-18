// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00093(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", authHeader)
	data := relayBuilder.String()
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
