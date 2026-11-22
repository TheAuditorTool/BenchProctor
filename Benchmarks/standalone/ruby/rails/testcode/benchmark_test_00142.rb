# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "active_model"
require "net/ldap"

class BenchmarkTest00142Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00142
    user_input = request.headers["Authorization"].to_s
    data = format("%<value>s", value: user_input)
    validator = Class.new do
      include ActiveModel::Validations
      attr_accessor :value
      validates :value, format: { with: /\A[a-zA-Z0-9 _.#%\-]+\z/ }
    end.new
    validator.value = data.to_s
    unless validator.valid?
      render json: { error: "invalid" }, status: 400
      return
    end
    processed = data
    _ldap_url = URI(ENV.fetch("LDAP_URL", "ldap://directory:1389"))
    ldap = Net::LDAP.new(host: _ldap_url.host, port: _ldap_url.port)
    ldap.search(base: "dc=example,dc=com", filter: "(cn=" + processed.to_s + ")")
    render json: { status: "ok" }
  end
end
