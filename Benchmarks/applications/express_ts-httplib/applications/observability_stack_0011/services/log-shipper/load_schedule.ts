// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const loadSchedule = async (req: Request, res: Response): Promise<void> => {
  const caption = ((req as any).file?.originalname as string) || "";
  const _raw = caption;
  const gauge = (_raw && _raw.length > 0) ? _raw : 'default';
  const fileContent = fs.readFileSync("/var/app/data/" + gauge, "utf8");
  res.send(fileContent);
}
