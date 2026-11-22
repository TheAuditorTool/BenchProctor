// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

const BenchmarkTest00038 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = `${userInput}`;
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.JSON_SCHEMA });
  ctx.body = { title: String(reportSpec?.title ?? "") }; return;
}

module.exports = { BenchmarkTest00038 };
