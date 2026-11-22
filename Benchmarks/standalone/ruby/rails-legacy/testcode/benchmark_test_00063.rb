# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "cgi"

class BenchmarkTest00063Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00063
    user_input = request.query_parameters[:q].to_s
    begin
      data = JSON.parse(user_input)['value'] || user_input
    rescue JSON::ParserError
      data = user_input
    end
    cookie_value = CGI.escape(data.to_s)
    response.set_header("Set-Cookie", "session=" + cookie_value + "; Path=/; Secure; HttpOnly; SameSite=Strict")
    render json: { status: "ok" }
  end
end
