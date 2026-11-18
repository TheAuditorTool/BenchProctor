// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"strings"

	"github.com/gin-gonic/gin"
	"github.com/yuin/goldmark"
)

func BenchmarkTest00190(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	data := func(v string) string { return strings.TrimSpace(v) }(uaValue)
	var mdBuf bytes.Buffer
	goldmark.New().Convert([]byte(data), &mdBuf)
	processed := mdBuf.String()
	htmlOut := "<div>" + processed + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
