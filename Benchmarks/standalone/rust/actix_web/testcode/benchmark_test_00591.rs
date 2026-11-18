// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use futures_util::StreamExt;

#[actix_web::post("/benchmark_test_00591")]
pub async fn benchmark_test_00591(mut payload: actix_multipart::Multipart) -> HttpResponse {
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
    let _prefix: String = multipart_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => multipart_value.to_lowercase(),
        "f" => multipart_value.to_uppercase(),
        _ => multipart_value.trim().to_string(),
    };
    crate::shared::store_session("data", &data);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
