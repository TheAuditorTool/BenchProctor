# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "redcarpet"

class BenchmarkTest00010Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00010
    user_input = params.require(:user).permit(:name)[:name].to_s
    data = sprintf("%s", user_input)
    processed = Redcarpet::Markdown.new(Redcarpet::Render::HTML.new(filter_html: true, no_styles: true, safe_links_only: true)).render(data)
    render html: ("<div>" + processed + "</div>").html_safe
  end
end
