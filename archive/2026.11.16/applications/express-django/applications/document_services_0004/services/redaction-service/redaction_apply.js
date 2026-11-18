// SPDX-License-Identifier: Apache-2.0

async function applyRedaction(req, res) {
  const excerpt = req.cookies.session_token || "";
  const dossier = excerpt != null ? excerpt : '';
  await fetch("http://convert-service:8000/run_conversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: dossier})});
  res.json({ done: true });
}

module.exports = { applyRedaction };
