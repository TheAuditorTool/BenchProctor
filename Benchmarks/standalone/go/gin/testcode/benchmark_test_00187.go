// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"fmt"

	"github.com/gin-gonic/gin"
	mdparser "github.com/yuin/goldmark/v2/parser"
	mdhtml "github.com/yuin/goldmark/v2/renderer/html"
)

func BenchmarkTest00187(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	var data string
	if uaValue != "" {
		data = uaValue
	}
	var mdBuf bytes.Buffer
	mdSource := []byte(data)
	_ = mdhtml.New().Render(&mdBuf, mdSource, mdparser.New().Parse(mdSource))
	processed := mdBuf.String()
	c.Header("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(c.Writer, "<p>Results for %s</p>", processed)
}
