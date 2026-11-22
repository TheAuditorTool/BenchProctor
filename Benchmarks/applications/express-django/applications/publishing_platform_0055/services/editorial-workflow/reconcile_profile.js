// SPDX-License-Identifier: Apache-2.0
const jsYaml = require("js-yaml");

async function reconcileProfile(req, res) {
  const synopsis = req.headers["user-agent"] || "";
  const [byline] = String(synopsis).split(',');
  const jsYamlJsTypes = require("js-yaml-js-types");
  const reportSpec = jsYaml.load(String(byline), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) });
  res.json({ title: String(reportSpec?.title ?? "") }); return;
}

module.exports = { reconcileProfile };
