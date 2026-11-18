// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00384 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00384 };
