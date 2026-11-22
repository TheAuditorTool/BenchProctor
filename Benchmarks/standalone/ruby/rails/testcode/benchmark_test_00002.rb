# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "redcarpet"

class BenchmarkTest00002Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00002
    user_input = request.body.read
    data = JSON.parse(user_input)["value"] rescue ""
    processed = Redcarpet::Markdown.new(Redcarpet::Render::HTML.new(filter_html: true, no_styles: true, safe_links_only: true)).render(data)
    send_data("<div>" + processed + "</div>", type: "text/html", disposition: "inline")
  end
end
