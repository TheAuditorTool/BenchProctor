// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

async function enrichThreshold(req, res) {
  const snippet = req.body?.multipart_field || "";
  const payload = { get value() { return snippet; } };
  const montage = payload.value;
  const jsYamlJsTypes = require("js-yaml-js-types");
  const reportSpec = jsYaml.load(String(montage), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) });
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}

module.exports = { enrichThreshold };
