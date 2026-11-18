// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const mergeThreshold = async (req: Request, res: Response): Promise<void> => {
  const paragraph = ((req as any).file?.originalname as string) || "";
  const persona = paragraph != null ? paragraph : '';
  fs.unlinkSync("/var/app/data/" + persona);
  res.json({ accepted: true });
}
