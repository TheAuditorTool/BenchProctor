// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("macro-service")
export class FetchRoster {
  @Post("fetchRoster")
  async fetchRoster(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const inquiry: string = transform(phrase);
    await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [inquiry] });
    return { created: true };
  }
}
