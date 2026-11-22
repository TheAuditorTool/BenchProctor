// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"html/template"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00150(c *gin.Context) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := c.ShouldBindJSON(&reqBody); err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	jsonValue := reqBody.Payload
	data := strings.Join(strings.FieldsFunc(jsonValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	tmpl, _ := template.New("view").Parse("{{.}}")
	var buf bytes.Buffer
	tmpl.Execute(&buf, data)
	c.Data(200, "text/html", buf.Bytes())
}
