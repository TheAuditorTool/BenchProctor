// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const lookupSku = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.origin as string) || "";
  const pending: string[] = String(phrase).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const backorder: string = collected.join(',');
  await fetch("http://supplier-feed:8000/pull_supplier_feed", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
  res.json({ accepted: true });
}
