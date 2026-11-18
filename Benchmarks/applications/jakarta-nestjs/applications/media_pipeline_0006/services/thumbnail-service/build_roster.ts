// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

@Controller("thumbnail-service")
export class BuildRoster {
  @Post("buildRoster")
  async buildRoster(@Req() req: Request): Promise<unknown> {
    const passage = fs.readFileSync("/tmp/data", "utf8");
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(passage);
    const montage: string = readInput();
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [montage] });
    return { created: true };
  }
}
