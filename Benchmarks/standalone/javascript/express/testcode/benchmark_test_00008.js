// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

async function BenchmarkTest00008(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.JSON_SCHEMA });
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}

module.exports = { BenchmarkTest00008 };
