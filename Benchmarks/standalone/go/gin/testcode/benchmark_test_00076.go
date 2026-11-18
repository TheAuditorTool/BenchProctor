// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00076(c *gin.Context) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(c.Request.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	data := fmt.Sprintf("%s", graphqlVar)
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid integer")
		return
	}
	boundedVal := strconv.Itoa(max(0, min(_num, 2147483647)))
	requested, _ := strconv.Atoi(boundedVal)
	allocated := requested + 1
	c.Header("X-Alloc-Size", strconv.Itoa(allocated))
}
