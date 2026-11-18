// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const fetchBatch = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.body.multipart_field as string) || "";
  const transform = (v: string): string => v.trim();
  const voucher: string = transform(heading);
  const backorder = "/var/app/data/" + path.basename(voucher);
  fs.unlinkSync(backorder);
  res.json({ accepted: true });
}
