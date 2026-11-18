// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"

	"github.com/gin-gonic/gin"
	"github.com/yuin/goldmark"
)

func BenchmarkTest00038(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	var data string
	if authHeader != "" {
		data = authHeader
	}
	var mdBuf bytes.Buffer
	goldmark.New().Convert([]byte(data), &mdBuf)
	processed := mdBuf.String()
	htmlOut := "<div>" + processed + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
