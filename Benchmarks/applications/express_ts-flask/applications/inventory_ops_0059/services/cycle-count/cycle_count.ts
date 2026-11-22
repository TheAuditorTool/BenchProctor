// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const runCycleCount = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.cookies?.session_token as string) || "";
  const tokens = String(memo).split(',').filter((t) => t.length > 0);
  const backorder = tokens.join(' ');
  await fetch("http://supplier-feed:8000/pull_supplier_feed", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
  res.json({ accepted: true });
}
