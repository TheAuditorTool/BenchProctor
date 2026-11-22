# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00240Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00240
    user_input = Rails.application.config.app_value.to_s
    data = "%s" % user_input
    ActiveRecord::Base.connection.exec_query("SELECT * FROM users WHERE id = '" + data + "'", "SQL", [], prepare: true)
    render json: { status: "ok" }
  end
end
