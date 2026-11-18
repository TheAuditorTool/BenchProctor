// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"net/http"
	"strconv"
	"strings"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/sqs"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00208(c *gin.Context) {
	var msgValue string
	_sqsOut, _sqsErr := sqsClient.ReceiveMessage(context.Background(), &sqs.ReceiveMessageInput{
		QueueUrl:            aws.String("https://sqs.us-east-1.amazonaws.com/123456789012/app-events"),
		MaxNumberOfMessages: 1,
	})
	if _sqsErr == nil && len(_sqsOut.Messages) > 0 {
		msgValue = aws.ToString(_sqsOut.Messages[0].Body)
	}
	var data string
	for _, token := range strings.Split(msgValue, ",") {
		data = token
	}
	var _num int
	if _, _err := fmt.Sscanf(data, "%d", &_num); _err != nil {
		c.String(http.StatusBadRequest, "invalid id")
		return
	}
	parsedId := strconv.Itoa(_num)
	rows, err := DB.Query("SELECT * FROM users WHERE id = $1", parsedId)
	if err != nil {
		c.String(http.StatusInternalServerError, err.Error())
		return
	}
	defer rows.Close()
	c.JSON(200, gin.H{"code": "OK"})
}
