// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const lookupSku = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers.host as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const restock: string = normalize(excerpt);
  await fetch("http://supplier-feed:8000/pull_supplier_feed", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: restock})});
  res.json({ accepted: true });
}
