// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"

	"github.com/microcosm-cc/bluemonday"
)

func BenchmarkTest00249(w http.ResponseWriter, r *http.Request) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	data := fmt.Sprintf("%s", dbValue)
	processed := bluemonday.UGCPolicy().Sanitize(data)
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
