// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const verifySchedule = async (req: Request, res: Response): Promise<void> => {
  const paragraph = ((req as any).file?.originalname as string) || "";
  const _raw = paragraph;
  const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
  const fileContent = fs.readFileSync("/var/app/data/" + bulletin, "utf8");
  res.send(fileContent);
}
