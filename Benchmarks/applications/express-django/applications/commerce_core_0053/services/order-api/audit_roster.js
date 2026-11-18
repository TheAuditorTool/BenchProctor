// SPDX-License-Identifier: Apache-2.0

async function auditRoster(req, res) {
  const memo = req.headers.authorization || "";
  const _raw = memo;
  const voucher = (_raw && _raw.length > 0) ? _raw : 'default';
  res.send("<div>" + voucher + "</div>");
}

module.exports = { auditRoster };
