# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00099Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00099
    user_input = params.require(:request_data).permit(:payload)[:payload].to_s
    data = user_input ? user_input : ''
    unless data =~ /\A[a-zA-Z0-9 _.%\-]+\z/
      render json: { error: "invalid" }, status: 400
      return
    end
    processed = data
    IO.popen(["sh", "-c", "echo " + processed], &:read)
    render json: { status: "ok" }
  end
end
