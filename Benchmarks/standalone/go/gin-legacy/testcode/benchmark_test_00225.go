// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00225(c *gin.Context) {
	header, err := c.FormFile("upload")
	if err != nil {
		c.String(http.StatusBadRequest, "bad upload")
		return
	}
	uploadedName := header.Filename
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(uploadedName) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := uploadedName
	ioutil.WriteFile("/var/app/data/"+processed, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
