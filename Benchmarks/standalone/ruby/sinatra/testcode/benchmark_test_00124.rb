# SPDX-License-Identifier: Apache-2.0
require "sinatra/base"
require "json"
require "uri"
require "openssl"
require "dry/schema"
require "net/ldap"

class BenchmarkTest00124 < Sinatra::Base
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
  post "/benchmark_test_00124" do
    user_input = JSON.parse(request.body.read).fetch("payload", "")
    attrs = { value: user_input.to_s }
    data = attrs[:value]
    schema = Dry::Schema.Params { required(:value).filled(:string, format?: /\A[a-zA-Z0-9 _.#%\-]+\z/) }
    unless schema.call(value: data.to_s).success?
      halt 400, JSON.generate({ error: "invalid" })
      return
    end
    processed = data
    _ldap_url = URI(ENV.fetch("LDAP_URL", "ldap://directory:1389"))
    ldap = Net::LDAP.new(host: _ldap_url.host, port: _ldap_url.port, auth: { method: :simple, username: ENV.fetch("LDAP_BIND_DN"), password: ENV.fetch("LDAP_BIND_PASSWORD") })
    ldap.replace_attribute("uid=" + processed.to_s + ",ou=people,dc=example,dc=com", :description, "reviewed")
    content_type :json
    JSON.generate({ status: "ok" })
  end
end
