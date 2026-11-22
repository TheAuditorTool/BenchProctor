// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as ldapjs from "ldapjs";

export const BenchmarkTest00087 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.origin as string) || "";
  const [data] = String(userInput).split(',');
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const ldapClient = ldapjs.createClient({ url: process.env.LDAP_URL || "ldap://directory:1389" });
  ldapClient.on("error", () => {});
  const password = String(req.body?.password ?? "");
  if (!password) { res.status(400).json({ error: "password required" }); return; }
  const authenticated = await new Promise<boolean>((resolve) => {
    ldapClient.bind("uid=" + processed + ",ou=people,dc=example,dc=com", password, (err: Error | null) => { ldapClient.unbind(); resolve(!err); });
  });
  res.json({ authenticated }); return;
}
