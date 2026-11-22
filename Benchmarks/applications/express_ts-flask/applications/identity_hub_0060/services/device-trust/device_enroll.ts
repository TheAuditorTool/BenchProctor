// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const enrollDevice = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.headers.referer as string) || "";
  const _input = String(paragraph);
  let persona;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': persona = _input.normalize('NFC'); break;
    default: persona = _input; break;
  }
  await fetch("http://profile-api:8000/update_profile", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ accepted: true });
}
