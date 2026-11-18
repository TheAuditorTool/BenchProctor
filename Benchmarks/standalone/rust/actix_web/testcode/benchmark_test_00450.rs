// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use futures_util::StreamExt;

#[actix_web::post("/benchmark_test_00450")]
pub async fn benchmark_test_00450(mut payload: actix_multipart::Multipart) -> HttpResponse {
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
    crate::shared::set_cookie(&format!("session={}; HttpOnly; SameSite=Strict", multipart_value));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
