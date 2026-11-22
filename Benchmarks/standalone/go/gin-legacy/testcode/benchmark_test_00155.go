// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"html/template"
	"net/http"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00155(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	segments := strings.Split(headerValue, ",")
	data := strings.Join(segments, " ")
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	bioTmpl := template.Must(template.New("bio").Parse(`<section class="bio">{{.}}</section>`))
	var bioPage bytes.Buffer
	if err := bioTmpl.Execute(&bioPage, template.HTML(processed)); err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.Data(200, "text/html", bioPage.Bytes())
}
