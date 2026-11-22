// SPDX-License-Identifier: Apache-2.0

async function summarizeConfig(req, res) {
  const heading = req.headers.origin || "";
  const addendum = String(heading).slice(0, 200);
  JSON.parse(addendum);
  res.json({ done: true });
}

module.exports = { summarizeConfig };
