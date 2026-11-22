// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00308 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const data = nodeUtil.format("%s", userInput);
  ctx.respond = false;
  return ctx.res.writeHead(303, { Location: String(data) }).end();
}

module.exports = { BenchmarkTest00308 };
