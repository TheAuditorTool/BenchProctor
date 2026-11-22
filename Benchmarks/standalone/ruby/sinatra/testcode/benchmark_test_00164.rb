# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "net/ldap"
require "sequel"

DB = Sequel.connect(ENV.fetch("DATABASE_URL", "sqlite:///tmp/app.db")) unless defined?(DB)

class BenchmarkTest00164 < Sinatra::Base
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
  post "/benchmark_test_00164" do
    user_input = DB[:comments].first&.fetch(:text, "").to_s
    unless user_input =~ /\A[a-zA-Z0-9 _.#%\-]+\z/
      halt 400, JSON.generate({ error: "invalid" })
      return
    end
    processed = user_input
    password = params[:password].to_s
    if password.empty?
      halt 400, JSON.generate({ error: "password required" })
      return
    end
    _ldap_url = URI(ENV.fetch("LDAP_URL", "ldap://directory:1389"))
    ldap = Net::LDAP.new(host: _ldap_url.host, port: _ldap_url.port)
    account = ldap.bind_as(base: "ou=people,dc=example,dc=com", filter: "(uid=" + processed.to_s + ")", password: password)
    unless account
      halt 401, JSON.generate({ error: "invalid credentials" })
      return
    end
    content_type :json
    JSON.generate({ dn: account.first.dn })
  end
end
