// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00022(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(graphqlVar)
	c.Redirect(http.StatusFound, data)
}
