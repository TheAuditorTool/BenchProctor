# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00174Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00174
    user_input = cookies[:session_token].to_s
    data = user_input.gsub("\u0000", "")
    plans = { "free" => { requests: 100 }, "team" => { requests: 5_000 } }
    plan = plans[data.to_s]
    return render json: { error: "not found" }, status: 404 if plan.nil?
    limit = plan.fetch(:requests)
    render json: { requests: limit }
  end
end
