# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00057Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00057
    user_input = params[:id].to_s
    data = "#{user_input}"
    match = data.to_s.match(/\A(?<user>[\w.+-]+)@(?<domain>[\w-]+(?:\.[\w-]+)+)\z/)
    return render json: { error: "not found" }, status: 404 if match.nil?
    domain = match[:domain].downcase
    render json: { domain: domain }
  end
end
