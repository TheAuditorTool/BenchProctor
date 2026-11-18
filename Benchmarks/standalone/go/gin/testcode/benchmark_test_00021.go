// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"net/http"
	"net/url"

	"github.com/gin-gonic/gin"
	"github.com/yuin/goldmark"
)

func BenchmarkTest00021(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	data, _ := url.QueryUnescape(cookieValue)
	var mdBuf bytes.Buffer
	goldmark.New().Convert([]byte(data), &mdBuf)
	processed := mdBuf.String()
	htmlOut := "<div>" + processed + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
