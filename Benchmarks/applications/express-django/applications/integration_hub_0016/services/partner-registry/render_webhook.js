// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

async function renderWebhook(req, res) {
  const wording = req.body.multipart_field || "";
  const payload = { get value() { return wording; } };
  const handshake = payload.value;
  const jsYamlJsTypes = require("js-yaml-js-types");
  const reportSpec = jsYaml.load(String(handshake), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) });
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}

module.exports = { renderWebhook };
