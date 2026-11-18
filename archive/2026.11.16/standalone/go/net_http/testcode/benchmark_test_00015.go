// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"html"
	"net/http"
	"strings"
)

func BenchmarkTest00015(w http.ResponseWriter, r *http.Request) {
	pathValue := strings.TrimPrefix(r.URL.Path, "/api/")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", pathValue)
	data := relayBuilder.String()
	processed := html.EscapeString(data)
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
