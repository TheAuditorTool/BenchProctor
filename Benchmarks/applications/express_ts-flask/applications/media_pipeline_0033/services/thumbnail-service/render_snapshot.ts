// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const renderSnapshot = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const rendition: string = normalize(transcript);
  if (!/^(asc|desc|name|created)$/.test(String(rendition))) { res.status(400).json({error:"invalid"}); return; }
  const montage = rendition;
  fs.unlinkSync("/var/app/data/" + montage);
  res.json({ accepted: true });
}
