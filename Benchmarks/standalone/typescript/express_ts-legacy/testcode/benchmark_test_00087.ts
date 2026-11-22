// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";
import * as ldapjs from "ldapjs";
import * as joi from "joi";

export const BenchmarkTest00087 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = nodeUtil.format("%s", userInput);
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.#%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(data);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const processed = _schemaVal;
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  ldapClient.compare("uid=" + processed + ",ou=people,dc=example,dc=com", "employeeType", "manager", (_err: Error | null, _matched?: boolean) => ldapClient.unbind());
  res.json({ accepted: true });
}
