// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use futures_util::StreamExt;

#[actix_web::post("/benchmark_test_00033")]
pub async fn benchmark_test_00033(mut payload: actix_multipart::Multipart) -> HttpResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Some(Ok(_field)) = payload.next().await {
            if let Some(_cd) = _field.content_disposition() {
                if let Some(_f) = _cd.get_filename() { _fname = _f.to_string(); break; }
            }
        }
        _fname
    };
    let captured = upload_name.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.#~\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    tokio::fs::write(format!("/var/app/data/{}", processed), "data").await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
