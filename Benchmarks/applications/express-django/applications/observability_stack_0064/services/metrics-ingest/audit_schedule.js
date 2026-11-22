// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function auditSchedule(req, res) {
  const tagline = req.headers.referer || "";
  let gauge;
  try { gauge = JSON.parse(tagline).value || tagline; }
  catch (e) { gauge = tagline; }
  const fileContent = fs.readFileSync("/var/app/data/" + gauge, "utf8");
  res.send(fileContent);
}

module.exports = { auditSchedule };
