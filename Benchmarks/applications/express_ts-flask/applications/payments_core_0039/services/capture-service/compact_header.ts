// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const compactHeader = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.headers.referer as string) || "";
  const _input = String(memo);
  let ledger;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': ledger = _input.normalize('NFC'); break;
    default: ledger = _input; break;
  }
  const outbound = { method: "get", url: String(ledger), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
