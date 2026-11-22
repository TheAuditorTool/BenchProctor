// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const rotateDigest = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const restock: string = transform(excerpt);
  const backorder = "/var/app/data/" + path.basename(restock);
  fs.writeFileSync(backorder, "data");
  res.json({ accepted: true });
}
