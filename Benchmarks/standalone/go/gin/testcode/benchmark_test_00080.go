// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
	"github.com/yuin/goldmark"
)

func BenchmarkTest00080(c *gin.Context) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := c.ShouldBindJSON(&reqBody); err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	jsonValue := reqBody.Payload
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", jsonValue)
	data := relayBuilder.String()
	var mdBuf bytes.Buffer
	goldmark.New().Convert([]byte(data), &mdBuf)
	processed := mdBuf.String()
	htmlOut := "<div>" + processed + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
