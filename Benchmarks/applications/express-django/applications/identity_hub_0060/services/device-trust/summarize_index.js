// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

async function summarizeIndex(req, res) {
  const paragraph = req.headers["user-agent"] || "";
  const [persona] = String(paragraph).split(',');
  const jsYamlJsTypes = require("js-yaml-js-types");
  const reportSpec = jsYaml.load(String(persona), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) });
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}

module.exports = { summarizeIndex };
