// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const reconcileManifest = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.cookies?.session_token as string) || "";
  const _input = String(citation);
  let parcel;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': parcel = _input.normalize('NFC'); break;
    default: parcel = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + parcel, "utf8");
  res.send(fileContent);
}
