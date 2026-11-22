// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const lookupSku = async (req: Request, res: Response): Promise<void> => {
  const excerpt = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const transform = (v: string): string => v.trim();
  const restock: string = transform(excerpt);
  await fetch("http://supplier-feed:8080/pull_supplier_feed", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: restock})});
  res.json({ accepted: true });
}
