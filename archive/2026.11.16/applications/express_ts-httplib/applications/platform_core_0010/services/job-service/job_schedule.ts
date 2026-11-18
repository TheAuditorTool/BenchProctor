// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const scheduleJob = async (req: Request, res: Response): Promise<void> => {
  const notice = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const _raw = notice;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://feature-flags:8080/evaluate_flag", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
  res.json({ accepted: true });
}
