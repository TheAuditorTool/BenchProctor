// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

const BenchmarkTest00239 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.CORE_SCHEMA });
  ctx.body = { title: String(reportSpec?.title ?? "") }; return;
}

module.exports = { BenchmarkTest00239 };
