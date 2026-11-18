// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const annotateDelivery = async (req: Request, res: Response): Promise<void> => {
  const summary = ((req as any).file?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const bulletin: string = normalize(summary);
  const resolved = path.resolve("/var/app/data", bulletin);
  if (!resolved.startsWith("/var/app/data/")) { res.status(403).json({error:"forbidden"}); return; }
  const snippet = resolved;
  fs.writeFileSync(snippet, "data");
  res.json({ accepted: true });
}
