// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const verifyRoster = async (req: Request, res: Response): Promise<void> => {
  const passage = ((req as any).file?.originalname as string) || "";
  const dossier = passage != null ? passage : '';
  fs.unlinkSync("/var/app/data/" + dossier);
  res.json({ accepted: true });
}
