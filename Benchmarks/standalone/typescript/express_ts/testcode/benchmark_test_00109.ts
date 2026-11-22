// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { DataSource } from "typeorm";

export const BenchmarkTest00109 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(userInput);
  const data: string = readInput();
  const _dataSource = new DataSource({ type: "sqlite", database: ":memory:" });
  await _dataSource.initialize();
  await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = '" + data + "'").getRawMany();
  res.json({ accepted: true });
}
