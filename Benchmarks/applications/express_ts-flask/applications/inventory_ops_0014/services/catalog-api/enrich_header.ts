// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const enrichHeader = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers.referer as string) || "";
  const _input = String(excerpt);
  let restock;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': restock = _input.normalize('NFC'); break;
    default: restock = _input; break;
  }
  const outbound = { method: "get", url: String(restock), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
