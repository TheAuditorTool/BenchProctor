// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const normalizeCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.headers.origin as string) || "";
  const _input = String(notice);
  let backorder;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': backorder = _input.normalize('NFC'); break;
    default: backorder = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + backorder, "utf8");
  res.send(fileContent);
}
