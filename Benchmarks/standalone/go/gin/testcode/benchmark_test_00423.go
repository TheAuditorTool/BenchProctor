// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00423(c *gin.Context) {
	header, err := c.FormFile("upload")
	if err != nil {
		c.String(http.StatusBadRequest, "bad upload")
		return
	}
	uploadName := header.Filename
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(uploadName)
	os.Remove("/var/app/data/" + data)
	c.JSON(200, gin.H{"code": "OK"})
}
