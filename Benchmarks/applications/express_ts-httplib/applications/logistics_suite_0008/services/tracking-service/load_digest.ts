// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const loadDigest = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.host as string) || "";
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(caption);
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(consignment)) { res.status(400).json({error:"invalid"}); return; }
  const parcel = consignment;
  const fileContent = fs.readFileSync("/var/app/data/" + parcel, "utf8");
  res.send(fileContent);
}
