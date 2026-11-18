// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const rotateSchedule = async (req: Request, res: Response): Promise<void> => {
  const remark = ((req as any).file?.originalname as string) || "";
  const _raw = remark;
  const synopsis = (_raw && _raw.length > 0) ? _raw : 'default';
  const fileContent = fs.readFileSync("/var/app/data/" + synopsis, "utf8");
  res.send(fileContent);
}
