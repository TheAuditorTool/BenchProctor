// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00579")]
pub async fn benchmark_test_00579() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let _prefix: String = comment_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => comment_value.to_lowercase(),
        "f" => comment_value.to_uppercase(),
        _ => comment_value.trim().to_string(),
    };
    use sha2::Digest;
    let _ = sha2::Sha256::digest(data.as_bytes());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
