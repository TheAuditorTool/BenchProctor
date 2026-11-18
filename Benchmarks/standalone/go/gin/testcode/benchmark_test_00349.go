// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"regexp"
	"strings"

	"github.com/antchfx/xmlquery"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00349(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", refererValue)
	data := relayBuilder.String()
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		c.String(http.StatusInternalServerError, xmlErr.Error())
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+processed+"']")
	c.JSON(200, gin.H{"code": "OK"})
}
