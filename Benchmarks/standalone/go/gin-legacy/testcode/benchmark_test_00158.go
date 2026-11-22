// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"

	"github.com/antchfx/xmlquery"
	"github.com/antchfx/xpath"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00158(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	capture := func() string { return strings.TrimSpace(cookieValue) }
	data := capture()
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
	roleExpr, exprErr := xpath.Compile("//user[@name='" + data + "']/role")
	if exprErr != nil {
		c.String(http.StatusBadRequest, "invalid user name")
		return
	}
	if roleNode := xmlquery.QuerySelector(xmlDoc, roleExpr); roleNode != nil {
		c.Header("X-User-Role", roleNode.InnerText())
	}
	c.JSON(200, gin.H{"code": "OK"})
}
