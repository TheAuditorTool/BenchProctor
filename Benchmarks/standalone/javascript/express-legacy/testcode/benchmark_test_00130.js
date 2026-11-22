// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

async function BenchmarkTest00130(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const jsYamlJsTypes = require("js-yaml-js-types");
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) });
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}

module.exports = { BenchmarkTest00130 };
