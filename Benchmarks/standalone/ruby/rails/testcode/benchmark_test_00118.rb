# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00118Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00118
    user_input = params[:id].to_s
    data = user_input.split(/[ \t]+/).join(" ")
    ActiveRecord::Base.connection.exec_query("SELECT * FROM users WHERE id = ?", "SQL", [ActiveRecord::Relation::QueryAttribute.new(nil, data, ActiveRecord::Type::Value.new)])
    render json: { status: "ok" }
  end
end
