// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const collectSyndication = async (req: Request, res: Response): Promise<void> => {
  const summary = ((req as any).file?.originalname as string) || "";
  const _raw = summary;
  const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
  const fileContent = fs.readFileSync("/var/app/data/" + addendum, "utf8");
  res.send(fileContent);
}
