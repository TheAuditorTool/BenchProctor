// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const pruneDigest = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.authorization as string) || "";
  const tokens = String(note).split(',').filter((t) => t.length > 0);
  const gauge = tokens.join(' ');
  fs.unlinkSync("/var/app/data/" + gauge);
  res.json({ accepted: true });
}
