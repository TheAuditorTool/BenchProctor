// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00199() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let (payload, _origin) = (comment_value.clone(), "http");
    let data = payload;
    let _profile = std::collections::BTreeMap::from([("display_name".to_string(), data.clone()), ("profile_complete".to_string(), "true".to_string())]);
    if let Ok(mut _session) = crate::shared::SESSION_STORE.lock() {
        _session.extend(_profile);
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
