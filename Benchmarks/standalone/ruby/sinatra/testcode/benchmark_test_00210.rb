# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "redcarpet"

class BenchmarkTest00210 < Sinatra::Base
  before do
    halt 413 if request.content_length.to_i > 1_000_000
  end
  after do
    headers["X-Content-Type-Options"] = "nosniff"
  end

  error StandardError do
    content_type :json
    status 500
    JSON.generate({ error: "internal" })
  end
  post "/benchmark_test_00210" do
    user_input = params[:field].to_s
    data = sprintf("%s", user_input)
    processed = Redcarpet::Markdown.new(Redcarpet::Render::HTML.new(filter_html: true, no_styles: true, safe_links_only: true)).render(data)
    content_type :html
    "<div>" + processed + "</div>"
  end
end
