// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const pruneSummary = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(caption);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(consignment)) { res.status(400).json({error:"invalid"}); return; }
  const parcel = consignment;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + parcel + "</section>"); return;
}
