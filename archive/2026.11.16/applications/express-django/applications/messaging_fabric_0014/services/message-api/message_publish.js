// SPDX-License-Identifier: Apache-2.0

async function publishMessage(req, res) {
  const summary = req.headers["x-forwarded-for"] || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(summary);
  const bulletin = readInput();
  await fetch("http://presence-service:8000/update_presence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ done: true });
}

module.exports = { publishMessage };
