// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

async function BenchmarkTest00192(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const jsYamlJsTypes = require("js-yaml-js-types");
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) });
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}

module.exports = { BenchmarkTest00192 };
