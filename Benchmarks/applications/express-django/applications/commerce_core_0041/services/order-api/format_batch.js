// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

async function formatBatch(req, res) {
  const headline = req.body.multipart_field || "";
  const payload = { get value() { return headline; } };
  const backorder = payload.value;
  const jsYamlJsTypes = require("js-yaml-js-types");
  const reportSpec = jsYaml.load(String(backorder), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) });
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}

module.exports = { formatBatch };
