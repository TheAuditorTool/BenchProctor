// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const mintToken = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.params.id as string) || "";
  const persona = decodeURIComponent(snippet);
  await fetch("http://mfa-service:8000/verify_mfa", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ accepted: true });
}
