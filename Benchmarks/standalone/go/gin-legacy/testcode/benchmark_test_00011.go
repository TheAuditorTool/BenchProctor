// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"html"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00011(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	data := func(v string) string { return strings.TrimSpace(v) }(headerValue)
	processed := html.EscapeString(data)
	c.Header("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(c.Writer, "<p>Results for %s</p>", processed)
}
