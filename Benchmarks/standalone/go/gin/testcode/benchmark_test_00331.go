// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00331(c *gin.Context) {
	fieldValue := c.PostForm("field")
	var data string
	if fieldValue != "" {
		data = fieldValue
	}
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.#%\\-]+$")
	if !validPattern.MatchString(data) {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	htmlOut := "<div>" + processed + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
