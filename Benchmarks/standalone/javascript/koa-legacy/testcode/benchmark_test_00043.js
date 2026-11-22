// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

const BenchmarkTest00043 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.JSON_SCHEMA });
  ctx.body = { title: String(reportSpec?.title ?? "") }; return;
}

module.exports = { BenchmarkTest00043 };
