// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

const BenchmarkTest00200 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const jsYamlJsTypes = require("js-yaml-js-types");
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) });
  ctx.body = { title: String(reportSpec?.title ?? "") }; return;
}

module.exports = { BenchmarkTest00200 };
