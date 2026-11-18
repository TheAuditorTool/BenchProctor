// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const formatApproval = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.headers.authorization as string) || "";
  const tokens = String(wording).split(',').filter((t) => t.length > 0);
  const remark = tokens.join(' ');
  fs.unlinkSync("/var/app/data/" + remark);
  res.json({ accepted: true });
}
