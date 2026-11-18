# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00159Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00159
    user_input = request.params["file"].original_filename.to_s
    pending = user_input.split(',')
    data = ''
    data = pending.shift until pending.empty?
    resolved = File.realpath(File.join("/var/app/data", data)) rescue nil
    unless resolved && (resolved == "/var/app/data" || resolved.start_with?("/var/app/data/"))
      render json: { error: "forbidden" }, status: 403
      return
    end
    checked_path = resolved
    content = File.read(checked_path)
    render json: { status: "ok" }
  end
end
