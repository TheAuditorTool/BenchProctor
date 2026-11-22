// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00285")]
pub async fn benchmark_test_00285(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let data = urlencoding::decode(&field_value).unwrap_or_default().to_string();
    let _coerced = data.parse::<f64>().unwrap_or(0.0);
    let processed = _coerced.to_string();
    let _profile = std::collections::BTreeMap::from([("display_name".to_string(), processed.clone()), ("profile_complete".to_string(), "true".to_string())]);
    if let Ok(mut _session) = crate::shared::SESSION_STORE.lock() {
        _session.extend(_profile);
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
