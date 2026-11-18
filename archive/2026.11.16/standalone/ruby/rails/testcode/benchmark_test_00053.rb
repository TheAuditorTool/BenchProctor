# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00053Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00053
    user_input = params.require(:user).permit(:name)[:name].to_s
    def _normalize_local(v)
      v.to_s.strip
    end
    data = _normalize_local(user_input)
    result = User.find_by(name: data)
    return render json: { error: "not found" }, status: 404 if result.nil?
    value = result.name
    render json: { status: "ok" }
  end
end
