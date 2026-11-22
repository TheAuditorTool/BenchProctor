# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00189Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00189
    user_input = File.read("/var/app/data.txt")
    data = [user_input].pack("H*").force_encoding("UTF-8") rescue user_input
    _coerced = Integer(data, exception: false).to_s
    parsed_id = _coerced
    ActiveRecord::Base.connection.exec_query("SELECT * FROM users WHERE id = '" + parsed_id + "'", "SQL", [], prepare: true)
    render json: { status: "ok" }
  end
end
