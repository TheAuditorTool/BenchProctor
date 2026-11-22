// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

const BenchmarkTest00079 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const jsYamlJsTypes = require("js-yaml-js-types");
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) });
  ctx.body = { title: String(reportSpec?.title ?? "") }; return;
}

module.exports = { BenchmarkTest00079 };
