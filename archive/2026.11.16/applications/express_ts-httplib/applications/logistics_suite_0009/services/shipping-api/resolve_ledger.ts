// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const resolveLedger = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.body as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const parcel: string = normalize(subject);
  fs.writeFileSync("/var/uploads/" + parcel, "data");
  res.json({ accepted: true });
}
