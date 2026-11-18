# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"

class BenchmarkTest00102Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00102
    user_input = params.require(:request_data).permit(:payload)[:payload].to_s
    data = user_input.split(/[ \t]+/).join(" ")
    ActiveRecord::Base.connection.execute("SELECT * FROM " + ActiveRecord::Base.connection.quote_column_name(data))
    render json: { status: "ok" }
  end
end
