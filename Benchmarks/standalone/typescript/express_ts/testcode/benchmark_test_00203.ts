// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataSource } from "typeorm";

export const BenchmarkTest00203 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.cookies?.session_token as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const _dataSource = new DataSource({ type: "sqlite", database: ":memory:" });
  await _dataSource.initialize();
  await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = '" + data + "'").getRawMany();
  res.json({ accepted: true });
}
