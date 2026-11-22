// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00219(c *gin.Context) {
	_cfgBytes, _ := ioutil.ReadFile("/etc/app/config.json")
	configValue := string(_cfgBytes)
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", configValue)
	data := relayBuilder.String()
	lookupStmt, err := DB.Prepare(fmt.Sprintf(`SELECT id, name FROM "%s"`, strings.ReplaceAll(data, `"`, `""`)))
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer lookupStmt.Close()
	rows, err := lookupStmt.Query()
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
