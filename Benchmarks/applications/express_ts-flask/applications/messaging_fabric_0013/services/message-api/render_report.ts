// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const renderReport = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const bulletin: string = normalize(summary);
  if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { res.status(400).json({error:"invalid"}); return; }
  const snippet = bulletin;
  fs.unlinkSync("/var/app/data/" + snippet);
  res.json({ accepted: true });
}
