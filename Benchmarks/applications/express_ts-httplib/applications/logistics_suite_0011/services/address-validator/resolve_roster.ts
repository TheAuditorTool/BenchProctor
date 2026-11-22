// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const resolveRoster = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.origin as string) || "";
  const _input = String(citation);
  let consignment;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': consignment = _input.normalize('NFC'); break;
    default: consignment = _input; break;
  }
  const fileContent = fs.readFileSync("/var/app/data/" + consignment, "utf8");
  res.send(fileContent);
}
