// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const buildLedger = async (req: Request, res: Response): Promise<void> => {
  const passage = ((req as any).file?.originalname as string) || "";
  const montage = passage != null ? passage : '';
  fs.unlinkSync("/var/app/data/" + montage);
  res.json({ accepted: true });
}
