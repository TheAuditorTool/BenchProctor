// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use futures_util::StreamExt;

#[actix_web::post("/benchmark_test_00070")]
pub async fn benchmark_test_00070(req: HttpRequest, mut payload: actix_multipart::Multipart) -> HttpResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Some(Ok(_field)) = payload.next().await {
            if let Some(_cd) = _field.content_disposition() {
                if let Some(_f) = _cd.get_filename() { _fname = _f.to_string(); break; }
            }
        }
        _fname
    };
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", upload_name).ok();
    use actix_web::Responder;
    actix_web::web::Redirect::to(data.clone()).respond_to(&req).map_into_boxed_body()
}
