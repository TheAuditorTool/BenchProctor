// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use futures_util::StreamExt;

#[actix_web::post("/benchmark_test_00423")]
pub async fn benchmark_test_00423(mut payload: actix_multipart::Multipart) -> HttpResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Some(Ok(_field)) = payload.next().await {
            if let Some(_cd) = _field.content_disposition() {
                if let Some(_f) = _cd.get_filename() { _fname = _f.to_string(); break; }
            }
        }
        _fname
    };
    let data = upload_name.replace("\t", " ");
    use diesel::prelude::*;
    if let Ok(mut conn) = diesel::SqliteConnection::establish(":memory:") {
        let _ = crate::shared::users::table.filter(crate::shared::users::name.eq(data.as_str())).load::<(i32, String)>(&mut conn);
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
