// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

async function BenchmarkTest00106(req, res) {
  const userInput = req.headers.origin || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.CORE_SCHEMA });
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}

module.exports = { BenchmarkTest00106 };
