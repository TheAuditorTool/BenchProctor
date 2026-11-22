# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00295Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00295
    user_input = Profile.first&.bio.to_s
    unless user_input =~ /\A(asc|desc|name|created)\z/
      render json: { error: "invalid" }, status: 400
      return
    end
    processed = user_input
    ActiveRecord::Base.connection.exec_query("SELECT * FROM users ORDER BY #{processed}", "SQL", [], prepare: true)
    render json: { status: "ok" }
  end
end
