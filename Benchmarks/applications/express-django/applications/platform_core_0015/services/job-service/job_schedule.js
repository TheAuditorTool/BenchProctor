// SPDX-License-Identifier: Apache-2.0

async function scheduleJob(req, res) {
  const note = req.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: note });
  const handshake = formData.payload;
  await fetch("http://platform-api:8000/provision_tenant", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: handshake})});
  res.json({ done: true });
}

module.exports = { scheduleJob };
