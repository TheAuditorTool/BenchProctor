// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00007(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", uaValue)
	data := relayBuilder.String()
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: data, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
