# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "cgi"
require "yaml"

class BenchmarkTest00514Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00514
    user_input = request.query_parameters[:q].to_s
    data = CGI.unescape(user_input)
    YAML.safe_load(data)
    render json: { status: "ok" }
  end
end
