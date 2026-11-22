// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00061(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	pending := strings.Split(graphqlVar, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	os.Remove("/var/app/data/" + data)
	c.JSON(200, gin.H{"code": "OK"})
}
