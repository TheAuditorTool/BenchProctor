// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"html"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00558(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(cookieValue)
	processed := html.EscapeString(data)
	htmlOut := "<div>" + processed + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
