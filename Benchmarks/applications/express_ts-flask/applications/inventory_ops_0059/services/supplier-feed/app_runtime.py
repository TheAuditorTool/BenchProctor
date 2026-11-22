"""Application runtime.

The stream and the cache are the ones the compose file provisions, and both are
bound at module scope, so a client for a host the compose file never declares
is not a latent problem, it is a service that cannot start.

The database is this service's own store, built from the schema under
``db/migrations`` and seeded with the same rows.
"""
import hashlib
import hmac
import os
import sqlite3
from typing import Any

DB_PATH = os.environ.get("DATABASE_PATH", "app.db")

_SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id         INTEGER PRIMARY KEY,
    name       TEXT NOT NULL DEFAULT '',
    role       TEXT NOT NULL DEFAULT 'user',
    bio        TEXT NOT NULL DEFAULT '',
    email      TEXT NOT NULL DEFAULT '',
    password   TEXT NOT NULL DEFAULT '',
    token_hash TEXT NOT NULL DEFAULT '',
    locked     INTEGER NOT NULL DEFAULT 0,
    active     BOOLEAN NOT NULL DEFAULT TRUE,
    pw_hash    TEXT NOT NULL DEFAULT '',
    pw_salt    TEXT NOT NULL DEFAULT '',
    security_answer TEXT NOT NULL DEFAULT '',
    reset_code TEXT NOT NULL DEFAULT '',
    login_code TEXT NOT NULL DEFAULT '',
    otp_code   TEXT NOT NULL DEFAULT '',
    totp_code  TEXT NOT NULL DEFAULT '',
    failed_logins INTEGER NOT NULL DEFAULT 0,
    mfa_enabled BOOLEAN NOT NULL DEFAULT FALSE,
    tenant_id  TEXT NOT NULL DEFAULT '',
    invited_by TEXT NOT NULL DEFAULT '',
    account_id TEXT NOT NULL DEFAULT '',
    date_of_birth TEXT NOT NULL DEFAULT '',
    national_id TEXT NOT NULL DEFAULT '',
    user_id    INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS accounts (
    id          INTEGER PRIMARY KEY,
    external_id TEXT NOT NULL UNIQUE,
    account_id  TEXT NOT NULL DEFAULT '',
    owner       TEXT NOT NULL DEFAULT '',
    balance     TEXT NOT NULL DEFAULT '0',
    locked      INTEGER NOT NULL DEFAULT 0,
    status      TEXT NOT NULL DEFAULT 'active',
    name        TEXT NOT NULL DEFAULT '',
    display_name TEXT NOT NULL DEFAULT '',
    email       TEXT NOT NULL DEFAULT '',
    date_of_birth TEXT NOT NULL DEFAULT '',
    national_id TEXT NOT NULL DEFAULT '',
    plan        TEXT NOT NULL DEFAULT 'standard',
    changed_by  TEXT NOT NULL DEFAULT '',
    api_secret  TEXT NOT NULL DEFAULT '',
    daily_limit DECIMAL(12, 2) NOT NULL DEFAULT 1000
);

