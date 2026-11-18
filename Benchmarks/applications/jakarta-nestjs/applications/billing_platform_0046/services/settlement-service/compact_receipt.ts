// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

@Controller("settlement-service")
export class CompactReceipt {
  @Post("compactReceipt")
  async compactReceipt(@Req() req: Request): Promise<unknown> {
    const remark = fs.readFileSync("/tmp/data", "utf8");
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(remark);
    const remittance: string = readInput();
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [remittance] });
    return { created: true };
  }
}
