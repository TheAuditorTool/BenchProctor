// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"html"
	"html/template"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00273(c *gin.Context) {
	fieldValue := c.PostForm("field")
	data := strings.Join(strings.FieldsFunc(fieldValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	processed := html.EscapeString(data)
	bioTmpl := template.Must(template.New("bio").Parse(`<section class="bio">{{.}}</section>`))
	var bioPage bytes.Buffer
	if err := bioTmpl.Execute(&bioPage, template.HTML(processed)); err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.Data(200, "text/html", bioPage.Bytes())
}
