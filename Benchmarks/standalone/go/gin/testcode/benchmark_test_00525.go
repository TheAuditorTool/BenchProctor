// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00525(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	var data string
	for _, token := range strings.Split(graphqlVar, ",") {
		data = token
	}
	os.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
