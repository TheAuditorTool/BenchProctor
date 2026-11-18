// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const reconcileBatch = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const backorder: string = normalize(citation);
  if (!/^(asc|desc|name|created)$/.test(String(backorder))) { res.status(400).json({error:"invalid"}); return; }
  const restock = backorder;
  fs.unlinkSync("/var/app/data/" + restock);
  res.json({ accepted: true });
}
