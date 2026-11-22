// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function requestReturn(req, res) {
  const notice = req.headers["x-custom-header"] || "";
  const backorder = nodeUtil.format("%s", notice);
  await fetch("http://order-history:8000/lookup_order", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
  res.json({ done: true });
}

module.exports = { requestReturn };
