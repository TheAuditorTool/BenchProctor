// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const pullSupplierFeed = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body.field as string) || "";
  const backorder = String(citation).slice(0, 200);
  await fetch("http://catalog-api:8000/lookup_sku", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
  res.json({ accepted: true });
}
