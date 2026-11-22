// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00109(headers: HeaderMap) -> impl IntoResponse {
    let header_value = headers.get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data: String = header_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| header_value.clone());
    let _coerced = data.parse::<f64>().unwrap_or(0.0);
    let processed = _coerced.to_string();
    if let Ok(_pkg) = sxd_document::parser::parse("<users><user id='1' role='admin'/><user id='2' role='member'/></users>") {
        let _ = sxd_xpath::evaluate_xpath(&_pkg.as_document(), &format!("count(//user[@role='{}'])", processed));
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
