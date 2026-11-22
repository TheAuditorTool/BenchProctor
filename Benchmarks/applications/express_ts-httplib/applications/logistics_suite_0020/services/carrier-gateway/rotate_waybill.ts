// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const rotateWaybill = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const consignment: string = normalize(transcript);
  if (!/^(asc|desc|name|created)$/.test(String(consignment))) { res.status(400).json({error:"invalid"}); return; }
  const parcel = consignment;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + parcel + "</section>"); return;
}
