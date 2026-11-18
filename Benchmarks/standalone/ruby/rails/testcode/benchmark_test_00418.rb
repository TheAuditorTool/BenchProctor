# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00418Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00418
    user_input = request.referer.to_s
    resolved = File.realpath(File.join("/var/app/data", user_input)) rescue nil
    unless resolved && (resolved == "/var/app/data" || resolved.start_with?("/var/app/data/"))
      render json: { error: "forbidden" }, status: 403
      return
    end
    checked_path = resolved
    File.delete(checked_path)
    render json: { status: "ok" }
  end
end
