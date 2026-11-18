#![allow(dead_code)]

const REDIS_URL: &str = "redis://cache:6379";
const AMQP_URL: &str = "amqp://guest:guest@broker:5672/%2F";
const MONGO_URL: &str = "mongodb://mongo:27017/app";
const MONGO_DB: &str = "app";
const LDAP_URL: &str = "ldap://directory:1389";
const LDAP_BASE_DN: &str = "dc=example,dc=com";
const DATABASE_PATH: &str = "/var/lib/app/app.db";
const DB_SCHEMA: &str = r#"CREATE TABLE IF NOT EXISTS users (
    id         INTEGER PRIMARY KEY,
    name       TEXT NOT NULL DEFAULT '',
    role       TEXT NOT NULL DEFAULT 'user',
    bio        TEXT NOT NULL DEFAULT '',
    email      TEXT NOT NULL DEFAULT '',
    password   TEXT NOT NULL DEFAULT '',
    token_hash TEXT NOT NULL DEFAULT '',
    locked     INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS accounts (
    id          INTEGER PRIMARY KEY,
    external_id TEXT NOT NULL UNIQUE,
    account_id  TEXT NOT NULL DEFAULT '',
    owner       TEXT NOT NULL DEFAULT '',
    balance     TEXT NOT NULL DEFAULT '0',
    locked      INTEGER NOT NULL DEFAULT 0,
    status      TEXT NOT NULL DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS sessions (
    sid     TEXT PRIMARY KEY,
    owner   TEXT NOT NULL DEFAULT '',
    payload TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS logs (
    id   INTEGER PRIMARY KEY,
    data TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS profiles (
    id      INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL DEFAULT 0,
    bio     TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS comments (
    id      INTEGER PRIMARY KEY,
    post_id INTEGER NOT NULL DEFAULT 0,
    text    TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS documents (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS vault (
    owner  TEXT PRIMARY KEY,
    secret TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS mq_messages (
    id    INTEGER PRIMARY KEY,
    queue TEXT NOT NULL DEFAULT '',
    body  TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS feed (
    id   INTEGER PRIMARY KEY,
    data TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS region_audit (
    id       INTEGER PRIMARY KEY,
    "offset" TEXT NOT NULL DEFAULT '',
    dump     TEXT NOT NULL DEFAULT '',
    byte     TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS admin_actions (
    id  INTEGER PRIMARY KEY,
    cmd TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS kv_cache (
    k     TEXT PRIMARY KEY,
    value TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS resources (
    id    INTEGER PRIMARY KEY,
    owner TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS products (
    id    INTEGER PRIMARY KEY,
    name  TEXT NOT NULL DEFAULT '',
    price DECIMAL(10, 2) NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS statements (
    id         INTEGER PRIMARY KEY,
    account_id TEXT NOT NULL DEFAULT '',
    period     TEXT NOT NULL DEFAULT '',
    iban       TEXT NOT NULL DEFAULT '',
    balance    DECIMAL(12, 2) NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS published_files (
    id        INTEGER PRIMARY KEY,
    folder    TEXT NOT NULL DEFAULT '',
    file_name TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS api_keys (
    key_hash           TEXT PRIMARY KEY,
    owner              TEXT NOT NULL DEFAULT '',
    is_factory_default INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS credentials (
    username             TEXT PRIMARY KEY,
    password_hash        TEXT NOT NULL DEFAULT '',
    must_change_password INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS app_ledger (
    k           TEXT PRIMARY KEY,
    payload        TEXT NOT NULL,
    created_at  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_app_ledger_created
    ON app_ledger (created_at);

INSERT INTO users (id, name, role, bio, email) VALUES
    (1, 'alice', 'user', 'Enjoys hiking', 'alice@example.com'),
    (2, 'bob', 'user', 'Coffee enthusiast', 'bob@example.com'),
    (3, 'admin', 'admin', 'Site administrator', 'admin@example.com')
ON CONFLICT DO NOTHING;

INSERT INTO profiles (id, user_id, bio) VALUES
    (1, 1, 'Enjoys hiking'),
    (2, 2, 'Coffee enthusiast'),
    (3, 3, 'Site administrator')
ON CONFLICT DO NOTHING;

INSERT INTO comments (id, post_id, text) VALUES
    (1, 1, 'Great write-up'),
    (2, 1, 'Thanks for sharing'),
    (3, 1, 'Pinned by the moderators')
ON CONFLICT DO NOTHING;

INSERT INTO accounts (id, external_id, account_id, owner, balance) VALUES
    (1, 'alice', 'acct-1001', 'alice', '100'),
    (2, 'bob', 'acct-1002', 'bob', '100'),
    (3, 'admin', 'acct-1003', 'admin', '100')
ON CONFLICT DO NOTHING;

INSERT INTO mq_messages (id, queue, body) VALUES
    (1, 'app-events', 'msg-001')
ON CONFLICT DO NOTHING;

INSERT INTO kv_cache (k, value) VALUES
    ('user_data', 'cached_value')
ON CONFLICT DO NOTHING;

INSERT INTO products (id, name, price) VALUES
    (1, 'Notebook', 4.50),
    (2, 'Desk lamp', 24.00),
    (3, 'Monitor arm', 89.90)
ON CONFLICT DO NOTHING;

INSERT INTO statements (id, account_id, period, iban, balance) VALUES
    (1, 'alice', '2024-01', 'GB29NWBK60161331926821', 100.00),
    (2, 'bob', '2024-01', 'GB29NWBK60161331926822', 100.00),
    (3, 'admin', '2024-01', 'GB29NWBK60161331926823', 100.00)
ON CONFLICT DO NOTHING;

INSERT INTO api_keys (key_hash, owner, is_factory_default) VALUES
    ('a1d35752d4da7e5eb33bb8b6013ce879c6e747f3d6ccafacb96668795dcf82bb', 'integration', 1),
    ('ca237a335b7a779dafcd4d7ef5bb990a3dca951d9da8ead69f8590db16803268', 'reporting', 0)
ON CONFLICT DO NOTHING;

INSERT INTO credentials (username, password_hash, must_change_password) VALUES
    ('setup', 'pbkdf2_sha256$600000$5f1c9a3e7b2d4f60a8c1e3b5d7f90a2c$4a4fd778e25e08888b610331f85f65276017ea8c0a11437df0ce637a699a221b', 1),
    ('operator', 'pbkdf2_sha256$600000$9e2b7d4c1a6f3e8b0d5c2a7f4e1b8d3c$c84253cbbf0f1610cf96d17b2610e7b3560af31fc8b7286c7119b189b9abb1bd', 0)
ON CONFLICT DO NOTHING;
"#;

static DB: std::sync::LazyLock<Option<std::sync::Mutex<rusqlite::Connection>>> = std::sync::LazyLock::new(|| {
    let conn = rusqlite::Connection::open(database_path()).ok()?;
    conn.execute_batch(DB_SCHEMA).ok()?;
    Some(std::sync::Mutex::new(conn))
});

fn database_path() -> String {
    std::env::var("DATABASE_PATH").unwrap_or_else(|_| DATABASE_PATH.to_string())
}

fn db() -> Option<std::sync::MutexGuard<'static, rusqlite::Connection>> {
    DB.as_ref().map(|m| m.lock().unwrap_or_else(std::sync::PoisonError::into_inner))
}

pub fn seeded_database_path() -> String {
    let _ = std::sync::LazyLock::force(&DB);
    database_path()
}

pub fn db_fetch_one(query: &str) -> String {
    db().and_then(|conn| conn.query_row(query, [], |row| row.get::<_, String>(0)).ok()).unwrap_or_default()
}

pub fn passthrough(v: String) -> String {
    v.trim().to_string()
}

fn amqp_channel(rt: &tokio::runtime::Runtime) -> Option<lapin::Channel> {
    rt.block_on(async {
        let conn = lapin::Connection::connect(AMQP_URL, lapin::ConnectionProperties::default())
            .await
            .ok()?;
        conn.create_channel().await.ok()
    })
}

pub fn queue_get_message(queue: &str) -> String {
    let queue = queue.to_string();
    std::thread::spawn(move || {
        let rt = match tokio::runtime::Builder::new_current_thread().enable_all().build() {
            Ok(rt) => rt,
            Err(_) => return String::new(),
        };
        let channel = match amqp_channel(&rt) {
            Some(ch) => ch,
            None => return String::new(),
        };
        rt.block_on(async move {
            let _ = channel
                .queue_declare(
                    &queue,
                    lapin::options::QueueDeclareOptions { durable: true, ..Default::default() },
                    lapin::types::FieldTable::default(),
                )
                .await;
            match channel
                .basic_get(&queue, lapin::options::BasicGetOptions { no_ack: true })
                .await
            {
                Ok(Some(message)) => String::from_utf8_lossy(&message.data).to_string(),
                _ => String::new(),
            }
        })
    })
    .join()
    .unwrap_or_default()
}
pub fn queue_publish(queue: &str, payload: &str) {
    let queue = queue.to_string();
    let payload = payload.to_string();
    let _ = std::thread::spawn(move || {
        let rt = match tokio::runtime::Builder::new_current_thread().enable_all().build() {
            Ok(rt) => rt,
            Err(_) => return,
        };
        let channel = match amqp_channel(&rt) {
            Some(ch) => ch,
            None => return,
        };
        rt.block_on(async move {
            let _ = channel
                .queue_declare(
                    &queue,
                    lapin::options::QueueDeclareOptions { durable: true, ..Default::default() },
                    lapin::types::FieldTable::default(),
                )
                .await;
            let _ = channel
                .basic_publish(
                    "",
                    &queue,
                    lapin::options::BasicPublishOptions::default(),
                    payload.as_bytes(),
                    lapin::BasicProperties::default(),
                )
                .await;
        });
    })
    .join();
}
pub fn redis_bridge_push(key: &str, payload: &str) {
    if let Ok(client) = redis::Client::open(REDIS_URL) {
        if let Ok(mut conn) = client.get_connection() {
            let _: redis::RedisResult<()> =
                redis::cmd("LPUSH").arg(key).arg(payload).query(&mut conn);
        }
    }
}
pub fn redis_bridge_pop(key: &str) -> String {
    if let Ok(client) = redis::Client::open(REDIS_URL) {
        if let Ok(mut conn) = client.get_connection() {
            if let Ok(value) = redis::cmd("RPOP").arg(key).query::<String>(&mut conn) {
                return value;
            }
        }
    }
    String::new()
}
pub fn redis_bridge_blocking_pop(key: &str) -> String {
    if let Ok(client) = redis::Client::open(REDIS_URL) {
        if let Ok(mut conn) = client.get_connection() {
            if let Ok((_list, value)) =
                redis::cmd("BRPOP").arg(key).arg(0).query::<(String, String)>(&mut conn)
            {
                return value;
            }
        }
    }
    String::new()
}
pub fn ws_recv_message() -> String {
    std::env::var("WS_NEXT_MESSAGE").unwrap_or_default()
}
pub fn dns_txt_lookup(domain: &str) -> String {
    format!("txt_for_{}", domain)
}
pub fn redis_get(key: &str) -> String {
    std::env::var(format!("REDIS_{}", key.to_uppercase())).unwrap_or_default()
}
pub fn memcache_get(key: &str) -> String {
    std::env::var(format!("MEMCACHE_{}", key.to_uppercase())).unwrap_or_default()
}
pub fn s3_get_object(bucket: &str, key: &str) -> String {
    let (bucket, key) = (bucket.to_string(), key.to_string());
    std::thread::spawn(move || {
        let rt = match tokio::runtime::Builder::new_current_thread().enable_all().build() {
            Ok(rt) => rt,
            Err(_) => return String::new(),
        };
        rt.block_on(async move {
            let config = aws_config::load_defaults(aws_config::BehaviorVersion::latest()).await;
            let client = aws_sdk_s3::Client::new(&config);
            match client.get_object().bucket(bucket).key(key).send().await {
                Ok(output) => match output.body.collect().await {
                    Ok(agg) => String::from_utf8_lossy(&agg.into_bytes()).to_string(),
                    Err(_) => String::new(),
                },
                Err(_) => String::new(),
            }
        })
    })
    .join()
    .unwrap_or_default()
}
pub fn sqs_receive_message(queue: &str) -> String {
    std::env::var(format!("SQS_{}_NEXT", queue.to_uppercase())).unwrap_or_default()
}
pub fn s3_put_object(bucket: &str, key: &str, body: &[u8]) {
    let (bucket, key, body) = (bucket.to_string(), key.to_string(), body.to_vec());
    let _ = std::thread::spawn(move || {
        if let Ok(rt) = tokio::runtime::Builder::new_current_thread().enable_all().build() {
            rt.block_on(async move {
                let config = aws_config::load_defaults(aws_config::BehaviorVersion::latest()).await;
                aws_sdk_s3::Client::new(&config)
                    .put_object()
                    .bucket(bucket)
                    .key(key)
                    .body(aws_sdk_s3::primitives::ByteStream::from(body))
                    .send()
                    .await
                    .ok();
            });
        }
    })
    .join();
}
pub fn iam_put_role_policy(role: &str, name: &str, doc: &str) {
    let (role, name, doc) = (role.to_string(), name.to_string(), doc.to_string());
    let _ = std::thread::spawn(move || {
        if let Ok(rt) = tokio::runtime::Builder::new_current_thread().enable_all().build() {
            rt.block_on(async move {
                let config = aws_config::load_defaults(aws_config::BehaviorVersion::latest()).await;
                aws_sdk_iam::Client::new(&config)
                    .put_role_policy()
                    .role_name(role)
                    .policy_name(name)
                    .policy_document(doc)
                    .send()
                    .await
                    .ok();
            });
        }
    })
    .join();
}
pub fn sts_assume_role(role_arn: &str, session_name: &str) {
    let (role_arn, session_name) = (role_arn.to_string(), session_name.to_string());
    let _ = std::thread::spawn(move || {
        if let Ok(rt) = tokio::runtime::Builder::new_current_thread().enable_all().build() {
            rt.block_on(async move {
                let config = aws_config::load_defaults(aws_config::BehaviorVersion::latest()).await;
                aws_sdk_sts::Client::new(&config)
                    .assume_role()
                    .role_arn(role_arn)
                    .role_session_name(session_name)
                    .send()
                    .await
                    .ok();
            });
        }
    })
    .join();
}
pub fn sqs_send_message(queue_url: &str, body: &str) {
    let (queue_url, body) = (queue_url.to_string(), body.to_string());
    let _ = std::thread::spawn(move || {
        if let Ok(rt) = tokio::runtime::Builder::new_current_thread().enable_all().build() {
            rt.block_on(async move {
                let config = aws_config::load_defaults(aws_config::BehaviorVersion::latest()).await;
                aws_sdk_sqs::Client::new(&config)
                    .send_message()
                    .queue_url(queue_url)
                    .message_body(body)
                    .send()
                    .await
                    .ok();
            });
        }
    })
    .join();
}
pub fn message_hmac(body: &str) -> String {
    use hmac::{Hmac, Mac};
    let key = std::env::var("MSG_HMAC_KEY").unwrap_or_else(|_| "shared-mesh-secret".to_string());
    let mut mac = match <Hmac<sha2::Sha256> as Mac>::new_from_slice(key.as_bytes()) {
        Ok(m) => m,
        Err(_) => return String::new(),
    };
    mac.update(body.as_bytes());
    hex::encode(mac.finalize().into_bytes())
}
pub fn kafka_consume() -> String {
    std::env::var("KAFKA_NEXT_OFFSET").unwrap_or_default()
}
pub fn ssm_get_parameter(name: &str) -> String {
    std::env::var(name.to_uppercase().replace(['/', '-'], "_")).unwrap_or_default()
}
pub fn uploaded_filename() -> String {
    std::env::var("UPLOAD_FILENAME").unwrap_or_default()
}
pub fn clipboard_paste() -> String {
    std::env::var("CLIPBOARD_NEXT").unwrap_or_default()
}
pub fn auth_check(user: &str, token: &str) -> bool {
    !user.is_empty() && user == token
}
pub fn acl_check(user: &str, perm: &str) -> bool {
    !user.is_empty() && !perm.is_empty()
}
pub fn verify_bearer(token: &str) -> bool {
    let expected = std::env::var("APP_SESSION_SECRET").unwrap_or_default();
    !expected.is_empty() && token == expected
}
pub fn user_has_role(user: &str, role: &str) -> bool {
    const ROLE_MAP: &[(&str, &str)] = &[("svc-admin", "admin"), ("svc-writer", "write"), ("svc-reader", "read")];
    ROLE_MAP.iter().any(|(u, r)| *u == user && *r == role)
}
pub fn hash_hex(value: &str) -> String {
    use sha2::Digest;
    format!("{:x}", sha2::Sha256::digest(value.as_bytes()))
}
pub fn expected_csrf() -> String {
    std::env::var("CSRF_TOKEN").unwrap_or_default()
}
pub fn respond_json(status: u16, body: &str) -> String {
    format!("{{\"status_code\": {}, \"body\": \"{}\"}}", status, body)
}
fn db_rows<P: rusqlite::Params>(sql: &str, params: P) {
    if let Some(conn) = db() {
        if let Ok(mut stmt) = conn.prepare(sql) {
            if let Ok(mut rows) = stmt.query(params) {
                while let Ok(Some(_)) = rows.next() {}
            }
        }
    }
}
pub fn db_query(sql: &str) {
    db_rows(sql, []);
}
pub fn db_query_bind(sql: &str, param: &str) {
    db_rows(sql, rusqlite::params![param]);
}
pub fn db_query_bind_named(sql: &str, param: &str) {
    db_rows(sql, rusqlite::named_params! { ":id": param });
}
pub fn db_exec(sql: &str) {
    if let Some(conn) = db() { let _ = conn.execute(sql, []); }
}
pub fn db_exec_bind(sql: &str, param: &str) {
    if let Some(conn) = db() { let _ = conn.execute(sql, rusqlite::params![param]); }
}
pub fn db_connect(dsn: &str) {
    let dsn = dsn.to_string();
    let _ = std::thread::spawn(move || {
        if let Ok(rt) = tokio::runtime::Builder::new_current_thread().enable_all().build() {
            rt.block_on(async move {
                use sqlx::Connection;
                if let Ok(conn) = sqlx::postgres::PgConnection::connect(&dsn).await {
                    let _ = conn.close().await;
                }
            });
        }
    })
    .join();
}
diesel::table! {
    users (id) {
        id -> diesel::sql_types::Integer,
        name -> diesel::sql_types::Text,
    }
}
pub fn orm_find_by_name(name: &str) {
    use diesel::prelude::*;
    if let Ok(mut conn) = diesel::SqliteConnection::establish(&seeded_database_path()) {
        let _ = users::table.filter(users::name.eq(name)).load::<(i32, String)>(&mut conn);
    }
}
pub fn orm_sql_query(sql: &str) {
    use diesel::prelude::*;
    if let Ok(mut conn) = diesel::SqliteConnection::establish(&seeded_database_path()) {
        let _ = diesel::sql_query(sql).execute(&mut conn);
    }
}
pub fn fetch_url(url: &str) -> String { std::env::var("EXTERNAL_API_RESPONSE").unwrap_or_else(|_| url.to_string()) }
pub async fn nosql_find_one(filter: &str) {
    let client = match mongodb::Client::with_uri_str(MONGO_URL).await {
        Ok(c) => c,
        Err(_) => return,
    };
    let coll = client.database(MONGO_DB).collection::<mongodb::bson::Document>("users");
    let _ = coll.find_one(mongodb::bson::doc! { "$where": filter }, None).await;
}
pub fn ldap_search(filter: &str) {
    let filter = filter.to_string();
    let _ = std::thread::spawn(move || {
        let url = std::env::var("LDAP_URL").unwrap_or_else(|_| LDAP_URL.to_string());
        if let Ok(mut conn) = ldap3::LdapConn::new(&url) {
            let _ = conn.search(LDAP_BASE_DN, ldap3::Scope::Subtree, &filter, vec!["cn"]);
        }
    })
    .join();
}
pub fn xpath_eval(expr: &str) {
    if let Ok(pkg) = sxd_document::parser::parse("<users><user id='1'/></users>") {
        let doc = pkg.as_document();
        let _ = sxd_xpath::evaluate_xpath(&doc, expr);
    }
}
pub fn jwt_sign(secret: &str) -> String {
    use hmac::{Hmac, Mac};
    use base64::Engine;
    let header_payload = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyIn0";
    let mut mac = match <Hmac<sha2::Sha256> as Mac>::new_from_slice(secret.as_bytes()) {
        Ok(m) => m,
        Err(_) => return String::new(),
    };
    mac.update(header_payload.as_bytes());
    let sig = base64::engine::general_purpose::URL_SAFE_NO_PAD.encode(mac.finalize().into_bytes());
    format!("{}.{}", header_payload, sig)
}
pub fn write_csv(row: &str) {
    let mut wtr = csv::Writer::from_writer(Vec::new());
    let _ = wtr.write_record([row]);
    let _ = wtr.flush();
}
pub fn store_session(key: &str, value: &str) {
    if let Ok(mut m) = SESSION_STORE.lock() { m.insert(key.to_string(), value.to_string()); }
}
pub fn keyring_get(key: &str) -> String {
    std::env::var(format!("KEYRING_{}", key.to_uppercase())).unwrap_or_default()
}
pub fn vault_get(key: &str) -> String {
    std::env::var(format!("VAULT_{}", key.to_uppercase())).unwrap_or_default()
}
const BRIDGE_DB_PATH: &str = "/var/lib/app/shared_state.db";
pub fn shared_db_write(key: &str, payload: &str) {
    if let Ok(conn) = rusqlite::Connection::open(BRIDGE_DB_PATH) {
        let _ = conn.execute("CREATE TABLE IF NOT EXISTS app_ledger (k TEXT PRIMARY KEY, payload TEXT)", []);
        let _ = conn.execute("INSERT OR REPLACE INTO app_ledger (k, payload) VALUES (?1, ?2)", rusqlite::params![key, payload]);
    }
}
pub fn shared_db_read(key: &str) -> String {
    if let Ok(conn) = rusqlite::Connection::open(BRIDGE_DB_PATH) {
        let _ = conn.execute("CREATE TABLE IF NOT EXISTS app_ledger (k TEXT PRIMARY KEY, payload TEXT)", []);
        if let Ok(val) = conn.query_row("SELECT payload FROM app_ledger WHERE k = ?1", rusqlite::params![key], |row| row.get::<_, String>(0)) {
            return val;
        }
    }
    String::new()
}

pub static SHARED_DATA: std::sync::Mutex<String> = std::sync::Mutex::new(String::new());
pub static SESSION_USER: std::sync::Mutex<String> = std::sync::Mutex::new(String::new());
pub static SESSION_STORE: std::sync::Mutex<std::collections::BTreeMap<String, String>> = std::sync::Mutex::new(std::collections::BTreeMap::new());

pub fn current_session_user() -> String {
    SESSION_USER.lock().map(|g| g.clone()).unwrap_or_default()
}

pub static NATIVE_EXT_INPUT: std::sync::Mutex<String> = std::sync::Mutex::new(String::new());
pub fn set_native_ext_input(value: &str) {
    if let Ok(mut g) = NATIVE_EXT_INPUT.lock() { *g = value.to_string(); }
}
pub fn native_ext_input() -> String {
    NATIVE_EXT_INPUT.lock().map(|g| g.clone()).unwrap_or_default()
}

pub fn encrypt(plaintext: &str) -> String {
    use aes_gcm::aead::{Aead, KeyInit};
    use aes_gcm::{Aes256Gcm, Nonce};
    use base64::Engine;
    let key_bytes: [u8; 32] = rand::random();
    let cipher = match Aes256Gcm::new_from_slice(&key_bytes) {
        Ok(c) => c,
        Err(_) => return String::new(),
    };
    let nonce_bytes: [u8; 12] = rand::random();
    let nonce = Nonce::from_slice(&nonce_bytes);
    let ciphertext = cipher.encrypt(nonce, plaintext.as_bytes()).unwrap_or_default();
    let mut framed = nonce_bytes.to_vec();
    framed.extend_from_slice(&ciphertext);
    base64::engine::general_purpose::STANDARD.encode(framed)
}
pub fn encrypt_with_key(key: &str, data: &str) -> String {
    use aes_gcm::aead::{Aead, KeyInit};
    use aes_gcm::{Aes256Gcm, Nonce};
    use base64::Engine;
    let mut key_bytes = [0u8; 32];
    let kb = key.as_bytes();
    let n = kb.len().min(32);
    key_bytes[..n].copy_from_slice(&kb[..n]);
    let cipher = match Aes256Gcm::new_from_slice(&key_bytes) {
        Ok(c) => c,
        Err(_) => return String::new(),
    };
    let nonce_bytes: [u8; 12] = rand::random();
    let nonce = Nonce::from_slice(&nonce_bytes);
    let ciphertext = cipher.encrypt(nonce, data.as_bytes()).unwrap_or_default();
    let mut framed = nonce_bytes.to_vec();
    framed.extend_from_slice(&ciphertext);
    base64::engine::general_purpose::STANDARD.encode(framed)
}
pub fn set_cookie(value: &str) {
    let _ = cookie::Cookie::parse(value.to_string());
}
pub struct AppResponse(pub rocket::response::Response<'static>);
impl<'r> rocket::response::Responder<'r, 'static> for AppResponse {
    fn respond_to(self, _: &'r rocket::Request<'_>) -> rocket::response::Result<'static> {
        Ok(self.0)
    }
}
