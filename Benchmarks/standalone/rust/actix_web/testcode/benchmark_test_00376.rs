// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use futures_util::StreamExt;

#[actix_web::post("/benchmark_test_00376")]
pub async fn benchmark_test_00376(mut payload: actix_multipart::Multipart) -> HttpResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Some(Ok(_field)) = payload.next().await {
            if let Some(_cd) = _field.content_disposition() {
                if let Some(_f) = _cd.get_filename() { _fname = _f.to_string(); break; }
            }
        }
        _fname
    };
    let mut data = String::new();
    for token in upload_name.split(',') { data = token.to_string(); }
    crate::shared::db_query_bind_named("SELECT * FROM users WHERE id = :id", &data);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
