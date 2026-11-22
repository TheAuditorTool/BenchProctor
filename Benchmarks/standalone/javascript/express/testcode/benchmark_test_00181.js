// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const jsYaml = require("js-yaml");

async function BenchmarkTest00181(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.CORE_SCHEMA });
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}

module.exports = { BenchmarkTest00181 };
