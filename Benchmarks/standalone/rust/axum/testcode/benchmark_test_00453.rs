// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;

pub async fn benchmark_test_00453(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let multipart_value = {
        let mut _mv = String::new();
        if let Ok(Some(_field)) = multipart.next_field().await {
            _mv = _field.text().await.unwrap_or_default();
        }
        _mv
    };
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(multipart_value.clone());
    axum::response::Redirect::to(data.as_str()).into_response()
}
