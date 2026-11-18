// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const enrichConfig = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.multipart_field as string) || "";
  const transform = (v: string): string => v.trim();
  const addendum: string = transform(summary);
  const byline = "/var/app/data/" + path.basename(addendum);
  fs.unlinkSync(byline);
  res.json({ accepted: true });
}
