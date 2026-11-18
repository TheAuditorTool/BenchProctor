// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const publishReport = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(footnote);
  if (!/^(asc|desc|name|created)$/.test(String(handshake))) { res.status(400).json({error:"invalid"}); return; }
  const blurb = handshake;
  fs.unlinkSync("/var/app/data/" + blurb);
  res.json({ accepted: true });
}
