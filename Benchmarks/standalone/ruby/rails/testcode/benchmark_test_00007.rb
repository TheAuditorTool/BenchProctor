# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00007Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00007
    user_input = params.require(:upload_form).permit(:upload)[:upload].original_filename.to_s
    data = user_input.gsub("\u0000", "")
    prng = Random.new
    token = prng.bytes(16).unpack1("H*")
    ActiveRecord::Base.connection.exec_insert(ActiveRecord::Base.sanitize_sql_array(["INSERT INTO reset_tokens (account, token) VALUES (?, ?)", data.to_s, token]))
    render json: { reset: "sent" }
  end
end
