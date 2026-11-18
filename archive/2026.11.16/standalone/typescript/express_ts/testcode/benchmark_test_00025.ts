// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { Sequelize } from "sequelize";

export const BenchmarkTest00025 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.payload as string) || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  const _coerced = parseInt(String(data), 10);
  const parsedId = _coerced;
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + parsedId + "'");
  res.json({ accepted: true });
}
