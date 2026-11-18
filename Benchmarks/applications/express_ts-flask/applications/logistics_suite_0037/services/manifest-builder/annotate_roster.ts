// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const annotateRoster = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const consignment: string = normalize(footnote);
  if (!/^(asc|desc|name|created)$/.test(String(consignment))) { res.status(400).json({error:"invalid"}); return; }
  const parcel = consignment;
  fs.unlinkSync("/var/app/data/" + parcel);
  res.json({ accepted: true });
}
