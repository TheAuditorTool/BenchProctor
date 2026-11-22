// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { Sequelize } from "sequelize";

export const BenchmarkTest00046 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  await _sequelize.query("SELECT * FROM users WHERE id = '" + userInput + "'");
  res.json({ accepted: true });
}
