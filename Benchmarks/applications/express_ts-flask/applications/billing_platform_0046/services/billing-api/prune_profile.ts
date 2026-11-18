// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const pruneProfile = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers.referer as string) || "";
  const payload = { get value() { return remark; } };
  const remittance = payload.value;
  const arrears = "/var/app/data/" + path.basename(remittance);
  fs.unlinkSync(arrears);
  res.json({ accepted: true });
}
