# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00043Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00043
    user_input = Comment.first&.text.to_s
    record = { payload: user_input.to_s }
    data = record.fetch(:payload)
    result = User.find_by(name: data)
    return render json: { error: "not found" }, status: 404 if result.nil?
    value = result.name
    render json: { status: "ok" }
  end
end
