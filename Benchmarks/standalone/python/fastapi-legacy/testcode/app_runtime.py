"""This application's own runtime: its store, its helpers and its RPC bridge.

Every third-party CLIENT a handler talks to is bound in the module that uses it,
from that library's own constructor. What is left here is what belongs to the
application rather than to a package: the seeded database and its mapped user,
the credential helpers, and the two gRPC functions that carry a call.
"""
import hashlib
import hmac
import os
import sqlite3
from typing import Any

import grpc

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


_GRPC_INBOX: dict[str, str] = {}


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


def grpc_call(target: str, method: str, payload: str) -> str:
    """One unary RPC to target, returning the peer's response.

    Raw bytes rather than generated stubs: the message is a single string, so a
    protoc step and thousands of lines of machine output would buy nothing that
    str.encode does not.
    """
    with grpc.insecure_channel(target) as channel:
        rpc = channel.unary_unary(method, request_serializer=str.encode, response_deserializer=bytes.decode)
        return rpc(payload)


def grpc_inbox(method: str) -> str:
    """Payload the most recent call to method delivered, or an empty string."""
    return _GRPC_INBOX.get(method, "")
