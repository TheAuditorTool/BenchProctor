# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "nokogiri"

class BenchmarkTest00443Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00443
    user_input = params.require(:user).permit(:name)[:name].to_s
    pending = user_input.split(',')
    data = ''
    data = pending.shift until pending.empty?
    Nokogiri::XML(data) { |config| config.dtdload.noent.nonet }
    render json: { status: "ok" }
  end
end
