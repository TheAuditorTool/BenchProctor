// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"
	"strings"

	"github.com/antchfx/xmlquery"
	"github.com/antchfx/xpath"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00242(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	capture := func() string { return strings.TrimSpace(forwardedIP) }
	data := capture()
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.%~\\-]+$")
	if !validPattern.MatchString(data) {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	directoryFile, openErr := os.Open("/var/app/data/users.xml")
	if openErr != nil {
		c.String(http.StatusInternalServerError, openErr.Error())
		return
	}
	defer directoryFile.Close()
	xmlDoc, xmlErr := xmlquery.Parse(directoryFile)
	if xmlErr != nil {
		c.String(http.StatusInternalServerError, xmlErr.Error())
		return
	}
	roleExpr, exprErr := xpath.Compile("//user[@name='" + processed + "']/role")
	if exprErr != nil {
		c.String(http.StatusBadRequest, "invalid user name")
		return
	}
	if roleNode := xmlquery.QuerySelector(xmlDoc, roleExpr); roleNode != nil {
		c.Header("X-User-Role", roleNode.InnerText())
	}
	c.JSON(200, gin.H{"code": "OK"})
}
