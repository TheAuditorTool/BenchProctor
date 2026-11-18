// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const buildLedger = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.cookies?.session_token as string) || "";
  const _input = String(passage);
  let montage;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': montage = _input.normalize('NFC'); break;
    default: montage = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + montage, "utf8");
  res.send(fileContent);
}
