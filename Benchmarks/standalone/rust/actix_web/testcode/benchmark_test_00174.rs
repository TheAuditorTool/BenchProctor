// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00174")]
pub async fn benchmark_test_00174(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let data: String = user_id.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| user_id.clone());
    let _ciphertext = crate::shared::encrypt(&data);
    tokio::fs::write("/var/data/cipher.bin", _ciphertext.as_bytes()).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
