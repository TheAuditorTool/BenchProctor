# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "base64"
require "shellwords"
require "open3"

class BenchmarkTest00009Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00009
    user_input = request.body.read
    data = Base64.decode64(user_input)
    processed = Shellwords.escape(data)
    Open3.capture2e("echo " + processed)
    render json: { status: "ok" }
  end
end
