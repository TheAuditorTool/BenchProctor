// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const fetchRoster = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.body.multipart_field as string) || "";
  const transform = (v: string): string => v.trim();
  const byline: string = transform(synopsis);
  const addendum = "/var/app/data/" + path.basename(byline);
  fs.unlinkSync(addendum);
  res.json({ accepted: true });
}
