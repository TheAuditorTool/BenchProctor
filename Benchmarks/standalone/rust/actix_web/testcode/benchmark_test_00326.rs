// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00326/{id}")]
pub async fn benchmark_test_00326(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let data = match path_value.chars().next() { Some(_) => path_value.clone(), None => "default".to_string() };
    let _ciphertext = crate::shared::encrypt(&data);
    tokio::fs::write("/var/data/cipher.bin", _ciphertext.as_bytes()).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
