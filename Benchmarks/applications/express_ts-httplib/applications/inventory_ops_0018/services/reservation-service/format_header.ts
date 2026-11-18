// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const formatHeader = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers["x-custom-header"] as string) || "";
  const _input = String(transcript);
  let backorder;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': backorder = _input.normalize('NFC'); break;
    default: backorder = _input; break;
  }
  fs.writeFileSync("/var/uploads/" + backorder, "data");
  res.json({ accepted: true });
}
