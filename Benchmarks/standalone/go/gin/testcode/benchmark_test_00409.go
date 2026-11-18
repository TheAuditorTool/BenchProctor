// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00409(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	var data string
	if forwardedIP != "" {
		data = forwardedIP
	}
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		c.String(http.StatusInternalServerError, xmlErr.Error())
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+data+"']")
	c.JSON(200, gin.H{"code": "OK"})
}
