// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00130(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", multipartValue)
	data := relayBuilder.String()
	sessionCookie := &http.Cookie{Name: "session", Value: data, Path: "/", HttpOnly: true, SameSite: http.SameSiteStrictMode}
	c.Writer.Header().Add("Set-Cookie", sessionCookie.String())
	c.JSON(200, gin.H{"code": "OK"})
}
