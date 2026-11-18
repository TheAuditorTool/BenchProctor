# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00554Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00554
    user_input = params.require(:upload_form).permit(:upload)[:upload].original_filename.to_s
    if user_input.to_s.empty?
      data = ''
    else
      data = user_input
    end
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
