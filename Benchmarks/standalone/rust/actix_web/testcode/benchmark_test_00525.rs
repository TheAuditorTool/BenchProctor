// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use futures_util::StreamExt;
use rand::rngs::OsRng;

#[actix_web::post("/benchmark_test_00525")]
pub async fn benchmark_test_00525(mut payload: actix_multipart::Multipart) -> HttpResponse {
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
    let data = multipart_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
