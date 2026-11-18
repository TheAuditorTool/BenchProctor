// SPDX-License-Identifier: Apache-2.0

async function createSession(req, res) {
  const excerpt = req.headers.host || "";
  const persona = `${excerpt}`;
  await fetch("http://directory-sync:8000/sync_directory", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ done: true });
}

module.exports = { createSession };
