// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00152(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	data := strings.Join(strings.FieldsFunc(rawBody, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	htmlOut := "<div>" + data + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
