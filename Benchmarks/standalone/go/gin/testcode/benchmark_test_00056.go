// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/url"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00056(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	c.Writer.Header().Add("Set-Cookie", "session=" + url.QueryEscape(graphqlVar) + "; Path=/; HttpOnly; SameSite=Strict")
	c.JSON(200, gin.H{"code": "OK"})
}
