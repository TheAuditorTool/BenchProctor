# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00196Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00196
    user_input = params.require(:user).permit(:name)[:name].to_s
    data = format("%<value>s", value: user_input)
    session.update(display_name: data.to_s, updated_at: Time.now.to_i)
    render json: { status: "ok" }
  end
end
