// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00288")]
pub async fn benchmark_test_00288() -> HttpResponse {
    let upload_name = crate::shared::uploaded_filename();
    struct FormData { payload: String }
    let data = FormData { payload: upload_name.clone() }.payload;
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", data)).await;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
