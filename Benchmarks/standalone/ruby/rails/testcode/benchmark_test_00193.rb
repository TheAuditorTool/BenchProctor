# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00193Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00193
    user_input = params.require(:request_data).permit(:payload)[:payload].to_s
    data = JSON.parse(user_input)["value"] rescue ""
    result = User.find_by(name: data)
    value = result.name
    render json: { status: "ok" }
  end
end
