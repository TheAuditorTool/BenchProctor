// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00278(c *gin.Context) {
	rawBytes, err := ioutil.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	xmlBody := string(rawBytes)
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(xmlBody)
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", data)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	c.JSON(http.StatusOK, map[string]string{"name": *result})
}
