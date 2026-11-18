// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/microcosm-cc/bluemonday"
)

func BenchmarkTest00314(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	var data string
	if len(fieldValue) > 0 {
		data = fieldValue
	} else {
		data = "default"
	}
	processed := bluemonday.UGCPolicy().Sanitize(data)
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
