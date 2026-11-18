// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const archiveRecord = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.origin as string) || "";
  const _input = String(footnote);
  let handshake;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': handshake = _input.normalize('NFC'); break;
    default: handshake = _input; break;
  }
  http.get(handshake);
  res.json({ accepted: true });
}
