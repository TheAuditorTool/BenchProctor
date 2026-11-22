// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"html"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00241(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	capture := func() string { return strings.TrimSpace(refererValue) }
	data := capture()
	processed := html.EscapeString(data)
	c.Header("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(c.Writer, "<p>Results for %s</p>", processed)
}
