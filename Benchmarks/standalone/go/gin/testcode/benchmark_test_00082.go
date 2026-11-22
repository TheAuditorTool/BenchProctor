// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00082(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	relayPrefix := ""
	if len(originValue) > 0 {
		relayPrefix = strings.ToLower(originValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = originValue
	case "f":
		data = originValue
	default:
		data = originValue
	}
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
