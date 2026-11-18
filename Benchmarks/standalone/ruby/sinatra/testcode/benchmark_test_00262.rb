# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "net/ldap"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00262 < Sinatra::Base
  before do
    halt 413 if request.content_length.to_i > 1_000_000
  end
  after do
    headers["X-Content-Type-Options"] = "nosniff"
  end

  error StandardError do
    content_type :json
    status 500
    JSON.generate({ error: "internal" })
  end
  post "/benchmark_test_00262" do
    user_input = DB[:users].first&.fetch(:name, "").to_s
    data = "#{user_input}"
    _ldap_url = URI(ENV.fetch("LDAP_URL", "ldap://directory:1389"))
    ldap = Net::LDAP.new(host: _ldap_url.host, port: _ldap_url.port)
    ldap.search(base: "dc=example,dc=com", filter: "(cn=" + data.to_s + ")")
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
