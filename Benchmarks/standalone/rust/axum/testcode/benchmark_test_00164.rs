// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00164(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Ok(Some(_field)) = multipart.next_field().await {
            if let Some(_f) = _field.file_name() { _fname = _f.to_string(); break; }
        }
        _fname
    };
    let data = upload_name.replace("\t", " ");
    use diesel::prelude::*;
    if let Ok(mut conn) = diesel::SqliteConnection::establish(":memory:") {
        let _ = crate::shared::users::table.filter(crate::shared::users::name.eq(data.as_str())).load::<(i32, String)>(&mut conn);
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
