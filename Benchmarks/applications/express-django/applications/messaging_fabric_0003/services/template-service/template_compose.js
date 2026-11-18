// SPDX-License-Identifier: Apache-2.0

async function composeTemplate(req, res) {
  const subject = req.body.field || "";
  const bulletin = decodeURIComponent(subject);
  await fetch("http://presence-service:8000/update_presence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
  res.json({ done: true });
}

module.exports = { composeTemplate };
