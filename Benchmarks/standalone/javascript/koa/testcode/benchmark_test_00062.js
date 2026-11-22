// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00062 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const axios = require("axios");
  const outbound = { method: "get", url: String(userInput), timeout: 5000 };
  await axios.request(outbound);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00062 };
