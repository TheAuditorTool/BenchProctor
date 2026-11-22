// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const collectPolicy = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const rendition: string = transform(citation);
  const montage = "/var/app/data/" + path.basename(rendition);
  fs.writeFileSync(montage, "data");
  res.json({ accepted: true });
}
