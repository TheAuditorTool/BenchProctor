// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00700 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00700 };
