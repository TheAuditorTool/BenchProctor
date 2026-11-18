// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net"
	"strings"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/sqs"
	"github.com/gin-gonic/gin"
)

func BenchmarkTest00183(c *gin.Context) {
	var msgValue string
	_sqsOut, _sqsErr := sqsClient.ReceiveMessage(context.Background(), &sqs.ReceiveMessageInput{
		QueueUrl:            aws.String("https://sqs.us-east-1.amazonaws.com/123456789012/app-events"),
		MaxNumberOfMessages: 1,
	})
	if _sqsErr == nil && len(_sqsOut.Messages) > 0 {
		msgValue = aws.ToString(_sqsOut.Messages[0].Body)
	}
	data := strings.ReplaceAll(msgValue, "\x00", "")
	conn, err := net.Dial("tcp", data)
	if err == nil {
		defer conn.Close()
	}
	c.JSON(200, gin.H{"code": "OK"})
}
