// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const auditRoster = async (req: Request, res: Response): Promise<void> => {
  const preface = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const _raw = preface;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  const paragraph = handshake.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + paragraph + "</div>");
}
