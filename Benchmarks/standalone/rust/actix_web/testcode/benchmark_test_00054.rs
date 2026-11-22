// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00054")]
pub async fn benchmark_test_00054(body: web::Bytes) -> HttpResponse {
    let json_value = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("payload").and_then(|p| p.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let transform = |v: String| v.trim().to_string();
    let data = transform(json_value.clone());
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    let _profile = std::collections::BTreeMap::from([("display_name".to_string(), processed.clone()), ("profile_complete".to_string(), "true".to_string())]);
    if let Ok(mut _session) = crate::shared::SESSION_STORE.lock() {
        _session.extend(_profile);
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
