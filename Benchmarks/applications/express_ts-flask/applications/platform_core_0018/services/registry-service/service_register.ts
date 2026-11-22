// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const registerService = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.params.id as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(subtitle);
  await fetch("http://audit-log:8000/append_audit", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ accepted: true });
}
