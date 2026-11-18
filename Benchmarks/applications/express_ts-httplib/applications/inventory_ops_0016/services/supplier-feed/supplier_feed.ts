// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";

export const pullSupplierFeed = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers["user-agent"] as string) || "";
  const backorder = nodeUtil.format("%s", citation);
  await fetch("http://catalog-api:8080/lookup_sku", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
  res.json({ accepted: true });
}
