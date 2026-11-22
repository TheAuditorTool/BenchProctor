// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

async function BenchmarkTest00145(req, res) {
  const userInput = req.body || "";
  const data = `${userInput}`;
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.JSON_SCHEMA });
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}

module.exports = { BenchmarkTest00145 };
