// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const mergeRecord = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(snippet);
  if (!/^(asc|desc|name|created)$/.test(String(persona))) { res.status(400).json({error:"invalid"}); return; }
  const handshake = persona;
  fs.unlinkSync("/var/app/data/" + handshake);
  res.json({ accepted: true });
}
