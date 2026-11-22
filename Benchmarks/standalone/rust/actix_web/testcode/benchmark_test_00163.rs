// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00163")]
pub async fn benchmark_test_00163(body: web::Bytes) -> HttpResponse {
    let json_value = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("payload").and_then(|p| p.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let (payload, _origin) = (json_value.clone(), "http");
    let data = payload;
    let _profile = std::collections::BTreeMap::from([("display_name".to_string(), data.clone()), ("profile_complete".to_string(), "true".to_string())]);
    if let Ok(mut _session) = crate::shared::SESSION_STORE.lock() {
        _session.extend(_profile);
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
