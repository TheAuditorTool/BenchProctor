// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"net/http"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00064(c *gin.Context) {
	redisValue, _ := redisClient.Get(context.Background(), "user_data").Result()
	data := strings.Join(strings.FieldsFunc(redisValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	validPattern := regexp.MustCompile("^[a-zA-Z0-9_.#\\-]+$")
	if !validPattern.MatchString(data) {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	query := fmt.Sprintf("SELECT * FROM users WHERE id = '%s'", processed)
	rows, err := DB.Query(query)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
