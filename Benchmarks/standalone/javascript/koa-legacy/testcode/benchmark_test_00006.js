// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00006 = async (ctx) => {
  const userInput = ctx.query.id || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const axios = require("axios");
  const outbound = { method: "get", url: String(data), timeout: 5000 };
  await axios.request(outbound);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00006 };
