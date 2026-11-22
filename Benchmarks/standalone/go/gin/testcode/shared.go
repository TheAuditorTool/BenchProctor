package testcode

import (
	"context"
	"crypto/aes"
	"crypto/cipher"
	"crypto/hmac"
	"crypto/rand"
	"crypto/rsa"
	"database/sql"
	"encoding/base64"
	"encoding/json"
	"net/http"
	"os"
	"strings"
	"sync"
	"sync/atomic"

	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/iam"
	"github.com/aws/aws-sdk-go-v2/service/s3"
	"github.com/aws/aws-sdk-go-v2/service/sqs"
	"github.com/aws/aws-sdk-go-v2/service/ssm"
	"github.com/aws/aws-sdk-go-v2/service/sts"
	"github.com/redis/go-redis/v9"
	"go.mongodb.org/mongo-driver/v2/mongo"
	"go.mongodb.org/mongo-driver/v2/mongo/options"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

var DB *sql.DB

var mongoClient, _ = mongo.Connect(options.Client().ApplyURI(envOr("MONGO_URL", "mongodb://mongo:27017/app")))

var redisClient = redis.NewClient(&redis.Options{Addr: "cache:6379"})

var awsCfg, _ = config.LoadDefaultConfig(context.Background())

var (
	s3Client  = s3.NewFromConfig(awsCfg)
	iamClient = iam.NewFromConfig(awsCfg)
	stsClient = sts.NewFromConfig(awsCfg)
	sqsClient = sqs.NewFromConfig(awsCfg)
	ssmClient = ssm.NewFromConfig(awsCfg)
)

var rsaKeyPair, _ = rsa.GenerateKey(rand.Reader, 2048)

var storageKey = func() []byte {
	k := make([]byte, 32)
	rand.Read(k)
	return k
}()

var lastRequestValue atomic.Value

var loginAttempts atomic.Int64

var trustedSettings sync.Map

type requestEnvelope struct{ body string }

type submissionForm struct{ payload string }

type ctxKey string

const (
	ctxKeyData ctxKey = "data"
	ctxKeyUser ctxKey = "user"
)

var (
	sharedCounter   string
	sharedCounterMu sync.Mutex
)

func SetDB(db *sql.DB) {
	DB = db
	if g, err := gorm.Open(postgres.New(postgres.Config{Conn: db}), &gorm.Config{DisableAutomaticPing: true}); err == nil {
		gormDB = g
	}
}

type User struct {
	ID   uint
	Name string
}

var gormDB *gorm.DB

func envOr(key, fallback string) string {
	if v := os.Getenv(key); v != "" {
		return v
	}
	return fallback
}

func RespondJSON(w http.ResponseWriter, status int, data interface{}) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	json.NewEncoder(w).Encode(data)
}

func ParseJSONBody(r *http.Request, v interface{}) error {
	return json.NewDecoder(r.Body).Decode(v)
}

func normalizeField(v string) string { return strings.TrimSpace(v) }

func authVerify(claim, token string) bool {
	return claim != "" && hmac.Equal([]byte(claim), []byte(token))
}

func verifyBearer(authHeader string) bool {
	expected := os.Getenv("APP_SESSION_SECRET")
	if expected == "" {
		return false
	}
	const prefix = "Bearer "
	if !strings.HasPrefix(authHeader, prefix) {
		return false
	}
	return hmac.Equal([]byte(authHeader[len(prefix):]), []byte(expected))
}

func aclCheck(user, perm string) bool {
	grants := map[string][]string{
		"admin":   {"admin", "read", "write", "delete", "session:write"},
		"service": {"read", "write", "session:write"},
	}
	for _, p := range grants[user] {
		if p == perm {
			return true
		}
	}
	return false
}

func ctxString(r *http.Request, k ctxKey) string {
	v, _ := r.Context().Value(k).(string)
	return v
}

func encryptForStorage(plaintext string) string {
	block, err := aes.NewCipher(storageKey)
	if err != nil {
		return ""
	}
	gcm, err := cipher.NewGCM(block)
	if err != nil {
		return ""
	}
	nonce := make([]byte, gcm.NonceSize())
	rand.Read(nonce)
	return base64.StdEncoding.EncodeToString(gcm.Seal(nonce, nonce, []byte(plaintext), nil))
}

type pluginActions struct{}

func (pluginActions) Reload() {
	os.Setenv("PLUGIN_STATE", "reloaded")
}

func (pluginActions) Shutdown() {
	os.Setenv("PLUGIN_STATE", "shutdown")
}

func alnumFilter(s string) string {
	var b strings.Builder
	for _, r := range s {
		if (r >= 'a' && r <= 'z') || (r >= 'A' && r <= 'Z') || (r >= '0' && r <= '9') {
			b.WriteRune(r)
		}
	}
	out := b.String()
	if len(out) > 32 {
		return out[:32]
	}
	return out
}
