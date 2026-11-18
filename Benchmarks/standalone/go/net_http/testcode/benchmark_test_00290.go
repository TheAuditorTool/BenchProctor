// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"
)

func BenchmarkTest00290(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", fieldValue)
	data := relayBuilder.String()
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	w.Header().Set("X-Wrapped", strconv.Itoa(int(wrapped)))
}
