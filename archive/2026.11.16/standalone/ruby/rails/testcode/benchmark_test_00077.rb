# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00077Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00077
    user_input = cookies[:session_token].to_s
    data = [user_input].pack("H*").force_encoding("UTF-8") rescue user_input
    resolved = File.realpath(File.join("/var/app/data", data)) rescue nil
    unless resolved && (resolved == "/var/app/data" || resolved.start_with?("/var/app/data/"))
      render json: { error: "forbidden" }, status: 403
      return
    end
    checked_path = resolved
    File.write(checked_path, "data")
    render json: { status: "ok" }
  end
end
