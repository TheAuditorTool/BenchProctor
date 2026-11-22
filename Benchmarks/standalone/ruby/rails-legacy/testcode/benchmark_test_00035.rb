# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "securerandom"

class BenchmarkTest00035Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00035
    user_input = params.require(:multipart_data).permit(:multipart_field)[:multipart_field].to_s
    tokens = user_input.split(',')
    data = tokens.join(' ')
    token = SecureRandom.random_bytes(16).unpack1("H*")
    ActiveRecord::Base.connection.exec_insert(ActiveRecord::Base.sanitize_sql_array(["INSERT INTO reset_tokens (account, token) VALUES (?, ?)", data.to_s, token]))
    render json: { reset: "sent" }
  end
end
