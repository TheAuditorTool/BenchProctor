// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"html/template"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
	mdparser "github.com/yuin/goldmark/v2/parser"
	mdhtml "github.com/yuin/goldmark/v2/renderer/html"
)

func BenchmarkTest00297(c *gin.Context) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	capture := func() string { return strings.TrimSpace(commentText) }
	data := capture()
	var mdBuf bytes.Buffer
	mdSource := []byte(data)
	_ = mdhtml.New().Render(&mdBuf, mdSource, mdparser.New().Parse(mdSource))
	processed := mdBuf.String()
	bioTmpl := template.Must(template.New("bio").Parse(`<section class="bio">{{.}}</section>`))
	var bioPage bytes.Buffer
	if err := bioTmpl.Execute(&bioPage, template.HTML(processed)); err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	c.Data(200, "text/html", bioPage.Bytes())
}
