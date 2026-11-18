// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use futures_util::StreamExt;

#[actix_web::post("/benchmark_test_00341")]
pub async fn benchmark_test_00341(mut payload: actix_multipart::Multipart) -> HttpResponse {
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
    let data = if multipart_value.len() <= 4096 { multipart_value.clone() } else { multipart_value.chars().take(4096).collect() };
    let requested: u32 = data.parse().unwrap_or(0);
    let count = (requested * 4096) as usize;
    let _buf: Vec<u8> = vec![0u8; count];
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
