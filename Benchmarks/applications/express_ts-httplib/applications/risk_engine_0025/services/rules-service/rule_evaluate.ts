// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const evaluateRule = async (req: Request, res: Response): Promise<void> => {
  const excerpt = ((req as any).files?.[0]?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const verdict: string = normalize(excerpt);
  await fetch("http://watchlist-sync:8080/sync_watchlist", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: verdict})});
  res.json({ accepted: true });
}
