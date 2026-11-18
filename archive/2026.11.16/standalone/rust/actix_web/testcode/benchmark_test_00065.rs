// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use futures_util::StreamExt;

#[actix_web::post("/benchmark_test_00065")]
pub async fn benchmark_test_00065(mut payload: actix_multipart::Multipart) -> HttpResponse {
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
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(multipart_value.clone());
    let _coerced = data.parse::<f64>().unwrap_or(0.0);
    let processed = _coerced.to_string();
    crate::shared::store_session("data", &processed);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
