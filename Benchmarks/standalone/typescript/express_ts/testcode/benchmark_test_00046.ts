// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataTypes, Sequelize } from "sequelize";

export const BenchmarkTest00046 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  const orderColumn = '"' + String(data).replace(/"/g, '""') + '"';
  await User.findAll({ order: _sequelize.literal(orderColumn) });
  res.json({ accepted: true });
}