CREATE TABLE IF NOT EXISTS sessions (
    sid     TEXT PRIMARY KEY,
    owner   TEXT NOT NULL DEFAULT '',
    payload TEXT NOT NULL DEFAULT '',
    user_name TEXT NOT NULL DEFAULT '',
    principal TEXT NOT NULL DEFAULT ''
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
    name TEXT NOT NULL DEFAULT '',
    title TEXT NOT NULL DEFAULT '',
    body TEXT NOT NULL DEFAULT '',
    content TEXT NOT NULL DEFAULT '',
    owner TEXT NOT NULL DEFAULT '',
    owner_id TEXT NOT NULL DEFAULT '',
    document_id INTEGER NOT NULL DEFAULT 0
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
    price DECIMAL(10, 2) NOT NULL DEFAULT 0,
    sku   TEXT NOT NULL DEFAULT '',
    tenant_id TEXT NOT NULL DEFAULT '',
    supplier_cost DECIMAL(12, 2) NOT NULL DEFAULT 0,
    supplier_api_key TEXT NOT NULL DEFAULT '',
    row_id INTEGER NOT NULL DEFAULT 0,
    price_cents INTEGER NOT NULL DEFAULT 0,
    supplier_cost_cents INTEGER NOT NULL DEFAULT 0
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
    is_factory_default INTEGER NOT NULL DEFAULT 0,
    revoked            INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS credentials (
    username             TEXT PRIMARY KEY,
    password_hash        TEXT NOT NULL DEFAULT '',
    must_change_password INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS inventory_ledger (
    k           TEXT PRIMARY KEY,
    payload        TEXT NOT NULL,
    created_at  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_inventory_ledger_created
    ON inventory_ledger (created_at);

CREATE TABLE IF NOT EXISTS admin_reports (
    id   INTEGER PRIMARY KEY,
    slug TEXT NOT NULL DEFAULT '',
    body TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS api_tokens (
    id        INTEGER PRIMARY KEY,
    owner     TEXT NOT NULL DEFAULT '',
    user_name TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS articles (
    id    INTEGER PRIMARY KEY,
    title TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS audit_events (
    id         INTEGER PRIMARY KEY,
    action     TEXT NOT NULL DEFAULT '',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS audit_log (
    id         INTEGER PRIMARY KEY,
    action     TEXT NOT NULL DEFAULT '',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cache_entries (
    id        INTEGER PRIMARY KEY,
    cache_key TEXT NOT NULL DEFAULT '',
    value     TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS cache_index (
    id        INTEGER PRIMARY KEY,
    cache_key TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS carts (
    id       INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL DEFAULT 0,
    total    DECIMAL(12, 2) NOT NULL DEFAULT 0,
    status   TEXT NOT NULL DEFAULT 'open'
);

CREATE TABLE IF NOT EXISTS catalog_items (
    id            INTEGER PRIMARY KEY,
    sku           TEXT NOT NULL DEFAULT '',
    name          TEXT NOT NULL DEFAULT '',
    supplier_cost DECIMAL(12, 2) NOT NULL DEFAULT 0,
    tenant_id     TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS checkout_state (
    id       INTEGER PRIMARY KEY,
    token    TEXT NOT NULL DEFAULT '',
    order_id INTEGER NOT NULL DEFAULT 0,
    total    DECIMAL(12, 2) NOT NULL DEFAULT 0,
    status   TEXT NOT NULL DEFAULT 'open'
);

CREATE TABLE IF NOT EXISTS checkouts (
    id          INTEGER PRIMARY KEY,
    order_id    INTEGER NOT NULL DEFAULT 0,
    customer_id TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS customer_records (
    id             INTEGER PRIMARY KEY,
    ssn            TEXT NOT NULL DEFAULT '',
    ssn_digest     TEXT NOT NULL DEFAULT '',
    ssn_ciphertext TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS customers (
    id  INTEGER PRIMARY KEY,
    ssn TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS daily_totals (
    id     INTEGER PRIMARY KEY,
    period TEXT NOT NULL DEFAULT '',
    total  DECIMAL(12, 2) NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS device_tokens (
    id           INTEGER PRIMARY KEY,
    device_id    TEXT NOT NULL DEFAULT '',
    owner        TEXT NOT NULL DEFAULT '',
    user_id      TEXT NOT NULL DEFAULT '',
    token_hash   TEXT NOT NULL DEFAULT '',
    token_sha256 TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS devices (
    id         INTEGER PRIMARY KEY,
    user_id    TEXT NOT NULL DEFAULT '',
    token_hash TEXT NOT NULL DEFAULT '',
    totp_code  TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS disputes (
    id      INTEGER PRIMARY KEY,
    account TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS exchange_rates (
    id   INTEGER PRIMARY KEY,
    feed TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS export_jobs (
    id      INTEGER PRIMARY KEY,
    job_id  INTEGER NOT NULL DEFAULT 0,
    user_id TEXT NOT NULL DEFAULT '',
    action  TEXT NOT NULL DEFAULT '',
    state   TEXT NOT NULL DEFAULT 'queued'
);

CREATE TABLE IF NOT EXISTS exports (
    id         INTEGER PRIMARY KEY,
    name       TEXT NOT NULL DEFAULT '',
    owner      TEXT NOT NULL DEFAULT '',
    path       TEXT NOT NULL DEFAULT '',
    details    TEXT NOT NULL DEFAULT '',
    archived   BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS feature_flags (
    id      INTEGER PRIMARY KEY,
    name    TEXT NOT NULL DEFAULT '',
    enabled BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS imported_records (
    id     INTEGER PRIMARY KEY,
    record TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS invite_tokens (
    id        INTEGER PRIMARY KEY,
    owner     TEXT NOT NULL DEFAULT '',
    token     BIGINT NOT NULL DEFAULT 0,
    issued_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS invoice_lines (
    id          INTEGER PRIMARY KEY,
    sku         TEXT NOT NULL DEFAULT '',
    qty         INTEGER NOT NULL DEFAULT 0,
    total_cents INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS invoices (
    id           INTEGER PRIMARY KEY,
    invoice_id   INTEGER NOT NULL DEFAULT 0,
    number       TEXT NOT NULL DEFAULT '',
    customer_ref TEXT NOT NULL DEFAULT '',
    tenant_id    TEXT NOT NULL DEFAULT '',
    status       TEXT NOT NULL DEFAULT 'open',
    total        DECIMAL(12, 2) NOT NULL DEFAULT 0,
    total_cents  INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS ip_allowlist (
    id   INTEGER PRIMARY KEY,
    addr TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS items (
    id   INTEGER PRIMARY KEY,
    sku  TEXT NOT NULL DEFAULT '',
    name TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS job_queue (
    id     INTEGER PRIMARY KEY,
    action TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS jobs (
    id       INTEGER PRIMARY KEY,
    job_id   INTEGER NOT NULL DEFAULT 0,
    name     TEXT NOT NULL DEFAULT '',
    owner    TEXT NOT NULL DEFAULT '',
    owner_id TEXT NOT NULL DEFAULT '',
    state    TEXT NOT NULL DEFAULT 'queued'
);

CREATE TABLE IF NOT EXISTS login_challenges (
    id                INTEGER PRIMARY KEY,
    user_id           TEXT NOT NULL DEFAULT '',
    user_name         TEXT NOT NULL DEFAULT '',
    otp_code          TEXT NOT NULL DEFAULT '',
    password_verified BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS mfa_challenges (
    id         INTEGER PRIMARY KEY,
    user_id    TEXT NOT NULL DEFAULT '',
    code       TEXT NOT NULL DEFAULT '',
    expires_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS order_lines (
    id          INTEGER PRIMARY KEY,
    sku         TEXT NOT NULL DEFAULT '',
    qty         INTEGER NOT NULL DEFAULT 0,
    quantity    INTEGER NOT NULL DEFAULT 0,
    total_cents INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS orders (
    id          INTEGER PRIMARY KEY,
    order_id    INTEGER NOT NULL DEFAULT 0,
    user_id     INTEGER NOT NULL DEFAULT 0,
    customer_id TEXT NOT NULL DEFAULT '',
    owner       TEXT NOT NULL DEFAULT '',
    sku         TEXT NOT NULL DEFAULT '',
    quantity    INTEGER NOT NULL DEFAULT 0,
    total       DECIMAL(12, 2) NOT NULL DEFAULT 0,
    total_cents INTEGER NOT NULL DEFAULT 0,
    status      TEXT NOT NULL DEFAULT 'open'
);

CREATE TABLE IF NOT EXISTS password_resets (
    id           INTEGER PRIMARY KEY,
    user_id      TEXT NOT NULL DEFAULT '',
    user_name    TEXT NOT NULL DEFAULT '',
    name         TEXT NOT NULL DEFAULT '',
    account      TEXT NOT NULL DEFAULT '',
    token_hash   TEXT NOT NULL DEFAULT '',
    token_sha256 TEXT NOT NULL DEFAULT '',
    expires_at   BIGINT NOT NULL DEFAULT 0,
    used_at      TIMESTAMP
);

CREATE TABLE IF NOT EXISTS patients (
    id            INTEGER PRIMARY KEY,
    ssn           TEXT NOT NULL DEFAULT '',
    ssn_encrypted TEXT NOT NULL DEFAULT '',
    ssn_hash      TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS pricing (
    id        INTEGER PRIMARY KEY,
    sku       TEXT NOT NULL DEFAULT '',
    tenant_id TEXT NOT NULL DEFAULT '',
    unit_cost DECIMAL(12, 2) NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS projects (
    id        INTEGER PRIMARY KEY,
    tenant_id TEXT NOT NULL DEFAULT '',
    name      TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS recovery_answers (
    id      INTEGER PRIMARY KEY,
    account TEXT NOT NULL DEFAULT '',
    answer  TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS refunds (
    id           INTEGER PRIMARY KEY,
    requested_by TEXT NOT NULL DEFAULT '',
    state        TEXT NOT NULL DEFAULT 'pending'
);

CREATE TABLE IF NOT EXISTS reset_tokens (
    id      INTEGER PRIMARY KEY,
    account TEXT NOT NULL DEFAULT '',
    token   TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS reviews (
    id          INTEGER PRIMARY KEY,
    review_id   INTEGER NOT NULL DEFAULT 0,
    author_id   INTEGER NOT NULL DEFAULT 0,
    review_text TEXT NOT NULL DEFAULT '',
    rating      INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS service_accounts (
    id            INTEGER PRIMARY KEY,
    name          TEXT NOT NULL DEFAULT '',
    password      TEXT NOT NULL DEFAULT '',
    password_hash TEXT NOT NULL DEFAULT '',
    pw_hash       TEXT NOT NULL DEFAULT '',
    pw_salt       TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS service_credentials (
    id       INTEGER PRIMARY KEY,
    name     TEXT NOT NULL DEFAULT '',
    password TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS settings (
    id               INTEGER PRIMARY KEY,
    maintenance_mode BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS signing_keys (
    id         INTEGER PRIMARY KEY,
    key_id     TEXT NOT NULL DEFAULT '',
    retired    BOOLEAN NOT NULL DEFAULT FALSE,
    retired_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS subscriptions (
    id              INTEGER PRIMARY KEY,
    subscription_id TEXT NOT NULL DEFAULT '',
    status          TEXT NOT NULL DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS tax_records (
    id  INTEGER PRIMARY KEY,
    ssn TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS transfers (
    id         INTEGER PRIMARY KEY,
    account_id TEXT NOT NULL DEFAULT '',
    amount     DECIMAL(12, 2) NOT NULL DEFAULT 0,
    status     TEXT NOT NULL DEFAULT 'pending',
    state      TEXT NOT NULL DEFAULT 'pending'
);

CREATE TABLE IF NOT EXISTS uploads (
    id            INTEGER PRIMARY KEY,
    stored_name   TEXT NOT NULL DEFAULT '',
    original_name TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS user_grants (
    id          INTEGER PRIMARY KEY,
    user_id     TEXT NOT NULL DEFAULT '',
    name        TEXT NOT NULL DEFAULT '',
    permissions TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS vault_entries (
    id     INTEGER PRIMARY KEY,
    owner  TEXT NOT NULL DEFAULT '',
    secret TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS webhook_events (
    id      INTEGER PRIMARY KEY,
    event   TEXT NOT NULL DEFAULT '',
    payload TEXT NOT NULL DEFAULT ''
);

INSERT INTO users (id, name, role, bio, email, tenant_id, account_id, date_of_birth, national_id) VALUES
    (1, 'alice', 'user', 'Enjoys hiking', 'alice@example.com', 'acme', 'acct-1001', '1990-04-12', 'QQ123456A'),
    (2, 'bob', 'user', 'Coffee enthusiast', 'bob@example.com', 'globex', 'acct-1002', '1985-11-03', 'QQ654321B'),
    (3, 'admin', 'admin', 'Site administrator', 'admin@example.com', 'acme', 'acct-1003', '1979-06-21', 'QQ112233C')
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

INSERT INTO accounts (id, external_id, account_id, owner, balance, name, display_name, email, date_of_birth, national_id) VALUES
    (1, 'alice', 'acct-1001', 'alice', '100', 'alice', 'Alice', 'alice@example.com', '1990-04-12', 'QQ123456A'),
    (2, 'bob', 'acct-1002', 'bob', '100', 'bob', 'Bob', 'bob@example.com', '1985-11-03', 'QQ654321B'),
    (3, 'admin', 'acct-1003', 'admin', '100', 'admin', 'Admin', 'admin@example.com', '1979-06-21', 'QQ112233C')
ON CONFLICT DO NOTHING;

INSERT INTO mq_messages (id, queue, body) VALUES
    (1, 'app-events', 'msg-001')
ON CONFLICT DO NOTHING;

INSERT INTO kv_cache (k, value) VALUES
    ('user_data', 'cached_value')
ON CONFLICT DO NOTHING;

INSERT INTO products (id, name, price, sku, tenant_id, supplier_cost, row_id, price_cents, supplier_cost_cents) VALUES
    (1, 'Notebook', 4.50, 'SKU-1001', 'acme', 2.10, 1, 450, 210),
    (2, 'Desk lamp', 24.00, 'SKU-1002', 'acme', 11.40, 2, 2400, 1140),
    (3, 'Monitor arm', 89.90, 'SKU-1003', 'globex', 52.00, 3, 8990, 5200)
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

INSERT INTO documents (id, name, title, body, content, owner, owner_id, document_id) VALUES
    (1, 'notes-1.txt', 'Notes 1', 'Enjoys hiking', 'Enjoys hiking', 'alice', 'alice', 1),
    (2, 'notes-2.txt', 'Notes 2', 'Coffee enthusiast', 'Coffee enthusiast', 'bob', 'bob', 2),
    (3, 'notes-3.txt', 'Notes 3', 'Site administrator', 'Site administrator', 'admin', 'admin', 3)
ON CONFLICT DO NOTHING;

INSERT INTO resources (id, owner) VALUES
    (1, 'alice'),
    (2, 'bob'),
    (3, 'admin')
ON CONFLICT DO NOTHING;

INSERT INTO published_files (id, folder, file_name) VALUES
    (1, 'public', 'handbook-1.pdf'),
    (2, 'public', 'handbook-2.pdf'),
    (3, 'public', 'handbook-3.pdf')
ON CONFLICT DO NOTHING;

INSERT INTO vault (owner, secret) VALUES
    ('alice', 'vault-alice-7f3a'),
    ('bob', 'vault-bob-7f3a'),
    ('admin', 'vault-admin-7f3a')
ON CONFLICT DO NOTHING;

INSERT INTO admin_reports (id, slug, body) VALUES
    (1, 'quarterly', 'Revenue by region'),
    (2, 'access-review', 'Privileged access review'),
    (3, 'payroll', 'Payroll run totals')
ON CONFLICT DO NOTHING;

INSERT INTO api_tokens (id, owner, user_name) VALUES
    (1, 'alice', 'alice'),
    (2, 'bob', 'bob'),
    (3, 'admin', 'admin')
ON CONFLICT DO NOTHING;

INSERT INTO articles (id, title) VALUES
    (1, 'Release notes'),
    (2, 'Getting started'),
    (3, 'Billing questions')
ON CONFLICT DO NOTHING;

INSERT INTO audit_events (id, action, created_at) VALUES
    (1, 'login', '2020-01-01 00:00:00'),
    (2, 'export', '2020-01-02 00:00:00')
ON CONFLICT DO NOTHING;

INSERT INTO audit_log (id, action, created_at) VALUES
    (1, 'login', '2020-01-01 00:00:00'),
    (2, 'export', '2020-01-02 00:00:00')
ON CONFLICT DO NOTHING;

INSERT INTO cache_entries (id, cache_key, value) VALUES
    (1, 'user_data', 'cached_value')
ON CONFLICT DO NOTHING;

INSERT INTO cache_index (id, cache_key) VALUES
    (1, 'user_data')
ON CONFLICT DO NOTHING;

INSERT INTO carts (id, order_id, total, status) VALUES
    (1, 1, 19.99, 'open'),
    (2, 2, 19.99, 'open'),
    (3, 3, 19.99, 'open')
ON CONFLICT DO NOTHING;

INSERT INTO catalog_items (id, sku, name, supplier_cost, tenant_id) VALUES
    (1, 'SKU-1001', 'Notebook', 2.10, 'acme'),
    (2, 'SKU-1002', 'Desk lamp', 11.40, 'acme'),
    (3, 'SKU-1003', 'Monitor arm', 52.00, 'globex')
ON CONFLICT DO NOTHING;

INSERT INTO checkout_state (id, token, order_id, total, status) VALUES
    (1, 'chk-alice', 1, 19.99, 'open'),
    (2, 'chk-bob', 2, 19.99, 'open'),
    (3, 'chk-admin', 3, 19.99, 'open')
ON CONFLICT DO NOTHING;

INSERT INTO checkouts (id, order_id, customer_id) VALUES
    (1, 1, 'alice'),
    (2, 2, 'bob'),
    (3, 3, 'admin')
ON CONFLICT DO NOTHING;

INSERT INTO daily_totals (id, period, total) VALUES
    (1, '2024-01-01', 1520.00),
    (2, '2024-01-02', 980.50)
ON CONFLICT DO NOTHING;

INSERT INTO device_tokens (id, device_id, owner, user_id, token_hash, token_sha256) VALUES
    (1, 'device-1', 'alice', 'alice', 'a3b34856112bf426a7cd76174e4c5f2cdc67d8d14312e9c3c0e4fd2ffb956598', 'a3b34856112bf426a7cd76174e4c5f2cdc67d8d14312e9c3c0e4fd2ffb956598'),
    (2, 'device-2', 'bob', 'bob', 'f9f4232967876f4e442bc8887e04b7488cc6c12185c1f1bba534e12cc11df8f8', 'f9f4232967876f4e442bc8887e04b7488cc6c12185c1f1bba534e12cc11df8f8'),
    (3, 'device-3', 'admin', 'admin', '88683f43c95aa20327e6f431a31c5ad7554c7206f479bb0b5dc3eb12675815e1', '88683f43c95aa20327e6f431a31c5ad7554c7206f479bb0b5dc3eb12675815e1')
ON CONFLICT DO NOTHING;

INSERT INTO devices (id, user_id, token_hash, totp_code) VALUES
    (1, 'alice', 'a3b34856112bf426a7cd76174e4c5f2cdc67d8d14312e9c3c0e4fd2ffb956598', '401111'),
    (2, 'bob', 'f9f4232967876f4e442bc8887e04b7488cc6c12185c1f1bba534e12cc11df8f8', '402222'),
    (3, 'admin', '88683f43c95aa20327e6f431a31c5ad7554c7206f479bb0b5dc3eb12675815e1', '403333')
ON CONFLICT DO NOTHING;

INSERT INTO disputes (id, account) VALUES
    (1, 'alice'),
    (2, 'bob'),
    (3, 'admin')
ON CONFLICT DO NOTHING;

INSERT INTO exports (id, name, owner, path, details) VALUES
    (1, 'export-1.csv', 'alice', '/var/lib/app/exports/export-1.csv', 'rows=120'),
    (2, 'export-2.csv', 'bob', '/var/lib/app/exports/export-2.csv', 'rows=120'),
    (3, 'export-3.csv', 'admin', '/var/lib/app/exports/export-3.csv', 'rows=120')
ON CONFLICT DO NOTHING;

INSERT INTO feature_flags (id, name, enabled) VALUES
    (1, 'public_signup', TRUE),
    (2, 'beta_dashboard', FALSE)
ON CONFLICT DO NOTHING;

INSERT INTO invite_tokens (id, owner, token) VALUES
    (1, 'admin', 1000)
ON CONFLICT DO NOTHING;

INSERT INTO invoices (id, invoice_id, number, customer_ref, tenant_id, status, total, total_cents) VALUES
    (1, 1, 'INV-1001', 'cust-alice', 'acme', 'open', 120.00, 12000),
    (2, 2, 'INV-1002', 'cust-bob', 'globex', 'open', 120.00, 12000),
    (3, 3, 'INV-1003', 'cust-admin', 'acme', 'open', 120.00, 12000)
ON CONFLICT DO NOTHING;

INSERT INTO items (id, sku, name) VALUES
    (1, 'SKU-1001', 'Notebook'),
    (2, 'SKU-1002', 'Desk lamp'),
    (3, 'SKU-1003', 'Monitor arm')
ON CONFLICT DO NOTHING;

INSERT INTO jobs (id, job_id, name, owner, owner_id, state) VALUES
    (1, 1, 'nightly-alice', 'alice', 'alice', 'queued'),
    (2, 2, 'nightly-bob', 'bob', 'bob', 'queued'),
    (3, 3, 'nightly-admin', 'admin', 'admin', 'queued')
ON CONFLICT DO NOTHING;

INSERT INTO login_challenges (id, user_id, user_name, otp_code, password_verified) VALUES
    (1, '1', 'alice', '401111', FALSE),
    (2, '2', 'bob', '402222', FALSE),
    (3, '3', 'admin', '403333', FALSE)
ON CONFLICT DO NOTHING;

INSERT INTO mfa_challenges (id, user_id, code, expires_at) VALUES
    (1, '1', '401111', '2099-12-31 23:59:59'),
    (2, '2', '402222', '2099-12-31 23:59:59'),
    (3, '3', '403333', '2099-12-31 23:59:59')
ON CONFLICT DO NOTHING;

INSERT INTO orders (id, order_id, user_id, customer_id, owner, sku, quantity, total, total_cents, status) VALUES
    (1, 1, 1, 'alice', 'alice', 'SKU-1001', 1, 4.50, 450, 'open'),
    (2, 2, 2, 'bob', 'bob', 'SKU-1001', 1, 4.50, 450, 'open'),
    (3, 3, 3, 'admin', 'admin', 'SKU-1001', 1, 4.50, 450, 'open')
ON CONFLICT DO NOTHING;

INSERT INTO password_resets (id, user_id, user_name, name, account, token_hash, token_sha256, expires_at) VALUES
    (1, '1', 'alice', 'alice', 'alice', '17af8cff71098ff048b42d40d8204e4422cf3d8247570e380fa4b0ef26b0a44c', '17af8cff71098ff048b42d40d8204e4422cf3d8247570e380fa4b0ef26b0a44c', 4102444800000),
    (2, '2', 'bob', 'bob', 'bob', 'a8c7dee792f15eccf147c6c00c3c84a2a36057624659cd1fe58a593a664b25c2', 'a8c7dee792f15eccf147c6c00c3c84a2a36057624659cd1fe58a593a664b25c2', 4102444800000),
    (3, '3', 'admin', 'admin', 'admin', '1d9bb8944ba64227fbc8697249f5bc3cb38cae967be88d9b7b2698feba9b2f28', '1d9bb8944ba64227fbc8697249f5bc3cb38cae967be88d9b7b2698feba9b2f28', 4102444800000)
ON CONFLICT DO NOTHING;

INSERT INTO pricing (id, sku, tenant_id, unit_cost) VALUES
    (1, 'SKU-1001', 'acme', 2.10),
    (2, 'SKU-1002', 'acme', 11.40),
    (3, 'SKU-1003', 'globex', 52.00)
ON CONFLICT DO NOTHING;

INSERT INTO projects (id, tenant_id, name) VALUES
    (1, 'acme', 'Project Alice'),
    (2, 'globex', 'Project Bob'),
    (3, 'acme', 'Project Admin')
ON CONFLICT DO NOTHING;

INSERT INTO recovery_answers (id, account, answer) VALUES
    (1, 'alice', 'harbor-1'),
    (2, 'bob', 'harbor-2'),
    (3, 'admin', 'harbor-3')
ON CONFLICT DO NOTHING;

INSERT INTO refunds (id, requested_by, state) VALUES
    (1, 'alice', 'pending'),
    (2, 'bob', 'pending'),
    (3, 'admin', 'pending')
ON CONFLICT DO NOTHING;

INSERT INTO reviews (id, review_id, author_id, review_text, rating) VALUES
    (1, 1, 1, 'Great write-up', 4),
    (2, 2, 2, 'Thanks for sharing', 4),
    (3, 3, 3, 'Pinned by the moderators', 4)
ON CONFLICT DO NOTHING;

INSERT INTO settings (id, maintenance_mode) VALUES
    (1, FALSE)
ON CONFLICT DO NOTHING;

INSERT INTO signing_keys (id, key_id, retired) VALUES
    (1, '2024-q1', FALSE)
ON CONFLICT DO NOTHING;

INSERT INTO subscriptions (id, subscription_id, status) VALUES
    (1, 'sub-1001', 'active'),
    (2, 'sub-1002', 'active'),
    (3, 'sub-1003', 'active')
ON CONFLICT DO NOTHING;

INSERT INTO transfers (id, account_id, amount, status, state) VALUES
    (1, 'alice', 250.00, 'pending', 'held_for_limit'),
    (2, 'bob', 250.00, 'pending', 'held_for_limit'),
    (3, 'admin', 250.00, 'pending', 'held_for_limit')
ON CONFLICT DO NOTHING;

INSERT INTO user_grants (id, user_id, name, permissions) VALUES
    (1, 'alice', 'alice', 'read'),
    (2, 'bob', 'bob', 'read'),
    (3, 'admin', 'admin', 'read,export,admin')
ON CONFLICT DO NOTHING;

INSERT INTO vault_entries (id, owner, secret) VALUES
    (1, 'alice', 'vault-alice-7f3a'),
    (2, 'bob', 'vault-bob-7f3a'),
    (3, 'admin', 'vault-admin-7f3a')
ON CONFLICT DO NOTHING;
"""


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.executescript(_SCHEMA)
    return conn


class _Column:
    """One mapped column. Comparing it yields a ``(predicate, value)`` pair."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other: Any) -> Any:
        return (f"{self.name} = ?", other)


class _Manager:
    """Django-style ``.objects`` query manager over the same sqlite the mapped
    columns use."""

    def __init__(self, conn: sqlite3.Connection, model: Any) -> None:
        self._conn = conn
        self._model = model
        self._clauses: list = []
        self._params: list = []

    def filter(self, **predicates: Any) -> "_Manager":
        for col, value in predicates.items():
            self._clauses.append(f"{col} = ?")
            self._params.append(value)
        return self

    def all(self) -> list:
        sql = f"SELECT * FROM {self._model.__tablename__}"
        if self._clauses:
            sql += " WHERE " + " AND ".join(self._clauses)
        return self._conn.execute(sql, tuple(self._params)).fetchall()

    def first(self) -> Any:
        rows = self.all()
        return rows[0] if rows else None

    def raw(self, sql: str, params: Any = ()) -> list:
        return self._conn.execute(sql, params).fetchall()


class _ObjectsDescriptor:
    def __get__(self, instance: Any, owner: Any) -> "_Manager":
        return _Manager(db._conn, owner)


class User:
    __tablename__ = "users"

    id = _Column("id")
    name = _Column("name")
    objects = _ObjectsDescriptor()


class _Query:
    def __init__(self, conn: sqlite3.Connection, model: Any) -> None:
        self._conn = conn
        self._model = model
        self._clauses: list = []
        self._params: list = []

    def filter(self, *predicates: Any) -> "_Query":
        for clause, value in predicates:
            self._clauses.append(clause)
            self._params.append(value)
        return self

    def all(self) -> list:
        sql = f"SELECT * FROM {self._model.__tablename__}"
        if self._clauses:
            sql += " WHERE " + " AND ".join(self._clauses)
        return self._conn.execute(sql, tuple(self._params)).fetchall()

    def first(self) -> Any:
        rows = self.all()
        return rows[0] if rows else None


class _Session:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self._conn = conn

    def query(self, model: Any) -> _Query:
        return _Query(self._conn, model)


class Database:
    """Thin wrapper over the connection. execute() keeps the DB-API shape the
    handlers already use, so the call sites are unchanged."""

    def __init__(self) -> None:
        self._conn = _connect()

    def execute(self, sql: str, params: Any = ()) -> sqlite3.Cursor:
        cursor = self._conn.execute(sql.replace("%s", "?"), params)
        self._conn.commit()
        return cursor

    def fetch_one(self, sql: str, params: Any = ()) -> Any:
        return self.execute(sql, params).fetchone()

    @property
    def session(self) -> _Session:
        return _Session(self._conn)


db = Database()


PASSWORD_ITERATIONS = 600000


def hash_password(password: str) -> str:
    salt = os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, PASSWORD_ITERATIONS)
    return f"pbkdf2_sha256${PASSWORD_ITERATIONS}${salt.hex()}${digest.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        _scheme, iterations, salt_hex, digest_hex = stored.split("$")
    except ValueError:
        return False
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt_hex), int(iterations))
    return hmac.compare_digest(digest.hex(), digest_hex)


def auth_check(principal: Any, credential: str) -> bool:
    """True when credential is the principal's password, or the role its account holds."""
    name = str(principal)
    row = db.fetch_one("SELECT password_hash FROM credentials WHERE username = ?", (name,))
    if row is not None and verify_password(str(credential), row["password_hash"]):
        return True
    account = db.fetch_one("SELECT role, locked FROM users WHERE name = ?", (name,))
    return account is not None and not account["locked"] and account["role"] == str(credential)


class _ExternalService:
    """Parameter-store / RPC stand-in: attribute access, call and subscript all
    return self, so an ssm_client.get_parameter(...) or rpc_stub.method(...) in a
    handler resolves without a live backend, the same way the db/broker stubs do."""

    def __call__(self, *args: Any, **kwargs: Any) -> "_ExternalService":
        return self

    def __getattr__(self, _name: str) -> "_ExternalService":
        return self

    def __getitem__(self, _key: Any) -> "_ExternalService":
        return self


ssm_client = _ExternalService()
rpc_stub = _ExternalService()
