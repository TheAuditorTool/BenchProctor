// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00092(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let multipart_value = {
        let mut _mv = String::new();
        if let Ok(Some(_field)) = multipart.next_field().await {
            _mv = _field.text().await.unwrap_or_default();
        }
        _mv
    };
    let data = urlencoding::decode(&multipart_value).unwrap_or_default().to_string();
    if let Ok(_pkg) = sxd_document::parser::parse("<users><user id='1' role='admin'/><user id='2' role='member'/></users>") {
        let _doc = _pkg.as_document();
        let _factory = sxd_xpath::Factory::new();
        if let Ok(Some(_xpath)) = _factory.build(&format!("//user[@id='{}']/@role", data)) {
            let _ = _xpath.evaluate(&sxd_xpath::Context::new(), _doc.root());
        }
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
