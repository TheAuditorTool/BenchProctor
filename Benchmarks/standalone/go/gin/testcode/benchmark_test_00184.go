// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"html/template"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00184(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	data := func(v string) string { return strings.TrimSpace(v) }(refererValue)
	c.Header("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(c.Writer, "<p>Results for %s</p>", template.HTMLEscapeString(data))
}
