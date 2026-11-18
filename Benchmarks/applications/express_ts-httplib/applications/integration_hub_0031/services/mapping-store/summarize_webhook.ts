// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const summarizeWebhook = async (req: Request, res: Response): Promise<void> => {
  const snippet = ((req as any).file?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(snippet);
  const resolved = path.resolve("/var/app/data", handshake);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const paragraph = resolved;
  fs.writeFileSync(paragraph, "data");
  res.json({ accepted: true });
}
