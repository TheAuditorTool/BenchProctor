// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

const BenchmarkTest00077 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  const jsYamlJsTypes = require("js-yaml-js-types");
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) });
  ctx.body = { title: String(reportSpec?.title ?? "") }; return;
}

module.exports = { BenchmarkTest00077 };
