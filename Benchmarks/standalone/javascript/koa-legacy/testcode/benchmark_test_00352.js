// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const jsYaml = require("js-yaml");

const BenchmarkTest00352 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const reportSpec = jsYaml.load(String(data), { schema: jsYaml.CORE_SCHEMA });
  ctx.body = { title: String(reportSpec?.title ?? "") }; return;
}

module.exports = { BenchmarkTest00352 };
