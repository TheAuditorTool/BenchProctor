// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const exportIndex = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.query.id as string) || "";
  const tokens = String(snippet).split(',').filter((t) => t.length > 0);
  const persona = tokens.join(' ');
  fs.unlinkSync("/var/app/data/" + persona);
  res.json({ accepted: true });
}
