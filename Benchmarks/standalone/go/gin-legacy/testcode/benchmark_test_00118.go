// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"io/ioutil"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00118(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	var parsed map[string]interface{}
	json.Unmarshal([]byte(dbValue), &parsed)
	data, _ := parsed["value"].(string)
	content, err := ioutil.ReadFile("/var/app/data/" + data)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
