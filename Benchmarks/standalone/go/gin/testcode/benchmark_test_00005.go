// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"html/template"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00005(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	tmpl, _ := template.New("view").Parse("{{.}}")
	var buf bytes.Buffer
	tmpl.Execute(&buf, forwardedIP)
	c.Data(200, "text/html", buf.Bytes())
}
