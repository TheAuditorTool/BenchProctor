// SPDX-License-Identifier: Apache-2.0

async function recordBounce(req, res) {
  const preface = process.env.MESSAGING_INPUT_0012 || "";
  const payload = { get value() { return preface; } };
  const bulletin = payload.value;
  await fetch("http://delivery-service:8000/dispatch_delivery", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ done: true });
}

module.exports = { recordBounce };
