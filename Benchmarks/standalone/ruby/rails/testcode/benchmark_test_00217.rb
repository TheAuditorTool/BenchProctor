# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "net/ldap"

class BenchmarkTest00217Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00217
    user_input = params[:id].to_s
    pending = user_input.split(',')
    data = ''
    data = pending.shift until pending.empty?
    _ldap_url = URI(ENV.fetch("LDAP_URL", "ldap://directory:1389"))
    ldap = Net::LDAP.new(host: _ldap_url.host, port: _ldap_url.port, auth: { method: :simple, username: ENV.fetch("LDAP_BIND_DN"), password: ENV.fetch("LDAP_BIND_PASSWORD") })
    ldap.replace_attribute("uid=" + data.to_s + ",ou=people,dc=example,dc=com", :description, "reviewed")
    render json: { status: "ok" }
  end
end
