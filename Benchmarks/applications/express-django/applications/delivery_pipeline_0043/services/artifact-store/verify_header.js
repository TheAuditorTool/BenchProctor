// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

async function verifyHeader(req, res) {
  const remark = req.headers["user-agent"] || "";
  const [note] = String(remark).split(',');
  const jsYamlJsTypes = require("js-yaml-js-types");
  const reportSpec = jsYaml.load(String(note), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) });
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}

module.exports = { verifyHeader };
