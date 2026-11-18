# SPDX-License-Identifier: Apache-2.0
require "json"
require "uri"
require "openssl"
require "cgi"
require "resolv"
require "ipaddr"
require "socket"

class BenchmarkTest00306Controller < ApplicationController
  before_action { head :payload_too_large if request.content_length.to_i > 1_000_000 }
  after_action { response.set_header("X-Content-Type-Options", "nosniff") }

  rescue_from StandardError do |exception|
    render json: { error: "internal" }, status: 500
  end
  def benchmark_test_00306
    user_input = request.query_parameters[:q].to_s
    data = CGI.unescape(user_input)
    _host = (URI.parse(data).host rescue nil)
    _ip = _host ? (Resolv.getaddress(_host) rescue nil) : nil
    if _ip.nil? || "10.0.0.0/8 127.0.0.0/8 169.254.0.0/16 172.16.0.0/12 192.168.0.0/16 0.0.0.0/8 ::1/128 fc00::/7 fe80::/10".split.any? { |c| IPAddr.new(c).include?(_ip) rescue false }
      render json: { error: "private range blocked" }, status: 403
      return
    end
    target_url = data
    TCPSocket.new(target_url, 80).close
    render json: { status: "ok" }
  end
end
