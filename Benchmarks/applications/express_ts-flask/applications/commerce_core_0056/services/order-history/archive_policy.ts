// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const archivePolicy = async (req: Request, res: Response): Promise<void> => {
  const citation = ((req as any).file?.originalname as string) || "";
  const backorder = citation != null ? citation : '';
  fs.unlinkSync("/var/app/data/" + backorder);
  res.json({ accepted: true });
}
