// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const reconcileManifest = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.referer as string) || "";
  const payload = { get value() { return citation; } };
  const parcel = payload.value;
  const fileContent = fs.readFileSync("/var/app/data/" + parcel, "utf8");
  res.send(fileContent);
}
