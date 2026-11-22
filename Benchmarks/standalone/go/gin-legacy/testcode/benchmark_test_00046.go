// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"os"
	"regexp"

	"github.com/antchfx/xmlquery"
	"github.com/antchfx/xpath"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00046(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	data := fmt.Sprintf("%s", refererValue)
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
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
