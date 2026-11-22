# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00243Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00243
    user_input = params.require(:request_data).permit(:payload)[:payload].to_s
    record = { payload: user_input.to_s }
    data = record.fetch(:payload)
    match = data.to_s.match(/\A(?<user>[\w.+-]+)@(?<domain>[\w-]+(?:\.[\w-]+)+)\z/)
    domain = match[:domain].downcase
    render json: { domain: domain }
  end
end
