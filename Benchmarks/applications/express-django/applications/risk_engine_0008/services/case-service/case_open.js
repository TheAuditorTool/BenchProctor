// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function openCase(req, res) {
  const synopsis = req.headers["user-agent"] || "";
  const verdict = nodeUtil.format("%s", synopsis);
  await fetch("http://decision-log:8000/record_decision", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: verdict})});
  res.json({ done: true });
}

module.exports = { openCase };
