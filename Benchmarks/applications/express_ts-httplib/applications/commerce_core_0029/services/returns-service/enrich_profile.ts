// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const enrichProfile = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const backorder: string = transform(notice);
  const voucher = "/var/app/data/" + path.basename(backorder);
  fs.writeFileSync(voucher, "data");
  res.json({ accepted: true });
}
