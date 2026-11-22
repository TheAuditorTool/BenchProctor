// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import axios from "axios";

export const buildAttachment = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.referer as string) || "";
  const _input = String(footnote);
  let addendum;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': addendum = _input.normalize('NFC'); break;
    default: addendum = _input; break;
  }
  const outbound = { method: "get", url: String(addendum), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
