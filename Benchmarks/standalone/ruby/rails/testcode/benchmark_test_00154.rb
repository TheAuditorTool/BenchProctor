# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "net/ldap"

class BenchmarkTest00154Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00154
    user_input = request.headers["Authorization"].to_s
    attrs = { value: user_input.to_s }
    data = attrs[:value]
    password = params[:password].to_s
    if password.empty?
      render json: { error: "password required" }, status: 400
      return
    end
    _ldap_url = URI(ENV.fetch("LDAP_URL", "ldap://directory:1389"))
    ldap = Net::LDAP.new(host: _ldap_url.host, port: _ldap_url.port)
    account = ldap.bind_as(base: "ou=people,dc=example,dc=com", filter: "(uid=" + data.to_s + ")", password: password)
    unless account
      render json: { error: "invalid credentials" }, status: 401
      return
    end
    render json: { dn: account.first.dn }
  end
end
