// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand"
	"net/http"
	"strings"
	"time"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00152(c *gin.Context) {
	fieldValue := c.PostForm("field")
	data := strings.ReplaceAll(fieldValue, "\x00", "")
	tokenRNG := rand.New(rand.NewSource(time.Now().UnixNano()))
	apiToken := fmt.Sprintf("%016x", tokenRNG.Uint64())
	DB.Exec("INSERT INTO api_tokens (label, token) VALUES ($1, $2)", data, apiToken)
	c.JSON(http.StatusOK, map[string]string{"token": apiToken})
}
