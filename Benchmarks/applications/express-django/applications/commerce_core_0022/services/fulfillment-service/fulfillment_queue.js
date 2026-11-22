// SPDX-License-Identifier: Apache-2.0

async function queueFulfillment(req, res) {
  const subject = req.headers["user-agent"] || "";
  await fetch("http://promo-service:8000/apply_promo", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: subject})});
  res.json({ done: true });
}

module.exports = { queueFulfillment };
