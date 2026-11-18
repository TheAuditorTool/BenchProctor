// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const enrichWallet = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const _raw = subtitle;
  const ledger = (_raw && _raw.length > 0) ? _raw : 'default';
  const remittance = ledger.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + remittance + "</div>");
}
