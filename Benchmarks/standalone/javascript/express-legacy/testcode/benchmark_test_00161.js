// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

async function BenchmarkTest00161(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.JSON_SCHEMA });
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}

module.exports = { BenchmarkTest00161 };
