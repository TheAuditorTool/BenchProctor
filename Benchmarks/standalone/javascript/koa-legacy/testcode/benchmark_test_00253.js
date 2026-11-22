// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00253 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const data = `${userInput}`;
  const axios = require("axios");
  const outbound = { method: "get", url: String(data), timeout: 5000 };
  await axios.request(outbound);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00253 };
