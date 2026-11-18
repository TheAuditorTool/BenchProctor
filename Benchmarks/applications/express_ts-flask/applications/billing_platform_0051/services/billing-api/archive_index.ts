// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const archiveIndex = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const arrears: string = normalize(synopsis);
  if (!/^(asc|desc|name|created)$/.test(String(arrears))) { res.status(400).json({error:"invalid"}); return; }
  const dunning = arrears;
  fs.unlinkSync("/var/app/data/" + dunning);
  res.json({ accepted: true });
}
