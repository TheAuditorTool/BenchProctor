// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const resolveLedger = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers["x-forwarded-for"] as string) || "";
  const _input = String(subject);
  let parcel;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': parcel = _input.normalize('NFC'); break;
    default: parcel = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + parcel, "utf8");
  res.send(fileContent);
}
