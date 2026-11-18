// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"os"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00201(c *gin.Context) {
	pathValue := c.Param("id")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", pathValue)
	data := relayBuilder.String()
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	os.WriteFile("/var/app/data/"+processed, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
