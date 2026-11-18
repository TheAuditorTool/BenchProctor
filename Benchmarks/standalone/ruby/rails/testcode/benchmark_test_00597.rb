# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00597Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00597
    user_input = request.query_parameters[:q].to_s
    tokens = user_input.split(',')
    data = tokens.join(' ')
    unless data =~ /\A(asc|desc|name|created)\z/
      render json: { error: "invalid" }, status: 400
      return
    end
    processed = data
    ActiveRecord::Base.connection.execute("SELECT * FROM users ORDER BY #{processed}")
    render json: { status: "ok" }
  end
end
