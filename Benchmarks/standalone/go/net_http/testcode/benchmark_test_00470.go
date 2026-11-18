// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"fmt"
	"net/http"
	"strings"

	"github.com/yuin/goldmark"
)

func BenchmarkTest00470(w http.ResponseWriter, r *http.Request) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", commentText)
	data := relayBuilder.String()
	var mdBuf bytes.Buffer
	goldmark.New().Convert([]byte(data), &mdBuf)
	processed := mdBuf.String()
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
