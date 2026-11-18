// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00098(c *gin.Context) {
	header, err := c.FormFile("upload")
	if err != nil {
		c.String(http.StatusBadRequest, "bad upload")
		return
	}
	uploadName := header.Filename
	var data string
	if len(uploadName) > 0 {
		data = uploadName
	} else {
		data = "default"
	}
	http.SetCookie(c.Writer, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	c.JSON(200, gin.H{"code": "OK"})
}
