// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00034")]
pub async fn benchmark_test_00034() -> HttpResponse {
    let msg_value = crate::shared::queue_get_message("app-events");
    let data = msg_value.replace("\t", " ");
    reqwest::get(&data).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
