// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const summarizeSnapshot = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.origin as string) || "";
  const _input = String(citation);
  let parcel;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': parcel = _input.normalize('NFC'); break;
    default: parcel = _input; break;
  }
  http.get(parcel);
  res.json({ accepted: true });
}
