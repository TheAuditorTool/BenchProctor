// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00093(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	form := submissionForm{payload: graphqlVar}
	data := form.payload
	c.Set("data", data)
}
