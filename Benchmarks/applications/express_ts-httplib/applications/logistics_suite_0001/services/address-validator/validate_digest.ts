// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const validateDigest = async (req: Request, res: Response): Promise<void> => {
  const quotation = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const parcel: string = transform(quotation);
  const consignment = "/var/app/data/" + path.basename(parcel);
  fs.writeFileSync(consignment, "data");
  res.json({ accepted: true });
}
