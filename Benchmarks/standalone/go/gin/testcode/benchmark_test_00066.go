// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand/v2"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00066(c *gin.Context) {
	userID := c.Query("id")
	tokenRNG := rand.New(rand.NewPCG(rand.Uint64(), rand.Uint64()))
	apiToken := fmt.Sprintf("%016x", tokenRNG.Uint64())
	DB.Exec("INSERT INTO api_tokens (label, token) VALUES ($1, $2)", userID, apiToken)
	c.JSON(http.StatusOK, map[string]string{"token": apiToken})
}
