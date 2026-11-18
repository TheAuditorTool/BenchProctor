// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00045(w http.ResponseWriter, r *http.Request) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(commentText)
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
