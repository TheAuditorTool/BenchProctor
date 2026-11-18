// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"strings"

	"github.com/gin-gonic/gin"
	"github.com/yuin/goldmark"
)

func BenchmarkTest00489(c *gin.Context) {
	userID := c.Query("id")
	data := func(v string) string { return strings.TrimSpace(v) }(userID)
	var mdBuf bytes.Buffer
	goldmark.New().Convert([]byte(data), &mdBuf)
	processed := mdBuf.String()
	htmlOut := "<div>" + processed + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
