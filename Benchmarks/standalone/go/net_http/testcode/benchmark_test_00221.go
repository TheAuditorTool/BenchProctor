// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/microcosm-cc/bluemonday"
)

func BenchmarkTest00221(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(fieldValue)
	processed := bluemonday.UGCPolicy().Sanitize(data)
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
