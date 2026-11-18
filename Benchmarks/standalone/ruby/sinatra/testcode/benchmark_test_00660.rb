# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "redcarpet"

class BenchmarkTest00660 < Sinatra::Base
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
  post "/benchmark_test_00660" do
    user_input = request.env["HTTP_USER_AGENT"].to_s
    data = ''
    user_input.split(',').each { |token| data = token }
    processed = Redcarpet::Markdown.new(Redcarpet::Render::HTML.new(filter_html: true, no_styles: true, safe_links_only: true)).render(data)
    content_type :html
    "<div>" + processed + "</div>"
  end
end
