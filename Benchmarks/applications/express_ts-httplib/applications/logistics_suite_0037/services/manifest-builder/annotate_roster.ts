// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";

export const annotateRoster = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.multipart_field as string) || "";
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(footnote);
  const parcel = "/var/app/data/" + path.basename(consignment);
  fs.unlinkSync(parcel);
  res.json({ accepted: true });
}
