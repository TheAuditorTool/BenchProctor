// SPDX-License-Identifier: Apache-2.0
use axum::extract::Query;
use axum::response::IntoResponse;
use std::collections::HashMap;

pub async fn benchmark_test_00214(Query(params): Query<HashMap<String, String>>) -> impl IntoResponse {
    let user_id = params.get("id").cloned().unwrap_or_default();
    struct FormData { payload: String }
    let data = FormData { payload: user_id.clone() }.payload;
    axum::response::Redirect::temporary(data.as_str()).into_response()
}
