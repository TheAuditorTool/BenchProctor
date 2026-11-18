// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const fetchSecret = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.body.multipart_field as string) || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(passage);
  await fetch("http://audit-log:8080/append_audit", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ accepted: true });
}
