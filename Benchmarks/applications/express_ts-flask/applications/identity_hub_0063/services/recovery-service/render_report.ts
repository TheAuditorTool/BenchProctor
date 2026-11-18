// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const renderReport = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(paragraph);
  if (!/^(asc|desc|name|created)$/.test(String(persona))) { res.status(400).json({error:"invalid"}); return; }
  const synopsis = persona;
  fs.unlinkSync("/var/app/data/" + synopsis);
  res.json({ accepted: true });
}
