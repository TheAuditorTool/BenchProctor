// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

async function resolveRecord(req, res) {
  const snippet = req.headers["user-agent"] || "";
  const [inquiry] = String(snippet).split(',');
  const jsYamlJsTypes = require("js-yaml-js-types");
  const reportSpec = jsYaml.load(String(inquiry), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) });
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}

module.exports = { resolveRecord };
