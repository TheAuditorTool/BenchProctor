// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use futures_util::StreamExt;

#[actix_web::post("/benchmark_test_00109")]
pub async fn benchmark_test_00109(mut payload: actix_multipart::Multipart) -> HttpResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Some(Ok(_field)) = payload.next().await {
            if let Some(_cd) = _field.content_disposition() {
                if let Some(_f) = _cd.get_filename() { _fname = _f.to_string(); break; }
            }
        }
        _fname
    };
    let _prefix: String = upload_name.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => upload_name.to_lowercase(),
        "f" => upload_name.to_uppercase(),
        _ => upload_name.trim().to_string(),
    };
    let at = data.find('@').unwrap();
    let mail_domain = &data[at + 1..];
    let _ = mail_domain;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
