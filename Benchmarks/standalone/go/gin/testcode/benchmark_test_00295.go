// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00295(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	relayPrefix := ""
	if len(multipartValue) > 0 {
		relayPrefix = strings.ToLower(multipartValue[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = multipartValue
	case "f":
		data = multipartValue
	default:
		data = multipartValue
	}
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		c.String(http.StatusInternalServerError, xmlErr.Error())
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+data+"']")
	c.JSON(200, gin.H{"code": "OK"})
}
