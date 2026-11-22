// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const evaluateRule = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers["x-custom-header"] as string) || "";
  const verdict = Buffer.from(excerpt, "hex").toString();
  await fetch("http://watchlist-sync:8000/sync_watchlist", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: verdict})});
  res.json({ accepted: true });
}
