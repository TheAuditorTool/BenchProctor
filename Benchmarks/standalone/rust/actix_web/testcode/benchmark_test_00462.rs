// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use futures_util::StreamExt;

#[actix_web::post("/benchmark_test_00462")]
pub async fn benchmark_test_00462(mut payload: actix_multipart::Multipart) -> HttpResponse {
    let multipart_value = {
        let mut _mv = String::new();
        if let Some(Ok(mut _field)) = payload.next().await {
            let mut _buf: Vec<u8> = Vec::new();
            while let Some(Ok(_chunk)) = _field.next().await {
                _buf.extend_from_slice(&_chunk);
            }
            _mv = String::from_utf8_lossy(&_buf).to_string();
        }
        _mv
    };
    let data = match multipart_value.chars().next() { Some(_) => multipart_value.clone(), None => "default".to_string() };
    tokio::fs::remove_file(format!("/var/app/data/{}", data)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
