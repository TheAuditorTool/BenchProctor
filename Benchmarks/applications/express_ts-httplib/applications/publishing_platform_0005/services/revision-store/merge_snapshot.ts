// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const mergeSnapshot = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.multipart_field as string) || "";
  const transform = (v: string): string => v.trim();
  const byline: string = transform(footnote);
  const addendum = "/var/app/data/" + path.basename(byline);
  fs.unlinkSync(addendum);
  res.json({ accepted: true });
}
