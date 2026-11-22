// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00135")]
pub async fn benchmark_test_00135() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let (payload, _origin) = (comment_value.clone(), "http");
    let data = payload;
    let _profile = std::collections::BTreeMap::from([("display_name".to_string(), data.clone()), ("profile_complete".to_string(), "true".to_string())]);
    if let Ok(mut _session) = crate::shared::SESSION_STORE.lock() {
        _session.extend(_profile);
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
