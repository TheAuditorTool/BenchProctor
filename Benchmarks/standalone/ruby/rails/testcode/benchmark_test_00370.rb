# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "net/ldap"

class BenchmarkTest00370Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00370
    user_input = params.require(:multipart_data).permit(:multipart_field)[:multipart_field].to_s
    unless user_input =~ /\A(asc|desc|name|created)\z/
      render json: { error: "invalid" }, status: 400
      return
    end
    processed = user_input
    _ldap_url = URI(ENV.fetch("LDAP_URL", "ldap://directory:1389"))
    ldap = Net::LDAP.new(host: _ldap_url.host, port: _ldap_url.port)
    ldap.search(base: "dc=example,dc=com", filter: "(cn=" + processed.to_s + ")")
    render json: { status: "ok" }
  end
end
