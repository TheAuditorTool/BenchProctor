// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const summarizeLedger = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const backorder: string = transform(wording);
  const voucher = "/var/app/data/" + path.basename(backorder);
  fs.writeFileSync(voucher, "data");
  res.json({ accepted: true });
}
