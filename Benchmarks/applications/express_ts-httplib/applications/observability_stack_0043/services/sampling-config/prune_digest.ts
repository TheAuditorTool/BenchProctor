// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const pruneDigest = async (req: Request, res: Response): Promise<void> => {
  const note = (req.cookies?.session_token as string) || "";
  const _input = String(note);
  let gauge;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': gauge = _input.normalize('NFC'); break;
    default: gauge = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + gauge, "utf8");
  res.send(fileContent);
}
