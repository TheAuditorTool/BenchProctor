// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const enrichManifest = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.referer as string) || "";
  const _input = String(footnote);
  let remittance;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': remittance = _input.normalize('NFC'); break;
    default: remittance = _input; break;
  }
  const outbound = { method: "get", url: String(remittance), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
