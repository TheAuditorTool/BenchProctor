// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const auditHeader = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.origin as string) || "";
  const _input = String(summary);
  let restock;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': restock = _input.normalize('NFC'); break;
    default: restock = _input; break;
  }
  http.get(restock);
  res.json({ accepted: true });
}
