// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strconv"
	"strings"

	"github.com/antchfx/xmlquery"
	"github.com/antchfx/xpath"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00277(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	var data string
	if cookieValue != "" {
		data = cookieValue
	}
	_lower := strings.ToLower(data)
	if !strings.HasPrefix(_lower, "t") && !strings.HasPrefix(_lower, "f") && _lower != "1" && _lower != "0" {
		c.String(http.StatusBadRequest, "invalid boolean")
		return
	}
	parsedBool := strconv.FormatBool(strings.HasPrefix(_lower, "t") || _lower == "1")
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
	roleExpr, exprErr := xpath.Compile("//user[@name='" + parsedBool + "']/role")
	if exprErr != nil {
		c.String(http.StatusBadRequest, "invalid user name")
		return
	}
	if roleNode := xmlquery.QuerySelector(xmlDoc, roleExpr); roleNode != nil {
		c.Header("X-User-Role", roleNode.InnerText())
	}
	c.JSON(200, gin.H{"code": "OK"})
}
