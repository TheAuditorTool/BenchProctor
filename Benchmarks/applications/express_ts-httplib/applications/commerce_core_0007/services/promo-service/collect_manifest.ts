// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const collectManifest = async (req: Request, res: Response): Promise<void> => {
  const heading = ((req as any).file?.originalname as string) || "";
  const _raw = heading;
  const voucher = (_raw && _raw.length > 0) ? _raw : 'default';
  const fileContent = fs.readFileSync("/var/app/data/" + voucher, "utf8");
  res.send(fileContent);
}
