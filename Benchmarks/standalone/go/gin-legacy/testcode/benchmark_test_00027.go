// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strconv"

	"github.com/antchfx/xmlquery"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00027(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(uaValue)
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
	userNodes, queryErr := xmlquery.QueryAll(xmlDoc, "//user[@name='"+data+"']")
	if queryErr != nil {
		c.String(http.StatusBadRequest, "invalid user name")
		return
	}
	c.Header("X-User-Matches", strconv.Itoa(len(userNodes)))
	c.JSON(200, gin.H{"code": "OK"})
}
