// SPDX-License-Identifier: Apache-2.0

async function schedulePublication(req, res) {
  const note = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  const trim = (v) => String(v).trim();
  const byline = trim(note);
  await fetch("http://asset-library:8000/attach_asset", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
  res.json({ done: true });
}

module.exports = { schedulePublication };
