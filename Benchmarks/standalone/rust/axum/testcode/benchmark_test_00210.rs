// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00210() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = db_value.to_string();
    if let Ok(_pkg) = sxd_document::parser::parse("<users><user id='1' role='admin'/><user id='2' role='member'/></users>") {
        let _ = sxd_xpath::evaluate_xpath(&_pkg.as_document(), &format!("count(//user[@role='{}'])", data));
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
