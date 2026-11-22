// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00024")]
pub async fn benchmark_test_00024() -> HttpResponse {
    let upload_name = crate::shared::uploaded_filename();
    let data = upload_name.to_string();
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", data)).await;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
