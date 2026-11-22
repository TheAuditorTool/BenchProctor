// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const buildWindow = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(remark);
  const notice = "/var/app/data/" + path.basename(persona);
  fs.writeFileSync(notice, "data");
  res.json({ accepted: true });
}
