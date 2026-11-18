// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const registerService = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.headers.referer as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(notice);
  await fetch("http://config-service:8000/rollout_config", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ accepted: true });
}
