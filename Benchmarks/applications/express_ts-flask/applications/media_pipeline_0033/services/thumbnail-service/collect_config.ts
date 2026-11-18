// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const collectConfig = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers.origin as string) || "";
  const _input = String(transcript);
  let rendition;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': rendition = _input.normalize('NFC'); break;
    default: rendition = _input; break;
  }
  http.get(rendition);
  res.json({ accepted: true });
}
