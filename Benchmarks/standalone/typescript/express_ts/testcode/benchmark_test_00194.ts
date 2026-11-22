// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataTypes, Sequelize } from "sequelize";

export const BenchmarkTest00194 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const data = userInput != null ? userInput : '';
  const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
  const User = _sequelize.define("User", { name: DataTypes.STRING }, { tableName: "users", timestamps: false });
  await User.findAll({ where: _sequelize.literal("name = '" + data + "'") });
  res.json({ accepted: true });
}
