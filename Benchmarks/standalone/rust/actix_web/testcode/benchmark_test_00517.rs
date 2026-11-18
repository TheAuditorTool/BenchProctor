// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00517")]
pub async fn benchmark_test_00517() -> HttpResponse {
    let redis_value = redis::Client::open("redis://cache:6379").ok().and_then(|client| client.get_connection().ok()).and_then(|mut conn| redis::cmd("GET").arg("user_data").query::<String>(&mut conn).ok()).unwrap_or_default();
    let data = redis_value.replace("\t", " ");
    crate::shared::db_query_bind("SELECT * FROM users WHERE id = $1", &data);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
