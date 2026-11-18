// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const pullSupplierFeed = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.referer as string) || "";
  const payload = { get value() { return summary; } };
  const restock = payload.value;
  await fetch("http://allocation-service:8000/solve_allocation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: restock})});
  res.json({ accepted: true });
}
