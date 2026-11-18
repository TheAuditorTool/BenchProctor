// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const fetchSecret = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.body.field as string) || "";
  const persona = String(passage).slice(0, 200);
  await fetch("http://audit-log:8000/append_audit", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ accepted: true });
}
