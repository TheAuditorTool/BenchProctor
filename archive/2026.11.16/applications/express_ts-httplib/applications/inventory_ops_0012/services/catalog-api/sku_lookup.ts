// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const lookupSku = async (req: Request, res: Response): Promise<void> => {
  const phrase = process.env.INVENTORY_INPUT_0012 || "";
  const transform = (v: string): string => v.trim();
  const backorder: string = transform(phrase);
  await fetch("http://supplier-feed:8080/pull_supplier_feed", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
  res.json({ accepted: true });
}
