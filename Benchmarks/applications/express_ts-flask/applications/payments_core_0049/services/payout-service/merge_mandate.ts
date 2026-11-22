// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const mergeMandate = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.headers.referer as string) || "";
  const _input = String(headline);
  let disbursement;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': disbursement = _input.normalize('NFC'); break;
    default: disbursement = _input; break;
  }
  const outbound = { method: "get", url: String(disbursement), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
