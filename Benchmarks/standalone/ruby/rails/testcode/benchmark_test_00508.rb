# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "net/ldap"

class BenchmarkTest00508Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00508
    user_input = request.headers["Origin"].to_s
    data = user_input.split(/[ \t]+/).join(" ")
    _ldap_url = URI(ENV.fetch("LDAP_URL", "ldap://directory:1389"))
    ldap = Net::LDAP.new(host: _ldap_url.host, port: _ldap_url.port)
    ldap.search(base: "dc=example,dc=com", filter: "(cn=" + data.to_s + ")")
    render json: { status: "ok" }
  end
end
