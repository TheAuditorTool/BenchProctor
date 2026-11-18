// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"fmt"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00018(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	data := fmt.Sprintf("%s", graphqlVar)
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
