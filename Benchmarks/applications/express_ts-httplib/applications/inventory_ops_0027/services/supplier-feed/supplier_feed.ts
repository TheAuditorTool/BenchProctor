// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const pullSupplierFeed = async (req: Request, res: Response): Promise<void> => {
  const summary = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _input = String(summary);
  let restock;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': restock = _input.normalize('NFC'); break;
    default: restock = _input; break;
  }
  await fetch("http://allocation-service:8080/solve_allocation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: restock})});
  res.json({ accepted: true });
}
