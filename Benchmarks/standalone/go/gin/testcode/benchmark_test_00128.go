// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00128(c *gin.Context) {
	fieldValue := c.PostForm("field")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(fieldValue)
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.#~\\-]+$")
	if !validPattern.MatchString(data) {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	os.Remove("/var/app/data/" + processed)
	c.JSON(200, gin.H{"code": "OK"})
}
