# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "cgi/escape"

class BenchmarkTest00232Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00232
    user_input = request.referer.to_s
    data = CGI.unescape(user_input)
    unless data =~ /\A[a-zA-Z0-9_.#\-]+\z/
      render json: { error: "invalid" }, status: 400
      return
    end
    processed = data
    User.find_by_sql("SELECT * FROM users WHERE id = '" + processed + "'")
    render json: { status: "ok" }
  end
end
