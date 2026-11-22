// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;

pub async fn benchmark_test_00180() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = comment_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    let parser = pulldown_cmark::Parser::new(&data);
    let mut md_rendered = String::new();
    pulldown_cmark::html::push_html(&mut md_rendered, parser);
    let processed = ammonia::clean(&md_rendered);
    let mut _env = minijinja::Environment::new();
    _env.add_template("profile.html", "<div class=\"profile-bio\">{{ bio|safe }}</div>").ok();
    let _page = _env.get_template("profile.html").and_then(|t| t.render(minijinja::context! { bio => processed })).unwrap_or_default();
    return ([("content-type", "text/html")], _page).into_response();
}
