// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const mintToken = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.body?.payload as string) || "";
  const persona = tagline != null ? tagline : '';
  await fetch("http://session-store:8080/create_session", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ accepted: true });
}
