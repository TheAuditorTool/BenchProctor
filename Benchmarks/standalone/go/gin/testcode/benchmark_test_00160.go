// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00160(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	data := strings.Join(strings.FieldsFunc(multipartValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
