// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"fmt"
	"strings"

	"github.com/gin-gonic/gin"
	"github.com/yuin/goldmark"
)

func BenchmarkTest00298(c *gin.Context) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", commentText)
	data := relayBuilder.String()
	var mdBuf bytes.Buffer
	goldmark.New().Convert([]byte(data), &mdBuf)
	processed := mdBuf.String()
	htmlOut := "<div>" + processed + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
