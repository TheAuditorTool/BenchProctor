// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00254() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = comment_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    if let Ok(_pkg) = sxd_document::parser::parse("<users><user id='1' role='admin'/><user id='2' role='member'/></users>") {
        let _ = sxd_xpath::evaluate_xpath(&_pkg.as_document(), &format!("count(//user[@role='{}'])", data));
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
