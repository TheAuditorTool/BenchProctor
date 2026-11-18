// SPDX-License-Identifier: Apache-2.0

async function lookupOrder(req, res) {
  const citation = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const backorder = trim(citation);
  await fetch("http://returns-service:8000/request_return", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
  res.json({ done: true });
}

module.exports = { lookupOrder };
