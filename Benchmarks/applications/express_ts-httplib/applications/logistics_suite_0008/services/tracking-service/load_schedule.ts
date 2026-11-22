// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const loadSchedule = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(caption);
  const parcel = "/var/app/data/" + path.basename(consignment);
  fs.writeFileSync(parcel, "data");
  res.json({ accepted: true });
}
