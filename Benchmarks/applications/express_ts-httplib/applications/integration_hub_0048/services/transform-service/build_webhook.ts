// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const buildWebhook = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body.field as string) || "";
  const pending: string[] = String(citation).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const handshake: string = collected.join(',');
  const resolved = path.resolve("/var/app/data", handshake);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const heading = resolved;
  const fileContent = fs.readFileSync(heading, "utf8");
  res.send(fileContent);
}
