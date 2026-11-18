// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const storeArchive = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.origin as string) || "";
  const _input = String(note);
  let addendum;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': addendum = _input.normalize('NFC'); break;
    default: addendum = _input; break;
  }
  await fetch("http://ocr-service:8000/extract_text", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
  res.json({ accepted: true });
}
